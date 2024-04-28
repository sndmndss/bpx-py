from enum import Enum


class Blockchain(Enum):
    ETHEREUM = "Ethereum"
    SOLANA = "Solana"
    Polygon = "Polygon"
    BITCOIN = "Bitcoin"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class TimeInterval(Enum):
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


class TimeInForce(Enum):
    GTC = "GTC"
    IOC = "IOC"
    FOK = "FOK"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class SelfTradePrevention(Enum):
    REJECT_TAKER = "RejectTaker"
    REJECT_MAKER = "RejectMaker"
    REJECT_BOTH = "RejectBoth"
    ALLOW_ALL = "Allow"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_
