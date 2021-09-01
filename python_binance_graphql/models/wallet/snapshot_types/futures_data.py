from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class FuturesPosition:
    entryPrice: float
    markPrice: float
    positionAmt: float
    symbol: str
    unRealizedProfit: float


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class FuturesAsset:
    asset: str
    marginBalance: float
    walletBalance: float


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class FuturesData:
    assets: List[FuturesAsset]
    position: List[FuturesPosition]
    totalAssetOfBtc: float
