from bpx.base.base_public import BasePublic
from bpx.http_client.sync_http_client import SyncHttpClient


class Public(BasePublic, SyncHttpClient):

    def __init__(self, proxy: dict = None):
        SyncHttpClient.__init__(self, proxies=proxy)

    def get_assets(self):
        return self.get(self.get_assets_url())

    def get_markets(self):
        return self.get(self.get_markets_url())

    def get_ticker(self, symbol: str):
        return self.get(self.get_ticker_url(symbol))

    def get_depth(self, symbol: str):
        return self.get(self.get_depth_url(symbol))

    def get_klines(self, symbol: str, interval: str, start_time=0, end_time=0):
        return self.get(self.get_klines_url(symbol, interval, start_time, end_time))

    def get_status(self):
        return self.get(self.get_status_url())

    def get_ping(self):
        return self.get(self.get_ping_url())

    def get_time(self):
        return self.get(self.get_time_url())

    def get_recent_trades(self, symbol: str, limit=100):
        return self.get(self.get_recent_trades_url(symbol, limit))

    def get_history_trades(self, symbol: str, limit=100, offset=0):
        return self.get(self.get_history_trades_url(symbol, limit, offset))
