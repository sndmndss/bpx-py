from bpx.account import Account

public_key = "<KEY>"
secret_key = "<KEY>"


account = Account(public_key, secret_key, debug=True)


def account_example():
    print(account.get_fill_history_query("SOL_USDC", limit=999))
    print(account.get_withdrawals())
    print(account.execute_order("SOL_USDC", "Bid", "Limit", 0.01, time_in_force="IOC", price=1, window=10000))
    print(account.get_deposits(limit=100, offset=0, window=5000))
    print(account.get_balances())
    print(account.get_deposit_address("Solana"))
    print(account.get_order_history_query("SOL_USDC"))
    print(account.get_open_order("SOL_USDC", "13241231242"))
    print(account.cancel_order("SOL_USDC", "12313213"))
    print(account.cancel_all_orders("SOL_USDC"))


account_example()
