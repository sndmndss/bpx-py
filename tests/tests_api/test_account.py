import pytest
from bpx.account import Account
import os

public_key = os.getenv("PUBLIC_KEY")
secret_key = os.getenv("SECRET_KEY")


@pytest.fixture
def account_client():
    return Account(public_key, secret_key, window=10000)


def test_fill_history_query(account_client: Account):
    fills = account_client.get_fill_history_query("SOL_USDC", limit=50)
    assert len(fills) == 50


def test_get_withdrawal(account_client: Account):
    withdrawal = account_client.get_withdrawals(limit=3)
    assert isinstance(withdrawal, list)
    assert len(withdrawal) == 3


def test_execute_order(account_client: Account):
    order = account_client.execute_order(
        symbol="SOL_USDC",
        order_type="Limit",
        side="Bid",
        quantity=0.01,
        price=0.01,
        time_in_force="IOC",
    )
    assert isinstance(order, dict)


def test_deposits(account_client: Account):
    deposits = account_client.get_deposits(limit=3)
    assert isinstance(deposits, list)
    assert len(deposits) == 3


def test_get_balances(account_client: Account):
    balances = account_client.get_balances()
    assert isinstance(balances, dict)
    assert balances


def test_get_deposit_address(account_client: Account):
    address = account_client.get_deposit_address("Solana")
    assert isinstance(address, dict)
    assert address


def test_get_order_history_query(account_client: Account):
    orders = account_client.get_order_history_query("SOL_USDC", limit=5)
    assert isinstance(orders, list)
    assert len(orders) == 5


def test_get_open_order(account_client: Account):
    order = account_client.get_open_order("BTC_USDC", "112355467178868736")
    assert isinstance(order, dict)
    assert order["price"] == "1"


def test_cancel_order(account_client: Account):
    status = account_client.cancel_order("SOL_USDC", order_id="1")
    assert status == "Order not found"


def test_cancel_all_orders(account_client: Account):
    cancelled_orders = account_client.cancel_all_orders("SOL_USDC")
    assert isinstance(cancelled_orders, list)
