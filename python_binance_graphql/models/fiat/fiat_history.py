from typing import List, Optional
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses_json.undefined import Undefined
import strawberry
from python_binance_graphql.utils.custom_types import BigInt


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class FiatOrder:
    orderNo: str
    fiatCurrency: str
    indicatedAmount: float
    amount: float
    totalFee: float
    status: str
    createTime: BigInt
    updateTime: BigInt
    method: Optional[str] = None


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class FiatHistory:
    code: int
    message: str
    data: List[FiatOrder]
    total: int
    success: bool
