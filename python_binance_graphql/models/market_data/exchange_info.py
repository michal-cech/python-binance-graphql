from dataclasses import dataclass
from typing import List
from python_binance_graphql.utils.enums import BinanceExchangeFiltersEnum, BinanceOrderTypesEnum, BinanceRateLimitersEnum, BinanceSymbolFiltersEnum
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry
from python_binance_graphql.utils.custom_types import BigInt


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class Symbol:
    symbol: str
    status: str
    baseAsset: str
    baseAssetPrecision: int
    quoteAsset: str
    quotePrecision: int
    quoteAssetPrecision: int
    orderTypes: List[BinanceOrderTypesEnum]
    icebergAllowed: bool
    ocoAllowed: bool
    isSpotTradingAllowed: bool
    isMarginTradingAllowed: bool
    filters: List[BinanceSymbolFiltersEnum]
    permissions: List[str]


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class ExchangeInfo:
    timezone: str
    serverTime: BigInt
    rateLimits: List[BinanceRateLimitersEnum]
    exchangeFilter: List[BinanceExchangeFiltersEnum]
    symbols: List[Symbol]
