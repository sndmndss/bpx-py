from bpx.base.base_public import BasePublic
from bpx.http_client.sync_http_client import SyncHttpClient
from bpx.models.objects import (
    MMFFunction,
    IMFFunction,
    HaircutFunction,
)
from bpx.constants.enums import (
    TimeIntervalType,
    TimeIntervalEnum,
    BorrowLendMarketHistoryIntervalType,
    BorrowLendMarketHistoryIntervalEnum,
)
from typing import Optional, Union

default_http_client = SyncHttpClient()


class Public(BasePublic):

    def __init__(
        self,
        proxy: Optional[dict] = None,
        http_client: SyncHttpClient = default_http_client,
    ):
        self.http_client = http_client
        self.http_client.proxies = proxy

    def get_assets(self):
        """
        Returns all assets

        https://docs.backpack.exchange/#tag/Markets/operation/get_assets
        """
        return self.http_client.get(self.get_assets_url())

    def get_collateral(self) -> Union[str, IMFFunction, MMFFunction, HaircutFunction]:
        return self.http_client.get(self.get_collateral_url())

    def get_borrow_lend_markets(self):
        """
        Returns all borrow lend markets

        https://docs.backpack.exchange/#tag/Borrow-Lend-Markets/operation/get_borrow_lend_markets
        """
        return self.http_client.get(self.get_borrow_lend_markets_url())

    def get_borrow_lend_market_history(
        self,
        interval: Union[
            BorrowLendMarketHistoryIntervalEnum, BorrowLendMarketHistoryIntervalType
        ],
        symbol: Optional[str] = None,
    ):
        """
        Returns borrow lend market history

        https://docs.backpack.exchange/#tag/Borrow-Lend-Markets/operation/get_borrow_lend_markets_history
        """
        return self.http_client.get(
            self.get_borrow_lend_market_history_url(interval, symbol)
        )

    def get_market(self):
        """
        Returns all markets

        https://docs.backpack.exchange/#tag/Markets/operation/get_markets
        """
        return self.http_client.get(self.get_markets_url())

    def get_markets(self):
        """
        Returns all markets

        https://docs.backpack.exchange/#tag/Markets/operation/get_markets
        """
        return self.http_client.get(self.get_markets_url())

    def get_ticker(self, symbol: str):
        """
        Returns ticker information for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_ticker
        """
        return self.http_client.get(self.get_ticker_url(symbol))

    def get_tickers(self):
        """
        Returns ticker information for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_tickers
        """
        return self.http_client.get(self.get_tickers_url())

    def get_depth(self, symbol: str):
        """
        Returns depth for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_depth
        """
        return self.http_client.get(self.get_depth_url(symbol))

    def get_klines(
        self,
        symbol: str,
        interval: Union[TimeIntervalType, TimeIntervalEnum],
        start_time: int,
        end_time: int = 0,
    ):
        """
        Returns klines for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_klines
        """
        return self.http_client.get(
            self.get_klines_url(
                symbol=symbol,
                interval=interval,
                start_time=start_time,
                end_time=end_time,
            )
        )

    def get_open_interest(self, symbol: str):
        """
        Returns open interest for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_open_interest
        """
        return self.http_client.get(self.get_open_interest_url(symbol))

    def get_funding_interval_rates(
        self, symbol: str, limit: int = 100, offset: int = 0
    ):
        """
        Returns funding interval rates for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_funding_interval_rates
        """
        return self.http_client.get(self.get_funding_interval_rates_url(symbol, limit, offset))

    def get_status(self):
        """
        Returns status information

        https://docs.backpack.exchange/#tag/Markets/operation/get_status
        """
        return self.http_client.get(self.get_status_url())

    def get_ping(self):
        """
        Returns pong if endpoint is reachable

        https://docs.backpack.exchange/#tag/System/operation/ping
        """
        return self.http_client.get(self.get_ping_url())

    def get_time(self):
        """
        Returns current server time

        https://docs.backpack.exchange/#tag/System/operation/get_time
        """
        return self.http_client.get(self.get_time_url())

    def get_recent_trades(self, symbol: str, limit=100):
        """
        Returns recent trades for a specified market

        https://docs.backpack.exchange/#tag/Trades
        """
        return self.http_client.get(self.get_recent_trades_url(symbol, limit))

    def get_history_trades(self, symbol: str, limit=100, offset=0):
        """
        Returns historical trades for a specified market

        https://docs.backpack.exchange/#tag/Trades/operation/get_historical_trades
        """
        return self.http_client.get(
            self.get_historical_trades_url(symbol, limit, offset)
        )
