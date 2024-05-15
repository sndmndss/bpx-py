from bpx.base.base_account import BaseAccount
from bpx.http_client.sync_http_client import SyncHttpClient

http_client = SyncHttpClient()


class Account(BaseAccount):
    def __init__(self,
                 public_key: str,
                 secret_key: str,
                 window: int = 5000,
                 proxy: dict = None,
                 debug: bool = False,
                 default_http_client: SyncHttpClient = http_client
                 ):

        super().__init__(public_key,
                         secret_key,
                         window,
                         debug)
        self.http_client = default_http_client
        self.http_client.proxies = proxy

    def get_balances(self, window: int = None):
        url, headers = super().get_balances(window)
        return self.http_client.get(url, headers=headers)

    def get_deposits(self, limit: int = 100, offset: int = 0,
                     __from: int = None, to: int = None,  window: int = None):

        url, headers, params = super().get_deposits(limit, offset, window, __from, to)
        return self.http_client.get(url, headers=headers, params=params)

    def get_deposit_address(self, blockchain: str, window: int = None):
        url, headers, params = super().get_deposit_address(blockchain, window)
        return self.http_client.get(url, headers=headers, params=params)

    def get_withdrawals(self, limit: int = 100, offset: int = 0,
                        __from: int = None, to: int = None, window: int = None):

        url, headers, params = super().get_withdrawals(limit, offset, __from, to, window)
        return self.http_client.get(url, headers=headers, params=params)

    def withdrawal(self, address: str,
                   symbol: str,
                   blockchain: str,
                   quantity: str,
                   window: int = None):
        url, headers, params = super().withdrawal(address, symbol, blockchain, quantity, window)
        return self.http_client.post(url, headers=headers, data=params)

    def get_order_history_query(self, symbol: str, limit: int = 100, offset: int = 0, window: int = None):
        url, headers, params = super().get_order_history_query(symbol, limit, offset, window)
        return self.http_client.get(url, headers=headers, params=params)

    def get_fill_history_query(self, symbol: str,
                               limit: int = 100,
                               offset: int = 0,
                               __from: int = None,
                               to: int = None,
                               window: int = None):
        url, headers, params = super().get_fill_history_query(symbol,
                                                         limit,
                                                         offset,
                                                         __from,
                                                         to,
                                                         window)
        return self.http_client.get(url, headers=headers, params=params)

    def get_open_order(self, symbol: str,
                       order_id: str = None,
                       client_id: int = None,
                       window: int = None):
        url, headers, params = super().get_open_order(symbol, order_id, client_id, window)
        return self.http_client.get(url, headers=headers, params=params)

    def execute_order(self, symbol: str,
                      side: str,
                      order_type: str,
                      quantity: float,
                      time_in_force: str = None,
                      price: float = 0,
                      trigger_price: float = 0,
                      self_trade_prevention: str = "RejectBoth",
                      quote_quantity: float = None,
                      client_id: int = None,
                      post_only: bool = None,
                      window: int = None):

        url, headers, params = super().execute_order(symbol, side, order_type,
                                                time_in_force, quantity,
                                                price, trigger_price,
                                                self_trade_prevention, quote_quantity,
                                                client_id, post_only, window)
        return self.http_client.post(url, headers=headers, data=params)

    def cancel_order(self, symbol: str,
                     order_id: str = None,
                     client_id: int = None,
                     window: int = None):
        url, headers, params = super().cancel_order(symbol, order_id, client_id, window)
        return self.http_client.delete(url, headers=headers, data=params)

    def get_open_orders(self, symbol: str = None, window: int = None):
        url, headers, params = super().get_open_orders(symbol, window)
        return self.http_client.get(url, headers=headers, params=params)

    def cancel_all_orders(self, symbol: str, window: int = None):
        url, headers, params = super().cancel_all_orders(symbol, window)
        return self.http_client.delete(url, headers=headers, data=params)
