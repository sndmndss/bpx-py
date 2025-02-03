
# Backpack SDK

This Backpack SDK is a continuously updated and supported Python toolkit that provides comprehensive access to all Backpack endpoints.  

Trade on spot/perp markets, manage your account, lend/borrow and retrieve various data using Backpack API.


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
account_fills = account.get_fill_history("SOL_USDC", 
                                               limit=10,
                                               window=10000) # window only for this order
print(deposit_address_sol)
print(account_fills)
```

bpx-py supports **async** code:
```python
from bpx.async_.account import Account
from bpx.constants.enums import MarketTypeEnum
import asyncio

async def main():
    public_key = "<KEY>"
    secret_key = "<KEY>"
    account = Account(public_key, secret_key, proxy="http://your_proxy-address:1234")
    deposit_address_sol = await account.get_deposit_address("Solana")
    await asyncio.sleep(1)
    account_fills = await account.get_fill_history("SOL_USDC", 
                                               limit=10,
                                               window=10000,
                                               market_type=MarketTypeEnum.SPOT)
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
from bpx.async_.public import Public
from bpx.constants.enums import BorrowLendMarketHistoryIntervalEnum
import asyncio

async def main():
    public = Public()
    assets = await public.get_assets()
    await asyncio.sleep(1)
    klines = await public.get_borrow_lend_market_history(BorrowLendMarketHistoryIntervalEnum.ONE_DAY)
    print(assets)
    print(klines)
    
asyncio.run(main())
```

### Request Configuration

You can get the request configuration using `bpx.base.base_account` and `bpx.base.base_public` without doing a request.

```python
from bpx.base.base_account import BaseAccount
from bpx.base.base_public import BasePublic
from bpx.models.objects import RequestConfiguration  # unnecessary

base_public = BasePublic()
base_account = BaseAccount("<PUBLIC_KEY>", "<SECRET_KEY>", window=5000, debug=True)

# let's get url and headers for this account request
request_config: RequestConfiguration = base_account.get_balances()
url = request_config.url
headers = request_config.headers
# let's get url for this public request
request_url: str = base_public.get_ticker_url(symbol="SOL_USDC")
```

### Can be useful 

`bpx.models` - models that are in use by request and response (not full).

`bpx.constants.enums` - Enums and literals for your use and IDE typing.

## Useful sources

[Discord channel to get help](https://discord.gg/backpack)

[Backpack API DOCS](https://docs.backpack.exchange)

[PYPI](https://pypi.org/project/bpx-py/)

[Backpack help center](https://support.backpack.exchange)


