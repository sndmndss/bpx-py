from cryptography.hazmat.primitives.asymmetric import ed25519
import base64
from typing import Optional, Union
from bpx.models.objects import RequestConfiguration
from time import time
from bpx.exceptions import *
from bpx.constants.enums import *


class BaseAccount:
    """
    Contains functions returning parameters for querying different endpoints:
    url, headers and request parameters
    """

    BPX_API_URL = "https://api.backpack.exchange/"

    def __init__(self, public_key: str, secret_key: str, window: int, debug: bool):

        self.private_key = ed25519.Ed25519PrivateKey.from_private_bytes(
            base64.b64decode(secret_key)
        )
        self.public_key = public_key
        self.window = window
        self.debug = debug

    def get_account(self, window: Optional[int] = None) -> RequestConfiguration:
        """
        Returns the url, headers for getting account information

        https://docs.backpack.exchange/#tag/Account/operation/get_account
        """
        headers = self._headers({}, "accountQuery", window=window)
        url = self.BPX_API_URL + "api/v1/account"
        request_config = RequestConfiguration(url=url, headers=headers)
        return request_config

    def update_account(
        self,
        auto_borrow_settlements: Optional[bool] = None,
        auto_lend: Optional[bool] = None,
        auto_realize_pnl: Optional[bool] = None,
        auto_repay_borrows: Optional[bool] = None,
        leverage_limit: Optional[str] = None,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for updating account settings

        https://docs.backpack.exchange/#tag/Account/operation/update_account_settings
        """
        params = {}
        if auto_borrow_settlements:
            params["autoBorrowSettlements"] = auto_borrow_settlements
        if auto_lend:
            params["autoLend"] = auto_lend
        if auto_realize_pnl:
            params["autoRealizePnl"] = auto_realize_pnl
        if auto_repay_borrows:
            params["autoRepayBorrows"] = auto_repay_borrows
        if leverage_limit:
            params["leverageLimit"] = leverage_limit
        headers = self._headers(params, "accountUpdate", window=window)
        url = self.BPX_API_URL + "api/v1/account"
        request_config = RequestConfiguration(url=url, headers=headers, data=params)
        return request_config

    def get_borrow_lend_positions(
        self, window: Optional[int] = None
    ) -> RequestConfiguration:
        """
        Returns the url, headers for getting borrow lend positions

        https://docs.backpack.exchange/#tag/Borrow-Lend/operation/get_borrow_lend_positions
        """
        headers = self._headers({}, "borrowLendPositionQuery", window=window)
        url = self.BPX_API_URL + "api/v1/borrowLend/positions"
        request_config = RequestConfiguration(url=url, headers=headers)
        return request_config

    def execute_borrow_lend(
        self,
        quantity: str,
        side: Union[BorrowLendSideType, BorrowLendSideEnum],
        symbol: str,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for borrowing or lending funds

        https://docs.backpack.exchange/#tag/Borrow-Lend/operation/execute_borrow_lend
        """
        params = {
            "quantity": quantity,
            "side": side,
            "symbol": symbol,
        }
        headers = self._headers(params, "borrowLendExecute", window=window)
        url = self.BPX_API_URL + "api/v1/borrowLend"
        request_config = RequestConfiguration(url=url, headers=headers, data=params)
        return request_config

    def get_balances(self, window: Optional[int] = None) -> RequestConfiguration:
        """
        Returns the url, headers for getting account balances

        https://docs.backpack.exchange/#tag/Capital/operation/get_balances
        """
        headers = self._headers({}, "balanceQuery", window=window)
        url = self.BPX_API_URL + "api/v1/capital"
        request_config = RequestConfiguration(url=url, headers=headers)
        return request_config

    def get_collateral(
        self, subaccount_id: Optional[int] = None, window: Optional[int] = None
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for getting collateral

        https://docs.backpack.exchange/#tag/Capital/operation/get_collateral
        """
        params = {}
        if subaccount_id:
            params["subaccountId"] = subaccount_id
        headers = self._headers(params, "collateralQuery", window=window)
        url = self.BPX_API_URL + "api/v1/capital/collateral"
        request_config = RequestConfiguration(url=url, headers=headers, params=params)
        return request_config

    def get_deposits(
        self,
        limit: int,
        offset: int,
        from_: Optional[int] = None,
        to: Optional[int] = None,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for getting account deposits

        https://docs.backpack.exchange/#tag/Capital/operation/get_deposits
        """
        params = {}
        if limit > 1000 or limit < 0:
            raise LimitValueError
        params["limit"] = limit
        if offset < 0:
            raise NegativeValueError(offset)
        params["offset"] = offset
        if from_:
            params["from"] = from_
        if to:
            params["to"] = to
        headers = self._headers(params, "depositQueryAll", window=window)
        url = self.BPX_API_URL + "wapi/v1/capital/deposits"
        request_config = RequestConfiguration(url=url, headers=headers, params=params)
        return request_config

    def get_deposit_address(
        self, blockchain: str, window: Optional[int] = None
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for getting a deposit address

        https://docs.backpack.exchange/#tag/Capital/operation/get_deposit_address
        """
        params = {"blockchain": blockchain}
        headers = self._headers(params, "depositAddressQuery", window=window)
        url = self.BPX_API_URL + "wapi/v1/capital/deposit/address"
        request_config = RequestConfiguration(url=url, headers=headers, params=params)
        return request_config

    def get_withdrawals(
        self,
        limit: int,
        offset: int,
        from_: Optional[int] = None,
        to: Optional[int] = None,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for getting account withdrawals

        https://docs.backpack.exchange/#tag/Capital/operation/get_withdrawals
        """
        params = {}
        if limit > 1000 or limit < 0:
            raise LimitValueError
        params["limit"] = limit
        if offset < 0:
            raise NegativeValueError(offset)
        params["offset"] = offset
        if from_:
            params["from"] = from_
        if to:
            params["to"] = to
        headers = self._headers(params, "withdrawalQueryAll", window=window)
        url = self.BPX_API_URL + "wapi/v1/capital/withdrawals"
        request_config = RequestConfiguration(url=url, headers=headers, params=params)
        return request_config

    def withdrawal(
        self,
        address: str,
        blockchain: str,
        quantity: str,
        symbol: str,
        two_factor_token: Optional[str] = None,
        auto_borrow: Optional[bool] = None,
        auto_lend_redeem: Optional[bool] = None,
        client_id: Optional[int] = None,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for withdrawing funds

        https://docs.backpack.exchange/#tag/Capital/operation/request_withdrawal
        """
        params = {
            "address": address,
            "blockchain": blockchain,
            "quantity": quantity,
            "symbol": symbol,
        }
        if two_factor_token:
            params["twoFactorToken"] = two_factor_token
        if auto_borrow:
            params["autoBorrow"] = auto_borrow
        if auto_lend_redeem:
            params["autoLendRedeem"] = auto_lend_redeem
        if client_id:
            params["clientId"] = client_id
        headers = self._headers(params, "withdraw", window=window)
        url = self.BPX_API_URL + "wapi/v1/capital/withdrawals"
        request_config = RequestConfiguration(url=url, headers=headers, data=params)
        return request_config

    def get_open_positions(self, window: Optional[int] = None) -> RequestConfiguration:
        """
        Returns the url, headers for getting open positions

        https://docs.backpack.exchange/#tag/Futures/operation/get_positions
        """
        headers = self._headers({}, "positionQuery", window=window)
        url = self.BPX_API_URL + "api/v1/position"
        request_config = RequestConfiguration(url=url, headers=headers)
        return request_config

    def get_borrow_history(
        self,
        borrow_lend_event_type: Optional[
            Union[BorrowLendEventEnum, BorrowLendEventType]
        ] = None,
        sources: Optional[str] = None,
        position_id: Optional[str] = None,
        symbol: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
                Returns the url, headers and request parameters for getting borrow history

        https://docs.backpack.exchange/#tag/History/operation/get_borrow_lend_history
        """
        if limit > 1000 or limit < 0:
            raise LimitValueError
        if offset < 0:
            raise NegativeValueError(offset)
        params = {"limit": limit, "offset": offset}
        if borrow_lend_event_type:
            params["type"] = borrow_lend_event_type
        if sources:
            params["sources"] = sources
        if position_id:
            params["positionId"] = position_id
        if symbol:
            params["symbol"] = symbol
        headers = self._headers(params, "borrowHistoryQueryAll", window=window)
        url = self.BPX_API_URL + "wapi/v1/history/borrowLend"
        request_config = RequestConfiguration(url=url, headers=headers, params=params)
        return request_config

    def get_interest_history(
        self,
        asset: Optional[str] = None,
        symbol: Optional[str] = None,
        position_id: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        source: Optional[
            Union[InterestPaymentSourceType, InterestPaymentSourceEnum]
        ] = None,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for getting interest history

        https://docs.backpack.exchange/#tag/History/operation/get_interest_history
        """
        if limit > 1000 or limit < 0:
            raise LimitValueError
        if offset < 0:
            raise NegativeValueError(offset)
        params = {"limit": limit, "offset": offset}
        if asset:
            params["asset"] = asset
        if symbol:
            params["symbol"] = symbol
        if position_id:
            params["positionId"] = position_id
        if source:
            params["source"] = source
        headers = self._headers(params, "interestHistoryQueryAll", window=window)
        url = self.BPX_API_URL + "wapi/v1/history/interest"
        request_config = RequestConfiguration(url=url, headers=headers, params=params)
        return request_config

    # def get_borrow_position_history(self, symbol: Optional[str] = None, side: Optional[Union[BorrowLendSideType, BorrowLendSideEnum]] = None, state: Optional[Union[BorrowLendPositionStateType, BorrowLendPositionStateEnum]] = None, limit: int = 100, offset: int = 0, window: Optional[int] = None) -> RequestConfiguration:
    #     """
    #     Returns the url, headers and request parameters for getting borrow lend position history
    #
    #     https://docs.backpack.exchange/#tag/History/operation/get_borrow_lend_position_history
    #     """
    #     if limit > 1000 or limit < 0:
    #         raise LimitValueError
    #     if offset < 0:
    #         raise NegativeValueError(offset)
    #     params = {"limit": limit, "offset": offset}
    #     if symbol:
    #         params["symbol"] = symbol
    #     if side:
    #         params["side"] = side
    #     if state:
    #         params["state"] = state
    #     headers = self._headers(params, "borrowLendPositionHistoryQueryAll", window=window)
    #     url = self.BPX_API_URL + "wapi/v1/history/borrowLend/positions"
    #     request_config = RequestConfiguration(url=url, headers=headers, params=params)
    #     return request_config

    def get_fill_history(
        self,
        symbol: Optional[str] = None,
        limit: Optional[int] = 100,
        offset: Optional[int] = 0,
        from_: Optional[int] = None,
        to: Optional[int] = None,
        fill_type: Optional[Union[FillTypeEnum, FillTypeType]] = None,
        market_type: Optional[Union[MarketTypeType, MarketTypeEnum]] = None,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for getting account fill history

        https://docs.backpack.exchange/#tag/History/operation/get_fills
        """

        if limit > 1000 or limit < 0:
            raise LimitValueError
        if offset < 0:
            raise NegativeValueError(offset)
        params = {
            "limit": limit,
            "offset": offset,
        }
        if from_:
            if from_ < 0:
                raise NegativeValueError(from_)
            else:
                params["from"] = from_
        if to:
            if to < 0:
                raise NegativeValueError(to)
            else:
                params["to"] = to
        if symbol:
            params["symbol"] = symbol
        if fill_type:
            params["fillType"] = fill_type
        if market_type:
            params["marketType"] = market_type
        headers = self._headers(params, "fillHistoryQueryAll", window=window)
        url = self.BPX_API_URL + "wapi/v1/history/fills"
        request_config = RequestConfiguration(url=url, headers=headers, params=params)
        return request_config

    def get_funding_payments(
        self,
        subaccount_id: Optional[int] = None,
        symbol: Optional[str] = None,
        limit: Optional[int] = 100,
        offset: Optional[int] = 0,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for getting funding payments

        https://docs.backpack.exchange/#tag/History/operation/get_funding_payments
        """
        if limit > 1000 or limit < 0:
            raise LimitValueError
        if offset < 0:
            raise NegativeValueError(offset)
        params = {
            "limit": limit,
            "offset": offset,
        }
        if subaccount_id:
            params["subaccountId"] = subaccount_id
        if symbol:
            params["symbol"] = symbol
        headers = self._headers(params, "fundingHistoryQueryAll", window=window)
        url = self.BPX_API_URL + "wapi/v1/history/funding"
        request_config = RequestConfiguration(url=url, headers=headers, params=params)
        return request_config

    def get_order_history(
        self,
        limit: int,
        offset: int,
        order_id: Optional[str] = None,
        symbol: Optional[str] = None,
        market_type: Optional[Union[MarketTypeEnum, MarketTypeType]] = None,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for getting account order history

        https://docs.backpack.exchange/#tag/History/operation/get_order_history
        """
        params = {}
        if limit > 1000 or limit < 0:
            raise LimitValueError
        params["limit"] = limit
        if offset < 0:
            raise NegativeValueError(offset)
        params["offset"] = offset
        if order_id:
            params["orderId"] = order_id
        if symbol:
            params["symbol"] = symbol
        if market_type:
            params["marketType"] = market_type
        headers = self._headers(params, "orderHistoryQueryAll", window=window)
        url = self.BPX_API_URL + "wapi/v1/history/orders"
        request_config = RequestConfiguration(url=url, headers=headers, params=params)
        return request_config

    def get_profit_and_loss_history(
        self,
        subaccount_id: Optional[int] = None,
        symbol: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for getting profit and loss history

        https://docs.backpack.exchange/#tag/History/operation/get_pnl_payments
        """

        if limit > 1000 or limit < 0:
            raise LimitValueError
        if offset < 0:
            raise NegativeValueError(offset)
        params = {"limit": limit, "offset": offset}
        if subaccount_id:
            params["subaccountId"] = subaccount_id
        if symbol:
            params["symbol"] = symbol

        headers = self._headers(params, "pnlHistoryQueryAll", window=window)
        url = self.BPX_API_URL + "wapi/v1/history/pnl"
        request_config = RequestConfiguration(url=url, headers=headers, params=params)
        return request_config

    def get_settlements_history(
        self,
        limit: Optional[int] = 100,
        offset: Optional[int] = 0,
        source: Optional[
            Union[SettlementSourceFilterEnum, SettlementSourceFilterType]
        ] = None,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for getting settlements history

        https://docs.backpack.exchange/#tag/History/operation/get_settlements
        """
        if limit > 1000 or limit < 0:
            raise LimitValueError
        if offset < 0:
            raise NegativeValueError(offset)
        params = {"limit": limit, "offset": offset}
        headers = self._headers(params, "settlementHistoryQueryAll", window=window)
        url = self.BPX_API_URL + "wapi/v1/history/settlement"
        request_config = RequestConfiguration(url=url, headers=headers, params=params)
        return request_config

    def get_open_order(
        self,
        symbol: str,
        order_id: Optional[str] = None,
        client_id: Optional[int] = None,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for getting account open orders

        https://docs.backpack.exchange/#tag/Order/operation/get_open_orders
        """

        params = {"symbol": symbol}
        if order_id:
            params["orderId"] = order_id
        if client_id:
            params["clientId"] = str(client_id)
        headers = self._headers(params, "orderQuery", window=window)
        url = self.BPX_API_URL + "api/v1/order"
        request_config = RequestConfiguration(url=url, headers=headers, params=params)
        return request_config

    def execute_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        time_in_force: Optional[Union[TimeInForceEnum, TimeInForceType]] = None,
        quantity: Optional[str] = None,
        price: Optional[str] = None,
        trigger_price: Optional[str] = None,
        self_trade_prevention: Optional[
            Union[SelfTradePreventionEnum, SelfTradePreventionType]
        ] = "RejectBoth",
        quote_quantity: Optional[str] = None,
        client_id: Optional[int] = None,
        post_only: Optional[bool] = None,
        reduce_only: Optional[bool] = None,
        auto_borrow: Optional[bool] = None,
        auto_borrow_repay: Optional[bool] = None,
        auto_lend: Optional[bool] = None,
        auto_lend_redeem: Optional[bool] = None,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for placing a new order

        https://docs.backpack.exchange/#tag/Order/operation/execute_order
        """
        if not SelfTradePreventionEnum.has_value(self_trade_prevention):
            raise InvalidSelfTradePreventionError(self_trade_prevention)
        params = {
            "symbol": symbol,
            "side": side,
            "orderType": order_type,
            "quantity": quantity,
            "selfTradePrevention": self_trade_prevention,
        }
        if order_type != "Market":
            if price:
                params["price"] = price
        if trigger_price:
            params["triggerPrice"] = trigger_price
        if quote_quantity:
            params["quoteQuantity"] = quote_quantity
        if post_only:
            params["postOnly"] = True
        if TimeInForceEnum.has_value(time_in_force):
            params["timeInForce"] = time_in_force
        else:
            raise InvalidTimeInForceValue(time_in_force)
        if client_id:
            params["clientId"] = client_id
        if reduce_only:
            params["reduceOnly"] = reduce_only
        if auto_borrow:
            params["autoBorrow"] = auto_borrow
        if auto_borrow_repay:
            params["autoBorrowRepay"] = auto_borrow_repay
        if auto_lend:
            params["autoLend"] = auto_lend
        if auto_lend_redeem:
            params["autoLendRedeem"] = auto_lend_redeem
        headers = self._headers(params, "orderExecute", window=window)
        url = self.BPX_API_URL + "api/v1/order"
        request_config = RequestConfiguration(url=url, headers=headers, data=params)
        return request_config

    def cancel_order(
        self,
        symbol: str,
        order_id: Optional[str] = None,
        client_id: Optional[int] = None,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for cancelling an existing order

        https://docs.backpack.exchange/#tag/Order/operation/cancel_order
        """
        params = {"symbol": symbol}
        if order_id:
            params["orderId"] = order_id
        if client_id:
            params["clientId"] = str(client_id)
        headers = self._headers(params, "orderCancel", window=window)
        url = self.BPX_API_URL + "api/v1/order"
        request_config = RequestConfiguration(url=url, headers=headers, data=params)
        return request_config

    def get_open_orders(
        self, symbol: str, window: Optional[int] = None
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for getting account open orders

        https://docs.backpack.exchange/#tag/Order/operation/get_open_orders
        """
        params = {"symbol": symbol}
        headers = self._headers(params, "orderQueryAll", window=window)
        url = self.BPX_API_URL + "api/v1/orders"
        request_config = RequestConfiguration(url=url, headers=headers, params=params)
        return request_config

    def cancel_all_orders(
        self, symbol: str, window: Optional[int] = None
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for cancelling all open orders for a specific symbol

        https://docs.backpack.exchange/#tag/Order/operation/cancel_open_orders
        """
        params = {"symbol": symbol}
        headers = self._headers(params, "orderCancelAll", window=window)
        url = self.BPX_API_URL + "api/v1/orders"
        request_config = RequestConfiguration(url=url, headers=headers, data=params)
        return request_config

    def submit_quote(
        self,
        rfq_id: str,
        bid_price: str,
        ask_price: str,
        client_id: Optional[int] = None,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for submitting a quote

        https://docs.backpack.exchange/#tag/Request-For-Quote/operation/submit_quote
        """
        params = {
            "rfqId": rfq_id,
            "bidPrice": bid_price,
            "askPrice": ask_price,
        }
        if client_id:
            params["clientId"] = client_id
        headers = self._headers(params, "quoteSubmit", window=window)
        url = self.BPX_API_URL + "api/v1/rfq/quote"
        request_config = RequestConfiguration(url=url, headers=headers, data=params)
        return request_config

    def _headers(self, params: dict, instruction: str, window: Optional[int]) -> dict:
        """
        Returns headers for the given instruction and params
        """
        window = self.window if window is None else window
        timestamp = int(time() * 1e3)
        encoded_signature = self._sign(params, instruction, timestamp, window)
        headers = {
            "X-API-Key": self.public_key,
            "X-Signature": encoded_signature,
            "X-Timestamp": str(timestamp),
            "X-Window": str(window),
            "Content-Type": "application/json; charset=utf-8",
        }
        if self.debug:
            print(headers)
        return headers

    def _sign(self, params: dict, instruction: str, timestamp: int, window: int):
        """
        Returns encoded signature for given parameters, instruction, timestamp and window
        """
        sign_str = f"instruction={instruction}"
        sorted_params_list = []
        for key, value in sorted(params.items()):
            if isinstance(value, bool):
                value = str(value).lower()
            sorted_params_list.append(f"{key}={value}")
        sorted_params = "&".join(sorted_params_list)
        if sorted_params:
            sign_str += "&" + sorted_params
        sign_str += f"&timestamp={timestamp}&window={window}"
        if self.debug:
            print(sign_str)
        signature_bytes = self.private_key.sign(sign_str.encode())
        encoded_signature = base64.b64encode(signature_bytes).decode()
        return encoded_signature
