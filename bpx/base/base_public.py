from bpx.exceptions import *
from bpx.enums import *


class BasePublic:
    BASE_URL = 'https://api.backpack.exchange/'

    def _endpoint(self, path):
        return f"{self.BASE_URL}{path}"

    def get_assets_url(self):
        return self._endpoint('api/v1/assets')

    def get_markets_url(self):
        return self._endpoint('api/v1/markets')

    def get_ticker_url(self, symbol):
        return self._endpoint(f'api/v1/ticker?symbol={symbol}')

    def get_depth_url(self, symbol):
        return self._endpoint(f'api/v1/depth?symbol={symbol}')

    def get_klines_url(self, symbol, interval, start_time, end_time):
        if start_time < 0 or end_time < 0:
            raise NegativeValueError
        if not TimeInterval.has_value(interval):
            raise InvalidTimeIntervalError(interval)
        url = f'api/v1/klines?symbol={symbol}&interval={interval}'
        if start_time:
            url += f'&startTime={start_time}'
        if end_time:
            url += f'&endTime={end_time}'
        return self._endpoint(url)

    def get_status_url(self):
        return self._endpoint('api/v1/status')

    def get_ping_url(self):
        return self._endpoint('api/v1/ping')

    def get_time_url(self):
        return self._endpoint('api/v1/time')

    def get_recent_trades_url(self, symbol, limit=100):
        if limit < 0 or limit > 1000:
            raise LimitValueError
        return self._endpoint(f'api/v1/trades?symbol={symbol}&limit={limit}')

    def get_history_trades_url(self, symbol, limit=100, offset=0):
        if limit < 0 or limit > 1000:
            raise LimitValueError
        if offset < 0:
            raise NegativeValueError
        return self._endpoint(f'api/v1/trades/history?symbol={symbol}&limit={limit}&offset={offset}')
