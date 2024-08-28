from bpx.public import Public
from datetime import datetime, timedelta


def public_example():
    public = Public()

    assets = public.get_assets()
    print("Assets:", assets)

    markets = public.get_markets()
    print("Markets:", markets)

    ticker = public.get_ticker("SOL_USDC")
    print("Ticker for SOL_USDC:", ticker)

    depth = public.get_depth("SOL_USDC")
    print("Depth for SOL_USDC:", depth)

    now = datetime.now()
    time_1_minute_ago = now - timedelta(minutes=1)
    timestamp_1_minute_ago = int(time_1_minute_ago.timestamp())
    time_11_minutes_ago = now - timedelta(minutes=11)
    timestamp_11_minutes_ago = int(time_11_minutes_ago.timestamp())
    klines = public.get_klines("SOL_USDC", "1m", timestamp_11_minutes_ago, timestamp_1_minute_ago)
    print("K-lines for SOL_USDC:", klines)

    status = public.get_status()
    print("System Status:", status)

    ping = public.get_ping()
    print("Ping:", ping)

    time = public.get_time()
    print("Server Time:", time)

    recent_trades = public.get_recent_trades("SOL_USDC")
    print("Recent Trades for SOL_USDC:", recent_trades)

    history_trades = public.get_history_trades("SOL_USDC", 100, 0)
    print("History Trades for SOL_USDC:", history_trades)


public_example()
