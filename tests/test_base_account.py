from bpx.base.base_account import BaseAccount
import pytest
from unittest.mock import patch
from bpx.exceptions import (
    NegativeValueError,
    LimitValueError,
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
    request_config = account.get_balances(window=10000)
    assert request_config.url == "https://api.backpack.exchange/api/v1/capital"
    assert "X-API-Key" in request_config.headers


def test_get_deposits(account):
    with pytest.raises(LimitValueError):
        account.get_deposits(limit=1001, offset=0, window=10000)

    with pytest.raises(NegativeValueError):
        account.get_deposits(limit=100, offset=-1, window=10000)

    request_config = account.get_deposits(limit=100, offset=0, window=10000)
    assert (
        request_config.url == "https://api.backpack.exchange/wapi/v1/capital/deposits"
    )
    assert request_config.params["limit"] == 100
    assert request_config.params["offset"] == 0


def test_get_deposit_address(account):
    request_config = account.get_deposit_address(blockchain="Bitcoin", window=10000)
    assert (
        request_config.url
        == "https://api.backpack.exchange/wapi/v1/capital/deposit/address"
    )
    assert request_config.params["blockchain"] == "Bitcoin"


def test_signing(account):
    with patch.object(account, "_sign", return_value="mock_signature") as mock_sign:
        request_config = account.get_balances(window=10000)
        mock_sign.assert_called_once()
        assert request_config.headers["X-Signature"] == "mock_signature"


def test_withdrawal(account):
    request_config = account.withdrawal(
        address="1BitcoinAddress",
        symbol="BTC",
        blockchain="Bitcoin",
        quantity="1.0",
        window=10000,
    )
    assert (
        request_config.url
        == "https://api.backpack.exchange/wapi/v1/capital/withdrawals"
    )
    assert request_config.data["address"] == "1BitcoinAddress"
    assert request_config.data["blockchain"] == "Bitcoin"
