from dataclasses import dataclass
from python_binance_graphql.models.base_model import BaseModel
from typing import List

from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
from python_binance_graphql.utils.custom_types import BigInt
import strawberry


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class QueryUserUniversalTransferHistoryInfo:
    asset: str
    amount: int
    type: str
    status: str
    tranId: BigInt
    timestamp: BigInt


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class QueryUserUniversalTransferHistory(BaseModel):
    total: int
    rows: List[QueryUserUniversalTransferHistoryInfo]
