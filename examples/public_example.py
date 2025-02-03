from bpx.public import Public
from bpx.constants.enums import TimeIntervalEnum
from bpx.constants.enums import BorrowLendMarketHistoryIntervalEnum
import time


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

    now_ts = int(time.time())
    ts_1_minute_ago = now_ts - 60
    ts_11_minutes_ago = now_ts - 660

    klines = public.get_klines(
        "SOL_USDC",
        interval=TimeIntervalEnum.ONE_MINUTE,
        start_time=ts_11_minutes_ago,
        end_time=ts_1_minute_ago,
    )
    print("K-lines for SOL_USDC:", klines)

    status = public.get_status()
    print("System Status:", status)

    ping = public.get_ping()
    print("Ping:", ping)

    time_ = public.get_time()
    print("Server Time:", time_)

    recent_trades = public.get_recent_trades("SOL_USDC")
    print("Recent Trades for SOL_USDC:", recent_trades)

    history_trades = public.get_history_trades("SOL_USDC", 100, 0)
    print("History Trades for SOL_USDC:", history_trades)

    collateral_info = public.get_collateral()
    print("Collateral Info:", collateral_info)

    borrow_lend_markets = public.get_borrow_lend_markets()
    print("Borrow Lend Markets:", borrow_lend_markets)

    borrow_lend_history = public.get_borrow_lend_market_history(
        BorrowLendMarketHistoryIntervalEnum.ONE_WEEK, symbol="ETH"
    )
    print("Borrow Lend Market History (1w) for ETH:", borrow_lend_history)

    market_data = public.get_market()
    print("Market data from get_market():", market_data)

    all_tickers = public.get_tickers("SOL_USDC")
    print("Tickers:", all_tickers)

    open_interest = public.get_open_interest("ETH_USDC_PERP")
    print("Open Interest for ETH_USDC:", open_interest)

    funding_rates = public.get_funding_interval_rates("SOL_USDC_PERP", limit=1000, offset=0)
    print("Funding Interval Rates for SOL_USDC:", funding_rates)


if __name__ == "__main__":
    public_example()
