# Backpack SDK

## Installation

bpx-py is stable on _python_ >= 3.8

```bash
pip install bpx-py
```

## Usage

Make an account and generate API keys on [Backpack](https://backpack.exchange/settings/api-keys)

### Account example

```python
from bpx.account import Account

public_key = "<KEY>"
secret_key = "<KEY>"
account = Account(public_key, 
        secret_key,
        window=6000, # default value is 5000
        proxy={"http":"132.142.132.12:3128"}) # you can use any requests proxy supported by requests
deposit_address_sol = account.get_deposit_address("Solana")
account_fills = account.get_fill_history_query("SOL_USDC", 
                                               limit=10,
                                               window=10000) # window only for this order
print(deposit_address_sol)
print(account_fills)
```

bpx-py supports **async** code:
```python
from bpx.__async.account import Account
import asyncio

async def main():
    public_key = "<KEY>"
    secret_key = "<KEY>"
    account = Account(public_key, secret_key, proxy="http://your_proxy-address:1234")
    deposit_address_sol = await account.get_deposit_address("Solana")
    await asyncio.sleep(1)
    account_fills = await account.get_fill_history_query("SOL_USDC", 
                                               limit=10,
                                               window=10000)
    print(deposit_address_sol)
    print(account_fills)

asyncio.run(main())
```

### Public

Backpack has public endpoints that don't need API keys:

```python
from bpx.public import Public

public = Public() 
server_time = public.get_time()
markets = public.get_markets()
print(server_time)
print(markets)
```
**Async** code:

```python
from bpx.__async.public import Public
import asyncio

async def main():
    public = Public()
    assets = await public.get_assets()
    await asyncio.sleep(1)
    klines = await public.get_klines("SOL_USDC", "1d")
    print(assets)
    print(klines)
    
asyncio.run(main())
```

## Useful sources

[Discord channel to get help](https://discord.gg/backpack)

[Backpack API DOCS](https://docs.backpack.exchange)

[PYPI](https://pypi.org/project/bpx-py/)

[Backpack help center](https://support.backpack.exchange)