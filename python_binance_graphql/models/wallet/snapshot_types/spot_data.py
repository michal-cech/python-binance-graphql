from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class SpotBalance:
    asset: str
    free: float
    locked: float


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class SpotData:
    balances: List[SpotBalance]
    totalAssetOfBtc: float
