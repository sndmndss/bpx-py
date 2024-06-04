from bpx.public import Public


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

    klines_timestamp = 1715692417
    klines = public.get_klines("SOL_USDC", "1m", klines_timestamp)
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
