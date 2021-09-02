from enum import Enum, IntEnum, auto


class BinanceTransferTypeEnum(str, Enum):
    MAIN_C2C = "MAIN_C2C"
    MAIN_UMFUTURE = "MAIN_UMFUTURE"
    MAIN_CMFUTURE = "MAIN_CMFUTURE"
    MAIN_MARGIN = "MAIN_MARGIN"
    MAIN_MINING = "MAIN_MINING"
    C2C_MAIN = "C2C_MAIN"
    C2C_UMFUTURE = "C2C_UMFUTURE"
    C2C_MINING = "C2C_MINING"
    C2C_MARGIN = "C2C_MARGIN"
    UMFUTURE_MAIN = "UMFUTURE_MAIN"
    UMFUTURE_C2C = "UMFUTURE_C2C"
    UMFUTURE_MARGIN = "UMFUTURE_MARGIN"
    CMFUTURE_MAIN = "CMFUTURE_MAIN"
    CMFUTURE_MARGIN = "CMFUTURE_MARGIN"
    MARGIN_MAIN = "MARGIN_MAIN"
    MARGIN_UMFUTURE = "MARGIN_UMFUTURE"
    MARGIN_CMFUTURE = "MARGIN_CMFUTURE"
    MARGIN_MINING = "MARGIN_MINING"
    MARGIN_C2C = "MARGIN_C2C"
    MINING_MAIN = "MINING_MAIN"
    MINING_UMFUTURE = "MINING_UMFUTURE"
    MINING_C2C = "MINING_C2C"
    MINING_MARGIN = "MINING_MARGIN"
    MAIN_PAY = "MAIN_PAY"
    PAY_MAIN = "PAY_MAIN"
    ISOLATEDMARGIN_MARGIN = "ISOLATEDMARGIN_MARGIN"
    MARGIN_ISOLATEDMARGIN = "MARGIN_ISOLATEDMARGIN"
    ISOLATEDMARGIN_ISOLATEDMARGIN = "ISOLATEDMARGIN_ISOLATEDMARGIN"


class BinanceFiatMovementEnum(IntEnum):
    DEPOSIT = 0
    WITHDRAW = 1


class BinanceFiatPaymentsEnum(IntEnum):
    BUY = 0
    SELL = 1


class BinanceC2CTradeTypeEnum(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class BinanceOrderStatus(str, Enum):
    COMPLETED = auto()
    PENDING = auto()
    TRADING = auto()
    BUYER_PAYED = auto()
    DISTRIBUTING = auto()
    IN_APPEAL = auto()
    CANCELLED = auto()
    CANCELLED_BY_SYSTEM = auto()


class BinanceRateLimitersEnum(str, Enum):
    REQUEST_WEIGHT = auto()
    ORDERS = auto()
    RAW_REQUESTS = auto()


class BinanceExchangeFiltersEnum(str, Enum):
    EXCHANGE_MAX_NUM_ORDERS = auto()
    EXCHANGE_MAX_NUM_ALGO_ORDERS = auto()


class BinanceOrderTypesEnum(str, Enum):
    LIMIT = auto()
    LIMIT_MAKER = auto()
    MARKET = auto()
    STOP_LOSS = auto()
    STOP_LOSS_LIMIT = auto()
    TAKE_PROFIT = auto()
    TAKE_PROFIT_LIMIT = auto()


class BinanceSymbolFiltersEnum(str, Enum):
    PRICE_FILTER = auto()
    PERCENT_PRICE = auto()
    LOT_SIZE = auto()
    MIN_NOTIONAL = auto()
    ICEBERG_PARTS = auto()
    MARKET_LOT_SIZE = auto()
    MAX_NUM_ORDERS = auto()
    MAX_NUM_ALGO_ORDERS = auto()
    MAX_NUM_ICEBERG_ORDERS = auto()
    MAX_POSITION = auto()
