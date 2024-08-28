from bpx.base.base_public import BasePublic
from bpx.http_client.async_http_client import AsyncHttpClient
from typing import Optional

default_http_client = AsyncHttpClient()


class Public(BasePublic):

    def __init__(
        self,
        proxy: Optional[str] = None,
        http_client: AsyncHttpClient = default_http_client,
    ):
        self.http_client = http_client
        self.http_client.proxy = proxy

    async def get_assets(self):
        """
        Returns all assets

        https://docs.backpack.exchange/#tag/Markets/operation/get_assets
        """
        return await self.http_client.get(self.get_assets_url())

    async def get_markets(self):
        """
        Returns all markets

        https://docs.backpack.exchange/#tag/Markets/operation/get_markets
        """
        return await self.http_client.get(self.get_markets_url())

    async def get_ticker(self, symbol: str):
        """
        Returns ticker information for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_ticker
        """
        return await self.http_client.get(self.get_ticker_url(symbol))

    async def get_depth(self, symbol: str):
        """
        Returns depth for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_depth
        """
        return await self.http_client.get(self.get_depth_url(symbol))

    async def get_klines(self, symbol: str, interval: str, start_time: int, end_time=0):
        """
        Returns klines for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_klines
        """
        return await self.http_client.get(
            self.get_klines_url(symbol, interval, start_time, end_time)
        )

    async def get_status(self):
        """
        Returns status information

        https://docs.backpack.exchange/#tag/Markets/operation/get_status
        """
        return await self.http_client.get(self.get_status_url())

    async def get_ping(self):
        """
        Returns pong if endpoint is reachable

        https://docs.backpack.exchange/#tag/System/operation/ping
        """
        return await self.http_client.get(self.get_ping_url())

    async def get_time(self):
        """
        Returns current server time

        https://docs.backpack.exchange/#tag/System/operation/get_time
        """
        return await self.http_client.get(self.get_time_url())

    async def get_recent_trades(self, symbol: str, limit=100):
        """
        Returns recent trades for a specified market

        https://docs.backpack.exchange/#tag/Trades
        """
        return await self.http_client.get(self.get_recent_trades_url(symbol, limit))

    async def get_history_trades(self, symbol: str, limit=100, offset=0):
        """
        Returns historical trades for a specified market

        https://docs.backpack.exchange/#tag/Trades/operation/get_historical_trades
        """
        return await self.http_client.get(
            self.get_history_trades_url(symbol, limit, offset)
        )
