from bpx.base.base_account import BaseAccount
import pytest
from unittest.mock import patch
from bpx.exceptions import (
    NegativeValueError,
    LimitValueError,
    InvalidBlockchainValue,
)
import os

public_key = os.getenv("PUBLIC_KEY")
secret_key = os.getenv("SECRET_KEY")


@pytest.fixture
def account():
    return BaseAccount(
        public_key=public_key, secret_key=secret_key, window=10000, debug=False
    )


def test_initialization(account):
    assert account.public_key == public_key
    assert account.window == 10000
    assert not account.debug


def test_get_balances(account):
    url, headers = account.get_balances(window=10000)
    assert url == "https://api.backpack.exchange/api/v1/capital"
    assert "X-API-Key" in headers


def test_get_deposits(account):
    with pytest.raises(LimitValueError):
        account.get_deposits(limit=1001, offset=0, window=10000)

    with pytest.raises(NegativeValueError):
        account.get_deposits(limit=100, offset=-1, window=10000)

    url, headers, params = account.get_deposits(limit=100, offset=0, window=10000)
    assert url == "https://api.backpack.exchange/wapi/v1/capital/deposits"
    assert params["limit"] == 100
    assert params["offset"] == 0


def test_get_deposit_address(account):
    with pytest.raises(InvalidBlockchainValue):
        account.get_deposit_address(blockchain="invalid_blockchain", window=10000)

    url, headers, params = account.get_deposit_address(
        blockchain="Bitcoin", window=10000
    )
    assert url == "https://api.backpack.exchange/wapi/v1/capital/deposit/address"
    assert params["blockchain"] == "Bitcoin"


def test_signing(account):
    with patch.object(account, "_sign", return_value="mock_signature") as mock_sign:
        _, headers = account.get_balances(window=10000)
        mock_sign.assert_called_once()
        assert headers["X-Signature"] == "mock_signature"


def test_withdrawal(account):
    with pytest.raises(InvalidBlockchainValue):
        account.withdrawal(
            address="1BitcoinAddress",
            symbol="BTC",
            blockchain="invalid_blockchain",
            quantity="1.0",
            window=10000,
        )

    url, headers, params = account.withdrawal(
        address="1BitcoinAddress",
        symbol="BTC",
        blockchain="Bitcoin",
        quantity="1.0",
        window=10000,
    )
    assert url == "https://api.backpack.exchange/wapi/v1/capital/withdrawals"
    assert params["address"] == "1BitcoinAddress"
    assert params["blockchain"] == "Bitcoin"
