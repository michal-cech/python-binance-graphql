from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class MarginAsset:
    asset: str
    borrowed: float
    free: float
    interest: float
    locked: float
    netAsset: float


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class MarginData:
    marginLevel: float
    totalAssetOfBtc: float
    totalLiabilityOfBtc: float
    totalNetAssetOfBtc: float
    userAssets: List[MarginAsset]
