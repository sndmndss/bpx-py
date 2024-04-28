from cryptography.hazmat.primitives.asymmetric import ed25519
import base64
from time import time
from bpx.exceptions import *
from bpx.enums import *


class BaseAccount:
    BPX_API_URL = 'https://api.backpack.exchange/'

    def __init__(self,
                 public_key: str,
                 secret_key: str,
                 window: int,
                 debug: bool):

        self.private_key = ed25519.Ed25519PrivateKey.from_private_bytes(
            base64.b64decode(secret_key)
        )
        self.public_key = public_key
        self.window = window
        self.debug = debug

    def get_balances(self, window: int):
        headers = self._headers({}, 'balanceQuery', window=window)
        url = self.BPX_API_URL + 'api/v1/capital'
        return url, headers

    def deposits(self, limit: int, offset: int, window: int):
        if limit > 1000 or limit < 0:
            raise LimitValueError
        if offset < 0:
            raise NegativeValueError(offset)
        params = {
            'limit': limit,
            'offset': offset,
        }
        headers = self._headers(params, 'depositQueryAll', window=window)
        url = self.BPX_API_URL + 'wapi/v1/capital/deposits'
        return url, headers, params

    def get_deposit_address(self, blockchain: str, window: int):
        if not Blockchain.has_value(blockchain):
            raise InvalidBlockchainValue(blockchain)
        params = {'blockchain': blockchain}
        headers = self._headers(params, 'depositAddressQuery', window=window)
        url = self.BPX_API_URL + 'wapi/v1/capital/deposit/address'
        return url, headers, params

    def get_withdrawals(self, limit: int, offset: int, window: int):
        if limit > 1000 or limit < 0:
            raise LimitValueError
        if offset < 0:
            raise NegativeValueError(offset)
        params = {'limit': limit, 'offset': offset}
        headers = self._headers(params, 'withdrawalQueryAll', window=window)
        url = self.BPX_API_URL + 'wapi/v1/capital/withdrawals'
        return url, headers, params

    def withdrawal(self, address: str,
                   symbol: str,
                   blockchain: str,
                   quantity: str,
                   window: int):
        if not Blockchain.has_value(blockchain):
            raise InvalidBlockchainValue(blockchain)
        params = {
            'address': address,
            'blockchain': blockchain,
            'quantity': quantity,
            'symbol': symbol,
        }
        headers = self._headers(params, 'withdraw', window=window)
        url = self.BPX_API_URL + 'wapi/v1/capital/withdrawals'
        return url, headers, params

    def get_order_history_query(self, symbol: str, limit: int, offset: int, window: int):
        if limit > 1000 or limit < 0:
            raise LimitValueError
        if offset < 0:
            raise NegativeValueError(offset)
        params = {'symbol': symbol,
                  'limit': limit,
                  'offset': offset}
        headers = self._headers(params, 'orderHistoryQueryAll', window=window)
        url = self.BPX_API_URL + 'wapi/v1/history/orders'
        return url, headers, params

    def get_fill_history_query(self, symbol: str,
                               limit: int,
                               offset: int,
                               __from: int,
                               to: int,
                               window: int):
        if limit > 1000 or limit < 0:
            raise LimitValueError
        if offset < 0:
            raise NegativeValueError(offset)
        params = {
            'symbol': symbol,
            'limit': limit,
            'offset': offset,
        }
        if __from:
            if __from < 0:
                raise NegativeValueError(__from)
            else:
                params['from'] = __from
        if to:
            if to < 0:
                raise NegativeValueError(to)
            else:
                params['to'] = to
        headers = self._headers(params, 'fillHistoryQueryAll', window=window)
        url = self.BPX_API_URL + 'wapi/v1/history/fills'
        return url, headers, params

    def get_open_order(self, symbol: str,
                       order_id: str,
                       client_id: int,
                       window: int):

        params = {'symbol': symbol}
        if order_id:
            params['orderId'] = order_id
        if client_id:
            params['clientId'] = client_id
        headers = self._headers(params, 'orderQuery', window=window)
        url = self.BPX_API_URL + 'api/v1/order'
        return url, headers, params

    def execute_order(self, symbol: str,
                      side: str,
                      order_type: str,
                      time_in_force: str,
                      quantity: float,
                      price: float,
                      trigger_price: float,
                      self_trade_prevention: str,
                      quote_quantity: float,
                      client_id: int,
                      post_only: bool,
                      window: int):
        if not SelfTradePrevention.has_value(self_trade_prevention):
            raise InvalidSelfTradePreventionError(self_trade_prevention)
        params = {
            'symbol': symbol,
            'side': side,
            'orderType': order_type,
            'quantity': quantity,
            'selfTradePrevention': self_trade_prevention,
        }
        if order_type != "Market":
            if price:
                params['price'] = price
        if trigger_price:
            params['triggerPrice'] = trigger_price
        if quote_quantity:
            params['quoteQuantity'] = quote_quantity
        if post_only:
            params['postOnly'] = True
        else:
            if TimeInForce.has_value(time_in_force):
                params['timeInForce'] = time_in_force
            else:
                raise InvalidTimeInForceValue(time_in_force)
        if client_id:
            params['clientId'] = client_id
        headers = self._headers(params, 'orderExecute', window=window)
        url = self.BPX_API_URL + 'api/v1/order'
        return url, headers, params

    def cancel_order(self, symbol: str,
                     order_id: str,
                     client_id: int,
                     window: int):
        params = {'symbol': symbol}
        if order_id:
            params['orderId'] = order_id
        if client_id:
            params['clientId'] = client_id
        headers = self._headers(params, 'orderCancel', window=window)
        url = self.BPX_API_URL + 'api/v1/order'
        return url, headers, params

    def get_open_orders(self, symbol: str = None, window: int = None):
        params = {'symbol': symbol}
        headers = self._headers(params, 'orderQueryAll', window=window)
        url = self.BPX_API_URL + 'api/v1/orders'
        return url, headers, params

    def cancel_all_orders(self, symbol: str, window: int = None):
        params = {'symbol': symbol}
        headers = self._headers(params, 'orderCancelAll', window=window)
        url = self.BPX_API_URL + 'api/v1/orders'
        return url, headers, params

    def _headers(self,
                 params: dict,
                 instruction: str,
                 window: int) -> dict:
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
