from bpx.account import Account

PUBLIC_KEY = "<PUBLIC_KEY>"
SECRET_KEY = "<SECRET_KEY>"


def account_examples():
    account = Account(
        public_key=PUBLIC_KEY, secret_key=SECRET_KEY, debug=False, window=5000
    )

    print("=== get_account ===")
    print(account.get_account())

    # print("=== update_account ===")
    # print(
    #     account.update_account(
    #         leverage_limit="5",
    #     )
    # )

    print("=== get_borrow_lend_positions ===")
    print(account.get_borrow_lend_positions())

    print("=== execute_borrow_lend ===")
    # print(
    #     account.execute_borrow_lend(
    #         symbol="SOL",
    #         side="Borrow",
    #         quantity="0.1",
    #     )
    # )
    print("=== get_balances ===")
    print(account.get_balances())

    print("=== get_collateral ===")
    print(account.get_collateral())

    print("=== get_deposits ===")
    print(account.get_deposits(limit=100, offset=0))

    print("=== get_deposit_address ===")
    print(account.get_deposit_address(blockchain="Ethereum"))

    print("=== get_withdrawals ===")
    print(account.get_withdrawals(limit=100, offset=0))

    # print("=== withdrawal ===")
    # print(account.withdrawal(address="0x0x", symbol="ETH", blockchain="Ethereum", quantity="0.1", auto_borrow=False, auto_lend_redeem=False))

    print("=== get_open_positions ===")
    print(account.get_open_positions())

    print("=== get_borrow_history ===")
    print(account.get_borrow_history())

    print("=== get_interest_history ===")
    print(account.get_interest_history())

    print("=== get_order_history ===")
    print(account.get_order_history(symbol="SOL_USDC", limit=100))

    print("=== get_fill_history ===")
    print(account.get_fill_history(symbol="SOL_USDC", limit=1000, fill_type="User"))

    print("=== get_funding_payments ===")
    print(account.get_funding_payments(symbol="BTC_USDC_PERP", limit=1000))

    print("=== get_profit_and_loss_history ===")
    print(account.get_profit_and_loss_history(symbol="SOL_USDC_PERP"))

    print("=== get_settlements_history ===")
    print(account.get_settlements_history(limit=1000))

    print("=== get_open_order ===")
    print(account.get_open_order(symbol="SOL_USDC", order_id="123456789"))

    # print("=== execute_order ===")
    # print(account.execute_order(
    #     symbol="SOL_USDC",
    #     side="Ask",
    #     order_type="Limit",
    #     quantity="0.1",
    #     price="100",
    #     time_in_force="GTC",
    #     auto_lend_redeem=True,
    # ))

    # print("=== cancel_order ===")
    # print(account.cancel_order(symbol="SOL_USDC", order_id="987654321"))

    print("=== get_open_orders ===")
    print(account.get_open_orders("SOL_USDC"))

    # print("=== cancel_all_orders ===")
    # print(account.cancel_all_orders("SOL_USDC"))

    # print("=== submit_quote ===")
    # print(account.submit_quote(rfq_id="123456789", bid_price="100", ask_price="0.1"))


if __name__ == "__main__":
    account_examples()
