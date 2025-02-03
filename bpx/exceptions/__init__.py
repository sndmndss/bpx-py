class LimitValueError(Exception):
    """Exception when value is out of maximal allowed"""

    MIN = 0
    MAX = 1000

    def __init__(self):
        super().__init__(
            f"Limit value is out of allowed minimal {self.MIN} and maximal {self.MAX}."
        )


class NegativeValueError(Exception):
    """Exception when value is negative, when it's not expected to be"""

    def __init__(self, value):
        super().__init__(f"Value {value} can't be negative")


class InvalidTimeIntervalError(Exception):
    def __init__(self, invalid_value):
        self.invalid_value = invalid_value
        documentation_url = "https://docs.backpack.exchange/"
        message = (
            f"{invalid_value} is not a valid time interval.\n"
            f"See the documentation for more details: {documentation_url}"
        )
        super().__init__(message)


class InvalidTimeInForceValue(Exception):
    def __init__(self, value):
        documentation_url = "https://support.backpack.exchange/en/articles/543681"
        super().__init__(
            f"No such timeInForce value {value}\n"
            f"See the documentation for more details: {documentation_url}"
        )


class InvalidSelfTradePreventionError(Exception):
    def __init__(self, value):
        documentation_url = "https://support.backpack.exchange/en/articles/543681"
        super().__init__(
            f"No such selfTradePrevention value {value}\n"
            f"See the documentation for more details: {documentation_url}"
        )
