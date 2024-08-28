from cryptography.hazmat.primitives.asymmetric import ed25519
import base64
from typing import Optional
from bpx.models.request_configuration import RequestConfiguration
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

    def get_balances(self, window: Optional[int] = None) -> RequestConfiguration:
        """
        Returns the url, headers for getting account balances

        https://docs.backpack.exchange/#tag/Capital/operation/get_balances
        """
        headers = self._headers({}, "balanceQuery", window=window)
        url = self.BPX_API_URL + "api/v1/capital"
        request_config = RequestConfiguration(url=url, headers=headers)
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
        if limit > 1000 or limit < 0:
            raise LimitValueError
        if offset < 0:
            raise NegativeValueError(offset)
        params = {
            "limit": limit,
            "offset": offset,
        }
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
        if limit > 1000 or limit < 0:
            raise LimitValueError
        if offset < 0:
            raise NegativeValueError(offset)
        params = {"limit": limit, "offset": offset}
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
        symbol: str,
        blockchain: str,
        quantity: str,
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
        headers = self._headers(params, "withdraw", window=window)
        url = self.BPX_API_URL + "wapi/v1/capital/withdrawals"
        request_config = RequestConfiguration(url=url, headers=headers, data=params)
        return request_config

    def get_order_history_query(
        self, symbol: str, limit: int, offset: int, window: Optional[int]
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for getting account order history

        https://docs.backpack.exchange/#tag/History/operation/get_order_history
        """
        if limit > 1000 or limit < 0:
            raise LimitValueError
        if offset < 0:
            raise NegativeValueError(offset)
        params = {"symbol": symbol, "limit": limit, "offset": offset}
        headers = self._headers(params, "orderHistoryQueryAll", window=window)
        url = self.BPX_API_URL + "wapi/v1/history/orders"
        request_config = RequestConfiguration(url=url, headers=headers, params=params)
        return request_config

    def get_fill_history_query(
        self,
        symbol: str,
        limit: int,
        offset: int,
        from_: Optional[int] = None,
        to: Optional[int] = None,
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
            "symbol": symbol,
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
        headers = self._headers(params, "fillHistoryQueryAll", window=window)
        url = self.BPX_API_URL + "wapi/v1/history/fills"
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
        time_in_force: Optional[str] = None,
        quantity: Optional[float] = None,
        price: float = 0,
        trigger_price: float = 0,
        self_trade_prevention: str = "RejectBoth",
        quote_quantity: Optional[float] = None,
        client_id: Optional[int] = None,
        post_only: Optional[bool] = None,
        window: Optional[int] = None,
    ) -> RequestConfiguration:
        """
        Returns the url, headers and request parameters for placing a new order

        https://docs.backpack.exchange/#tag/Order/operation/execute_order
        """
        if not SelfTradePrevention.has_value(self_trade_prevention):
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
        else:
            if TimeInForce.has_value(time_in_force):
                params["timeInForce"] = time_in_force
            else:
                raise InvalidTimeInForceValue(time_in_force)
        if client_id:
            params["clientId"] = client_id
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
        sorted_params = "&".join(
            f"{key}={value}" for key, value in sorted(params.items())
        )
        if sorted_params:
            sign_str += "&" + sorted_params
        sign_str += f"&timestamp={timestamp}&window={window}"
        if self.debug:
            print(sign_str)
        signature_bytes = self.private_key.sign(sign_str.encode())
        encoded_signature = base64.b64encode(signature_bytes).decode()
        return encoded_signature
