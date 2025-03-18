from bpx.base.base_public import BasePublic
from bpx.http_client.async_http_client import AsyncHttpClient
from typing import Optional, Union, Dict, Any, List

from bpx.constants.enums import (
    TimeIntervalEnum,
    TimeIntervalType,
    BorrowLendMarketHistoryIntervalEnum,
    BorrowLendMarketHistoryIntervalType,
)

default_http_client = AsyncHttpClient()


class Public(BasePublic):

    def __init__(
        self,
        proxy: Optional[str] = None,
        http_client: AsyncHttpClient = default_http_client,
    ):
        self.http_client = http_client
        self.http_client.proxy = proxy

    async def get_assets(self) -> Union[Dict[str, Any], List[Any], str]:
        """
        Returns all assets

        https://docs.backpack.exchange/#tag/Markets/operation/get_assets
        """
        return await self.http_client.get(self.get_assets_url())

    async def get_collateral(self) -> Union[Dict[str, Any], List[Any], str]:
        return await self.http_client.get(self.get_collateral_url())

    async def get_borrow_lend_markets(self) -> Union[Dict[str, Any], List[Any], str]:
        """
        Returns all borrow lend markets

        https://docs.backpack.exchange/#tag/Borrow-Lend-Markets/operation/get_borrow_lend_markets
        """
        return await self.http_client.get(self.get_borrow_lend_markets_url())

    async def get_borrow_lend_market_history(
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
        return await self.http_client.get(
            self.get_borrow_lend_market_history_url(interval, symbol)
        )

    async def get_markets(self) -> Union[Dict[str, Any], List[Any], str]:
        """
        Returns all markets

        https://docs.backpack.exchange/#tag/Markets/operation/get_markets
        """
        return await self.http_client.get(self.get_markets_url())

    async def get_ticker(self, symbol: str) -> Union[Dict[str, Any], List[Any], str]:
        """
        Returns ticker information for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_ticker
        """
        return await self.http_client.get(self.get_ticker_url(symbol))

    async def get_tickers(self) -> Union[Dict[str, Any], List[Any], str]:
        """
        Returns ticker information for all markets

        https://docs.backpack.exchange/#tag/Markets/operation/get_tickers
        """
        return await self.http_client.get(self.get_tickers_url())

    async def get_depth(self, symbol: str) -> Union[Dict[str, Any], List[Any], str]:
        """
        Returns depth for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_depth
        """
        return await self.http_client.get(self.get_depth_url(symbol))

    async def get_klines(
        self,
        symbol: str,
        interval: Union[TimeIntervalType, TimeIntervalEnum],
        start_time: int,
        end_time: Optional[int] = None,
    ) -> Union[Dict[str, Any], List[Any], str]:
        """
        Returns klines for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_klines
        """
        return await self.http_client.get(
            self.get_klines_url(symbol, interval, start_time, end_time)
        )

    async def get_open_interest(
        self, symbol: str
    ) -> Union[Dict[str, Any], List[Any], str]:
        """
        Returns open interest for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_open_interest
        """
        return await self.http_client.get(self.get_open_interest_url(symbol))

    async def get_funding_interval_rates(
        self, symbol: str, limit: int = 100, offset: int = 0
    ) -> Union[Dict[str, Any], List[Any], str]:
        """
        Returns funding interval rates for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_funding_interval_rates
        """
        return await self.http_client.get(
            self.get_funding_interval_rates_url(symbol, limit, offset)
        )

    async def get_status(self) -> str:
        """
        Returns status information

        https://docs.backpack.exchange/#tag/Markets/operation/get_status
        """
        return await self.http_client.get(self.get_status_url())

    async def get_ping(self) -> str:
        """
        Returns pong if endpoint is reachable

        https://docs.backpack.exchange/#tag/System/operation/ping
        """
        return await self.http_client.get(self.get_ping_url())

    async def get_time(self) -> str:
        """
        Returns current server time

        https://docs.backpack.exchange/#tag/System/operation/get_time
        """
        return await self.http_client.get(self.get_time_url())

    async def get_recent_trades(
        self, symbol: str, limit=100
    ) -> Union[Dict[str, Any], List[Any], str]:
        """
        Returns recent trades for a specified market

        https://docs.backpack.exchange/#tag/Trades
        """
        return await self.http_client.get(self.get_recent_trades_url(symbol, limit))

    async def get_history_trades(
        self, symbol: str, limit=100, offset=0
    ) -> Union[Dict[str, Any], List[Any], str]:
        """
        Returns historical trades for a specified market

        https://docs.backpack.exchange/#tag/Trades/operation/get_historical_trades
        """
        return await self.http_client.get(
            self.get_historical_trades_url(symbol, limit, offset)
        )

    async def get_all_mark_prices(
        self,
        symbol: Optional[str] = None,
    ) -> Union[Dict[str, Any], List[Any], str]:
        """
        Retrieves mark price, index price and the funding rate for the current interval for all symbols, or the symbol specified.

        https://docs.backpack.exchange/#tag/Markets/operation/get_mark_prices
        """
        return await self.http_client.get(self.get_all_mark_prices_url(symbol))
