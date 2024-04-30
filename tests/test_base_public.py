from bpx.base.base_public import BasePublic
import pytest
from bpx.exceptions import NegativeValueError, InvalidTimeIntervalError, LimitValueError
from bpx.enums import TimeInterval


@pytest.fixture
def base_public():
    return BasePublic()

def test_get_assets_url(base_public):
    assert base_public.get_assets_url() == "https://api.backpack.exchange/api/v1/assets"


def test_get_markets_url(base_public):
    assert base_public.get_markets_url() == "https://api.backpack.exchange/api/v1/markets"


def test_get_ticker_url(base_public):
    symbol = "BTC_USD"
    expected_url = "https://api.backpack.exchange/api/v1/ticker?symbol=BTC_USD"
    assert base_public.get_ticker_url(symbol) == expected_url


def test_get_depth_url(base_public):
    symbol = "BTC_USD"
    expected_url = "https://api.backpack.exchange/api/v1/depth?symbol=BTC_USD"
    assert base_public.get_depth_url(symbol) == expected_url


def test_get_klines_url(base_public):
    symbol = "BTC_USD"
    interval = "1m"
    start_time = 1609459200
    end_time = 1609462800
    expected_url = "https://api.backpack.exchange/api/v1/klines?symbol=BTC_USD&interval=1m&startTime=1609459200&endTime=1609462800"
    assert base_public.get_klines_url(symbol, interval, start_time, end_time) == expected_url

    with pytest.raises(NegativeValueError):
        base_public.get_klines_url(symbol, interval, -1, end_time)

    with pytest.raises(InvalidTimeIntervalError):
        base_public.get_klines_url(symbol, "10x", start_time, end_time)


def test_get_recent_trades_url(base_public):
    symbol = "BTC_USD"
    limit = 100
    expected_url = "https://api.backpack.exchange/api/v1/trades?symbol=BTC_USD&limit=100"
    assert base_public.get_recent_trades_url(symbol, limit) == expected_url

    with pytest.raises(LimitValueError):
        base_public.get_recent_trades_url(symbol, -1)

    with pytest.raises(LimitValueError):
        base_public.get_recent_trades_url(symbol, 1001)


def test_get_status_url(base_public):
    assert base_public.get_status_url() == "https://api.backpack.exchange/api/v1/status"


def test_get_ping_url(base_public):
    assert base_public.get_ping_url() == "https://api.backpack.exchange/api/v1/ping"


def test_get_time_url(base_public):
    assert base_public.get_time_url() == "https://api.backpack.exchange/api/v1/time"