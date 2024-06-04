import asyncio
from bpx.async_.public import Public


async def pubblic_example():
    public = Public(proxy="")

    assets = await public.get_assets()
    print("Assets:", assets)
    await asyncio.sleep(1)

    markets = await public.get_markets()
    print("Markets:", markets)
    await asyncio.sleep(1)

    ticker = await public.get_ticker("SOL_USDC")
    print("Ticker for SOL_USDC:", ticker)
    await asyncio.sleep(1)

    depth = await public.get_depth("SOL_USDC")
    print("Depth for SOL_USDC:", depth)
    await asyncio.sleep(1)

    klines = await public.get_klines("SOL_USDC", "1m", 1609459200, 1609545600)
    print("K-lines for SOL_USDC:", klines)
    await asyncio.sleep(1)

    status = await public.get_status()
    print("System Status:", status)
    await asyncio.sleep(1)

    ping = await public.get_ping()
    print("Ping:", ping)
    await asyncio.sleep(1)

    time = await public.get_time()
    print("Server Time:", time)
    await asyncio.sleep(1)

    recent_trades = await public.get_recent_trades("SOL_USDC")
    print("Recent Trades for SOL_USDC:", recent_trades)
    await asyncio.sleep(1)

    history_trades = await public.get_history_trades("SOL_USDC", 100, 0)
    print("History Trades for SOL_USDC:", history_trades)
    await asyncio.sleep(1)

asyncio.run(pubblic_example())
