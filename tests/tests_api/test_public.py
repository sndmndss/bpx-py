import pytest
from bpx.public import Public


@pytest.fixture
def public_client():
    return Public()


def test_get_assets_returns_list(public_client: Public):
    assets = public_client.get_assets()
    assert isinstance(assets, list)


def test_get_markets_returns_list(public_client: Public):
    assert isinstance(public_client.get_markets(), list)


def test_get_ticker_returns_dict(public_client: Public):
    assert isinstance(public_client.get_ticker("SOL_USDC"), dict)


def test_get_depth_returns_dict(public_client: Public):
    assert isinstance(public_client.get_depth("SOL_USDC"), dict)


def test_get_klines_returns_list(public_client: Public):
    start_time = 1715692417
    end_time = 1715778817
    assert isinstance(public_client.get_klines("BTC_USDC", "1d", start_time, end_time), list)


def test_get_status_returns_dict(public_client: Public):
    status = public_client.get_status()
    assert isinstance(status, dict)
    assert status["status"] == "Ok"


def test_get_ping_returns_pong(public_client: Public):
    pong = public_client.get_ping()
    assert pong == "pong"


def test_get_time_returns_int(public_client: Public):
    time = public_client.get_time()
    if isinstance(time, str):
        assert time.isdigit()
    else:
        assert isinstance(time, int)


def test_get_recent_trades_returns_list(public_client: Public):
    assert isinstance(public_client.get_recent_trades("SOL_USDC"), list)


def test_get_history_trades_returns_list(public_client: Public):
    assert isinstance(public_client.get_history_trades("WEN_USDC"), list)
