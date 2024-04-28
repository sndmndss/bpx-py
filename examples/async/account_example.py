from bpx.__async.account import Account
import asyncio

public_key = "<KEY>"
secret_key = "<KEY>>"

account = Account(public_key, secret_key)


async def account_example():
    fill_history = await account.get_fill_history_query("SOL_USDC", limit=999)
    withdrawals = await account.get_withdrawals()
    executed_order = await account.execute_order("SOL_USDC", "Bid", "Limit", 0.01, time_in_force="IOC", price=1, window=10000)
    deposits = await account.deposits(limit=1, offset=0, window=5000)
    balances = await account.get_balances()
    deposit_address = await account.get_deposit_address("Solana")
    order_history = await account.get_order_history_query("SOL_USDC")
    open_order = await account.get_open_order("SOL_USDC", "32142131231")
    cancelled_order = await account.cancel_order("SOL_USDC", "12313213")
    all_orders_cancelled = await account.cancel_all_orders("SOL_USDC")

    print("Account fills:", fill_history)
    print("Withdrawals:", withdrawals)
    print("Executed order:", executed_order)
    print("Deposits:", deposits)
    print("Balances:", balances)
    print("Deposit address:", deposit_address)
    print("Order history:", order_history)
    print("Open order:", open_order)
    print("Cancelled order:", cancelled_order)
    print("All orders cancelled:", all_orders_cancelled)

asyncio.run(account_example())