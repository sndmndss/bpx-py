from bpx.exceptions import *
from bpx.constants.enums import *
from bpx.constants.enums import (
    BorrowLendMarketHistoryIntervalEnum,
    BorrowLendMarketHistoryIntervalType,
)
from typing import Union, Optional


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

    def get_collateral_url(self) -> str:
        """ "
        Returns URL for getting collateral
        https://docs.backpack.exchange/#tag/Assets/operation/get_collateral_parameters
        """
        return self._endpoint(f"api/v1/collateral")

    def get_borrow_lend_markets_url(self) -> str:
        """
        Returns URL for getting borrow lend markets

        https://docs.backpack.exchange/#tag/Borrow-Lend-Markets/operation/get_borrow_lend_markets
        """
        return self._endpoint("api/v1/borrowLend/markets")

    def get_borrow_lend_market_history_url(
        self,
        interval: Union[
            BorrowLendMarketHistoryIntervalEnum, BorrowLendMarketHistoryIntervalType
        ],
        symbol: Optional[str] = None,
    ) -> str:
        """
                Returns URL for getting borrow lend market history

        https://docs.backpack.exchange/#tag/Borrow-Lend-Markets/operation/get_borrow_lend_markets_history
        """
        url = f"api/v1/borrowLend/markets/history?interval={interval}"
        if symbol:
            url += f"&symbol={symbol}"
        return self._endpoint(url)

    def get_markets_url(self) -> str:
        """
        Returns URL for getting markets

        https://docs.backpack.exchange/#tag/Markets/operation/get_markets
        """
        return self._endpoint("api/v1/markets")

    def get_market_url(self, symbol: str) -> str:
        """
        Returns URL for getting information about a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_market
        """
        return self._endpoint(f"api/v1/markets/{symbol}")

    def get_ticker_url(self, symbol: str) -> str:
        """
        Returns URL for getting ticker information for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_ticker
        """
        return self._endpoint(f"api/v1/ticker?symbol={symbol}")

    def get_tickers_url(self) -> str:
        """
        Returns URL for getting ticker information for all markets

        https://docs.backpack.exchange/#tag/Markets/operation/get_tickers
        """
        return self._endpoint("api/v1/tickers")

    def get_depth_url(self, symbol) -> str:
        """
        Returns URL for getting depth for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_depth
        """
        return self._endpoint(f"api/v1/depth?symbol={symbol}")

    def get_klines_url(
        self,
        symbol: str,
        interval: Union[TimeIntervalEnum, TimeIntervalType],
        start_time: int,
        end_time: Optional[int] = None,
    ) -> str:
        """
        Returns URL for getting klines for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_klines
        """
        if start_time < 0:
            raise NegativeValueError("start_time")
        if not TimeIntervalEnum.has_value(interval):
            raise InvalidTimeIntervalError(interval)
        url = (
            f"api/v1/klines?symbol={symbol}&interval={interval}&startTime={start_time}"
        )
        if end_time:
            url += f"&endTime={end_time}"
        return self._endpoint(url)

    def get_all_mark_prices_url(self, symbol: Optional[str] = None) -> str:
        """
        Returns URL for getting all market prices

        https://docs.backpack.exchange/#tag/Markets/operation/get_mark_prices
        """
        if symbol:
            return self._endpoint(f"api/v1/markPrices?symbol={symbol}")
        return self._endpoint("api/v1/markPrices")

    def get_open_interest_url(self, symbol: str) -> str:
        """
        Returns URL for getting open interest for a specified market

        https://docs.backpack.exchange/#tag/Markets/operation/get_open_interest
        """
        return self._endpoint(f"api/v1/openInterest?symbol={symbol}")

    def get_funding_interval_rates_url(
        self, symbol: str, limit: int = 1000, offset: int = 0
    ) -> str:
        """
        Returns URL for getting funding rates for a specified market

        https://docs.backpack.exchange/#tag/Funding-Rates/operation/get_funding_rates
        """
        if limit < 0 or limit > 1000:
            raise LimitValueError
        if offset < 0:
            raise NegativeValueError(f"offset = {offset}")
        return self._endpoint(f"api/v1/fundingRates?symbol={symbol}&limit={limit}")

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

    def get_recent_trades_url(self, symbol: str, limit: int = 100) -> str:
        """
        Returns URL for getting recent trades for a specified market

        https://docs.backpack.exchange/#tag/Trades
        """
        if limit < 0 or limit > 1000:
            raise LimitValueError
        return self._endpoint(f"api/v1/trades?symbol={symbol}&limit={limit}")

    def get_historical_trades_url(
        self, symbol: str, limit: int = 100, offset: int = 0
    ) -> str:
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
