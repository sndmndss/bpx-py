import pytest
from bpx.async_.public import Public

@pytest.fixture
def public_client():
    return Public()

@pytest.mark.asyncio
async def test_get_assets_returns_list(public_client: Public):
    assets = await public_client.get_assets()
    assert isinstance(assets, list)

@pytest.mark.asyncio
async def test_get_markets_returns_list(public_client: Public):
    markets = await public_client.get_markets()
    assert isinstance(markets, list)

@pytest.mark.asyncio
async def test_get_ticker_returns_dict(public_client: Public):
    ticker = await public_client.get_ticker("SOL_USDC")
    assert isinstance(ticker, dict)

@pytest.mark.asyncio
async def test_get_depth_returns_dict(public_client: Public):
    depth = await public_client.get_depth("SOL_USDC")
    assert isinstance(depth, dict)

@pytest.mark.asyncio
async def test_get_klines_returns_list(public_client: Public):
    start_time = 1715692417
    end_time = 1715778817
    klines = await public_client.get_klines("BTC_USDC", "1d", start_time, end_time)
    assert isinstance(klines, list)

@pytest.mark.asyncio
async def test_get_status_returns_dict(public_client: Public):
    status = await public_client.get_status()
    assert isinstance(status, dict)
    assert status["status"] == "Ok"

@pytest.mark.asyncio
async def test_get_ping_returns_pong(public_client: Public):
    pong = await public_client.get_ping()
    assert pong == "pong"

@pytest.mark.asyncio
async def test_get_time_returns_int(public_client: Public):
    time = await public_client.get_time()
    if isinstance(time, str):
        assert time.isdigit()
    else:
        assert isinstance(time, int)

@pytest.mark.asyncio
async def test_get_recent_trades_returns_list(public_client: Public):
    recent_trades = await public_client.get_recent_trades("SOL_USDC")
    assert isinstance(recent_trades, list)

@pytest.mark.asyncio
async def test_get_history_trades_returns_list(public_client: Public):
    history_trades = await public_client.get_history_trades("WEN_USDC")
    assert isinstance(history_trades, list)
