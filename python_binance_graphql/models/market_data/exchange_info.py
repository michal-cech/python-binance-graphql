from dataclasses import dataclass
from typing import List, Optional
from python_binance_graphql.utils.enums import BinanceOrderTypesEnum
from python_binance_graphql.models.filters import SymbolFilter, ExchangeFilter
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry
from python_binance_graphql.utils.custom_types import BigInt


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class RateLimitType:
    rateLimitType: str
    interval: str
    intervalNum: int
    limit: int


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
    permissions: List[str]
    filters: Optional[List[SymbolFilter]]


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class ExchangeInfo:
    timezone: str
    serverTime: BigInt
    rateLimits: List[RateLimitType]
    symbols: List[Symbol]
    exchangeFilter: Optional[List[ExchangeFilter]] = None
