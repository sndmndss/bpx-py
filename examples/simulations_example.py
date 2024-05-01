from bpx.simulations import *
from bpx.account import Account


public_key = "<KEY>"
secret_key = "<KEY>"


account = Account(public_key, secret_key, debug=True)

fills = account.get_fill_history_query("SOL_USDC", limit=1000)
print(get_fees(fills))
print(get_volume(fills))


balance = account.get_balances()
print(get_approximate_balance_in_usdc(balance))
