from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses_json.undefined import Undefined
import strawberry
from python_binance_graphql.utils.custom_types import BigInt
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class AssetDividendRecordInfo:
    amount: float
    asset: str
    divTime: BigInt
    enInfo: str
    tranId: BigInt


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class AssetDividendRecord:
    rows: List[AssetDividendRecordInfo]
    total: int
