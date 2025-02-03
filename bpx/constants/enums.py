from enum import Enum
from typing import Literal


class TimeIntervalEnum(str, Enum):
    ONE_MINUTE = "1m"
    THREE_MINUTES = "3m"
    FIVE_MINUTES = "5m"
    FIFTEEN_MINUTES = "15m"
    THIRTY_MINUTES = "30m"
    ONE_HOUR = "1h"
    TWO_HOURS = "2h"
    FOUR_HOURS = "4h"
    SIX_HOURS = "6h"
    EIGHT_HOURS = "8h"
    TWELVE_HOURS = "12h"
    ONE_DAY = "1d"
    THREE_DAYS = "3d"
    ONE_WEEK = "1w"
    ONE_MONTH = "1month"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    def __str__(self):
        return self.value


TimeIntervalType = Literal[
    "1m",
    "3m",
    "5m",
    "15m",
    "30m",
    "1h",
    "2h",
    "4h",
    "6h",
    "8h",
    "12h",
    "1d",
    "3d",
    "1w",
    "1month",
]


class TimeInForceEnum(str, Enum):
    GTC = "GTC"
    IOC = "IOC"
    FOK = "FOK"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    def __str__(self):
        return self.value


TimeInForceType = Literal["GTC", "IOC", "FOK"]


class SelfTradePreventionEnum(str, Enum):
    REJECT_TAKER = "RejectTaker"
    REJECT_MAKER = "RejectMaker"
    REJECT_BOTH = "RejectBoth"
    ALLOW_ALL = "Allow"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    def __str__(self):
        return self.value


SelfTradePreventionType = Literal["RejectTaker", "RejectMaker", "RejectBoth", "Allow"]


class BorrowLendSideEnum(str, Enum):
    BORROW = "Borrow"
    LEND = "Bend"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    def __str__(self):
        return self.value


BorrowLendSideType = Literal["Borrow", "Lend"]


class BorrowLendEventEnum(str, Enum):
    BORROW = "Borrow"
    BORROW_REPAY = "BorrowRepay"
    LEND = "Lend"
    LEND_REDEEM = "LendRedeem"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    def __str__(self):
        return self.value


BorrowLendEventType = Literal["Borrow", "BorrowRepay", "Lend", "LendRedeem"]


class InterestPaymentSourceEnum(str, Enum):
    UNREALIZED_PNL = "UnrealizedPnl"
    BORROW_LEND = "BorrowLend"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    def __str__(self):
        return self.value


InterestPaymentSourceType = Literal["UnrealizedPnl", "BorrowLend"]


class BorrowLendPositionStateEnum(str, Enum):
    OPEN = "Open"
    CLOSED = "Closed"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    def __str__(self):
        return self.value


BorrowLendPositionStateType = Literal["Open", "Closed"]


class MarketTypeEnum(str, Enum):
    SPOT = "SPOT"
    PERP = "PERP"
    IPERP = "IPERP"
    DATED = "DATED"
    PREDICTION = "PREDICTION"
    RFQ = "RFQ"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    def __str__(self):
        return self.value


MarketTypeType = Literal["SPOT", "PERP", "IPERP", "DATED", "PREDICTION", "RFQ"]


class FillTypeEnum(str, Enum):
    USER = "User"
    BOOK_LIQUIDATION = "BookLiquidation"
    ADL = "Adl"
    BACKSTOP = "Backstop"
    LIQUIDATION = "Liquidation"
    ALL_LIQUIDATION = "Allliquidation"
    COLLATERAL_CONVERSION = "CollateralConversion"
    COLLATERAL_CONVERSION_AND_SPOT_LIQUIDATION = (
        "CollateralConversionAndSpotLiquidation"
    )

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    def __str__(self):
        return self.value


FillTypeType = Literal[
    "User",
    "BookLiquidation",
    "Adl",
    "Backstop",
    "Liquidation",
    "Allliquidation",
    "CollateralConversion",
    "CollateralConversionAndSpotLiquidation",
]


class SettlementSourceFilterEnum(str, Enum):
    BACKSTOP_LIQUIDATION = "BackstopLiquidation"
    CULLED_BORROW_INTEREST = "CulledBorrowInterest"
    CULLED_REALIZE_PNL = "CulledRealizePnl"
    CULLED_REALIZE_PNL_BOOK_UTILIZATION = "CulledRealizePnlBookUtilization"
    FUNDING_PAYMENT = "FundingPayment"
    REALIZE_PNL = "RealizePnl"
    TRADING_FEES = "TradingFees"
    TRADING_FEES_SYSTEM = "TradingFeesSystem"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    def __str__(self):
        return self.value


SettlementSourceFilterType = Literal[
    "BackstopLiquidation",
    "CulledBorrowInterest",
    "CulledRealizePnl",
    "CulledRealizePnlBookUtilization",
    "FundingPayment",
    "RealizePnl",
    "TradingFees",
    "TradingFeesSystem",
]


class BorrowLendMarketHistoryIntervalEnum(str, Enum):
    ONE_DAY = "1d"
    ONE_WEEK = "1w"
    ONE_MONTH = "1month"
    ONE_YEAR = "1year"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    def __str__(self):
        return self.value


BorrowLendMarketHistoryIntervalType = Literal["1d", "1w", "1month", "1year"]
