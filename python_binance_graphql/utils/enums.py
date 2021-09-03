from enum import Enum, IntEnum
import strawberry


@strawberry.enum
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


@strawberry.enum
class BinanceFiatMovementEnum(IntEnum):
    DEPOSIT = 0
    WITHDRAW = 1


@strawberry.enum
class BinanceFiatPaymentsEnum(IntEnum):
    BUY = 0
    SELL = 1


@strawberry.enum
class BinanceC2CTradeTypeEnum(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


@strawberry.enum
class BinanceOrderStatus(str, Enum):
    COMPLETED = "COMPLETED"
    PENDING = "PENDING"
    TRADING = "TRADING"
    BUYER_PAYED = "BUYER_PAYED"
    DISTRIBUTING = "DISTRIBUTING"
    IN_APPEAL = "IN_APPEAL"
    CANCELLED = "CANCELLED"
    CANCELLED_BY_SYSTEM = "CANCELLED_BY_SYSTEM"


@strawberry.enum
class BinanceOrderTypesEnum(str, Enum):
    LIMIT = "LIMIT"
    LIMIT_MAKER = "LIMIT_MAKER"
    MARKET = "MARKET"
    STOP_LOSS = "STOP_LOSS"
    STOP_LOSS_LIMIT = "STOP_LOSS_LIMIT"
    TAKE_PROFIT = "TAKE_PROFIT"
    TAKE_PROFIT_LIMIT = "TAKE_PROFIT_LIMIT"


@strawberry.enum
class BinanceKlineIntervalEnum(str, Enum):
    _1m = "1m"
    _3m = "3m"
    _5m = "5m"
    _15m = "15m"
    _30m = "30m"
    _1h = "1h"
    _2h = "2h"
    _4h = "4h"
    _6h = "6h"
    _8h = "8h"
    _12h = "12h"
    _1d = "1d"
    _3d = "3d"
    _1w = "1w"
    _1M = "1M"
