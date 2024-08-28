from bpx.base.base_public import BasePublic
from bpx.http_client.sync_http_client import SyncHttpClient
from typing import Optional

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

    def get_depth(self, symbol: str):
        """
        Returns depth for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_depth
        """
        return self.http_client.get(self.get_depth_url(symbol))

    def get_klines(
        self, symbol: str, interval: str, start_time: int, end_time: int = 0
    ):
        """
        Returns klines for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_klines
        """
        return self.http_client.get(
            self.get_klines_url(symbol, interval, start_time, end_time)
        )

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
        return self.http_client.get(self.get_history_trades_url(symbol, limit, offset))
