from bpx.base.base_account import BaseAccount
from bpx.http_client.async_http_client import AsyncHttpClient
from typing import Optional

default_http_client = AsyncHttpClient()


class Account(BaseAccount):
    def __init__(
        self,
        public_key: str,
        secret_key: str,
        window: int = 5000,
        proxy: Optional[str] = None,
        debug: bool = False,
        http_client: AsyncHttpClient = default_http_client,
    ):
        super().__init__(public_key, secret_key, window, debug)
        self.http_client = http_client
        self.http_client.proxy = proxy

    async def get_balances(self, window: Optional[int] = None):
        """
        Returns the account balances

        https://docs.backpack.exchange/#tag/Capital/operation/get_balances
        """
        url, headers = super().get_balances(window)
        return await self.http_client.get(url, headers=headers)

    async def get_deposits(
        self,
        limit: int = 100,
        offset: int = 0,
        from_: Optional[int] = None,
        to: Optional[int] = None,
        window: Optional[int] = None,
    ):
        """
        Returns the account deposits

        https://docs.backpack.exchange/#tag/Capital/operation/get_deposits
        """
        url, headers, params = super().get_deposits(limit, offset, window)
        return await self.http_client.get(url, headers=headers, params=params)

    async def get_deposit_address(self, blockchain: str, window: Optional[int] = None):
        """
        Returns the deposit address for a specified blockchain

        https://docs.backpack.exchange/#tag/Capital/operation/get_deposit_address
        """
        url, headers, params = super().get_deposit_address(blockchain, window)
        return await self.http_client.get(url, headers=headers, params=params)

    async def get_withdrawals(
        self,
        limit: int = 100,
        offset: int = 0,
        from_: Optional[int] = None,
        to: Optional[int] = None,
        window: Optional[int] = None,
    ):
        """
        Returns the account withdrawals

        https://docs.backpack.exchange/#tag/Capital/operation/get_withdrawals
        """
        url, headers, params = super().get_withdrawals(limit, offset, from_, to, window)
        return await self.http_client.get(url, headers=headers, params=params)

    async def withdrawal(
        self,
        address: str,
        symbol: str,
        blockchain: str,
        quantity: str,
        window: Optional[int] = None,
    ):
        """
        Posts withdrawal and returns withdrawal status

        https://docs.backpack.exchange/#tag/Capital/operation/request_withdrawal
        """
        url, headers, params = super().withdrawal(
            address, symbol, blockchain, quantity, window
        )
        return await self.http_client.post(url, headers=headers, data=params)

    async def get_order_history_query(
        self, symbol: str, limit: int = 100, offset: int = 0, window: Optional[int] = None
    ):
        """
        Returns orders history of a specified symbol

        https://docs.backpack.exchange/#tag/History/operation/get_order_history
        """
        url, headers, params = super().get_order_history_query(
            symbol, limit, offset, window
        )
        return await self.http_client.get(url, headers=headers, params=params)

    async def get_fill_history_query(
        self,
        symbol: str,
        limit: int = 100,
        offset: int = 0,
        from_: Optional[int] = None,
        to: Optional[int] = None,
        window: Optional[int] = None,
    ):
        """
        Returns fills history of a specified symbol

        https://docs.backpack.exchange/#tag/History/operation/get_fills
        """
        url, headers, params = super().get_fill_history_query(
            symbol, limit, offset, from_, to, window
        )
        return await self.http_client.get(url, headers=headers, params=params)

    async def get_open_order(
        self,
        symbol: str,
        order_id: Optional[str] = None,
        client_id: Optional[int] = None,
        window: Optional[int] = None,
    ):
        """
        Returns open orders of a specified symbol

        https://docs.backpack.exchange/#tag/Order/operation/get_order
        """
        url, headers, params = super().get_open_order(
            symbol, order_id, client_id, window
        )
        return await self.http_client.get(url, headers=headers, params=params)

    async def execute_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: Optional[float] = None,
        time_in_force: Optional[str] = None,
        price: float = 0,
        trigger_price: float = 0,
        self_trade_prevention: str = "RejectBoth",
        quote_quantity: Optional[float] = None,
        client_id: Optional[int] = None,
        post_only: Optional[bool] = None,
        window: Optional[int] = None,
    ):
        """
        Posts order and returns the status of the executed order

        https://docs.backpack.exchange/#tag/Order/operation/execute_order
        """
        url, headers, params = super().execute_order(
            symbol,
            side,
            order_type,
            time_in_force,
            quantity,
            price,
            trigger_price,
            self_trade_prevention,
            quote_quantity,
            client_id,
            post_only,
            window,
        )
        return await self.http_client.post(url, headers=headers, data=params)

    async def cancel_order(
        self,
        symbol: str,
        order_id: Optional[str] = None,
        client_id: Optional[int] = None,
        window: Optional[int] = None,
    ):
        """
        Cancels an existing order

        https://docs.backpack.exchange/#tag/Order/operation/cancel_order
        """
        url, headers, params = super().cancel_order(symbol, order_id, client_id, window)
        return await self.http_client.delete(url, headers=headers, data=params)

    async def get_open_orders(self, symbol: str, window: Optional[int] = None):
        """
        Returns open orders of a specified symbol

        https://docs.backpack.exchange/#tag/Order/operation/get_open_orders
        """
        url, headers, params = super().get_open_orders(symbol, window)
        return await self.http_client.get(url, headers=headers, params=params)

    async def cancel_all_orders(self, symbol: str, window: Optional[int] = None):
        """
        Cancels all existing orders of a specified symbol

        https://docs.backpack.exchange/#tag/Order/operation/cancel_open_orders
        """
        url, headers, params = super().cancel_all_orders(symbol, window)
        return await self.http_client.delete(url, headers=headers, data=params)
