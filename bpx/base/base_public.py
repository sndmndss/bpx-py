from bpx.exceptions import *
from bpx.constants.enums import *


class BasePublic:
    BASE_URL = "https://api.backpack.exchange/"

    def _endpoint(self, path) -> str:
        return f"{self.BASE_URL}{path}"

    def get_assets_url(self) -> str:
        """
        Returns URL for getting assets

        https://docs.backpack.exchange/#tag/Markets/operation/get_assets
        """
        return self._endpoint("api/v1/assets")

    def get_markets_url(self) -> str:
        """
        Returns URL for getting markets

        https://docs.backpack.exchange/#tag/Markets/operation/get_markets
        """
        return self._endpoint("api/v1/markets")

    def get_ticker_url(self, symbol) -> str:
        """
        Returns URL for getting ticker information for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_ticker
        """
        return self._endpoint(f"api/v1/ticker?symbol={symbol}")

    def get_depth_url(self, symbol) -> str:
        """
        Returns URL for getting depth for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_depth
        """
        return self._endpoint(f"api/v1/depth?symbol={symbol}")
    # currently not available
    # def get_collateral_summaries_for_all_assets(self):
    #     """
    #     Returns URL for getting collateral metadata for all asset.
    #
    #     https://docs.backpack.exchange/#tag/Markets/operation/get_all_collaterals
    #     """
    #     return self._endpoint(f"api/v1/collaterals")
    #
    # def get_collateral_summary(self, asset: str):
    #     """
    #     Returns URL for getting collateral metadata for a specified asset
    #
    #     https://docs.backpack.exchange/#tag/Markets/operation/get_collateral
    #     """
    #     url = f"api/v1/collateral?asset={asset}"
    #     return self._endpoint(url)

    def get_klines_url(self, symbol, interval, start_time, end_time) -> str:
        """
        Returns URL for getting klines for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_klines
        """
        if start_time < 0 or end_time < 0:
            raise NegativeValueError("start_time and end_time")
        if not TimeInterval.has_value(interval):
            raise InvalidTimeIntervalError(interval)
        url = f"api/v1/klines?symbol={symbol}&interval={interval}"
        if start_time:
            url += f"&startTime={start_time}"
        if end_time:
            url += f"&endTime={end_time}"
        return self._endpoint(url)

    def get_status_url(self) -> str:
        """
        Returns URL for getting status information

        https://docs.backpack.exchange/#tag/Markets/operation/get_status
        """
        return self._endpoint("api/v1/status")

    def get_ping_url(self) -> str:
        """
        Returns URL for getting pong if endpoint is reachable

        https://docs.backpack.exchange/#tag/System/operation/ping
        """
        return self._endpoint("api/v1/ping")

    def get_time_url(self) -> str:
        """
        Returns URL for getting current server time

        https://docs.backpack.exchange/#tag/System/operation/get_time
        """
        return self._endpoint("api/v1/time")

    def get_recent_trades_url(self, symbol, limit=100) -> str:
        """
        Returns URL for getting recent trades for a specified market

        https://docs.backpack.exchange/#tag/Trades
        """
        if limit < 0 or limit > 1000:
            raise LimitValueError
        return self._endpoint(f"api/v1/trades?symbol={symbol}&limit={limit}")

    def get_history_trades_url(self, symbol, limit=100, offset=0) -> str:
        """
        Returns URL for getting historical trades for a specified market

        https://docs.backpack.exchange/#tag/Trades/operation/get_historical_trades
        """
        if limit < 0 or limit > 1000:
            raise LimitValueError
        if offset < 0:
            raise NegativeValueError
        return self._endpoint(
            f"api/v1/trades/history?symbol={symbol}&limit={limit}&offset={offset}"
        )
