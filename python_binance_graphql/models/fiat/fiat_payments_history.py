from python_binance_graphql.models.base_model import BaseModel
from typing import List
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses_json.undefined import Undefined
import strawberry
from python_binance_graphql.utils.custom_types import BigInt


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class FiatPayment:
    orderNo: str
    sourceAmount: float
    fiatCurrency: str
    obtainAmount: float
    cryptoCurrency: str
    totalFee: float
    price: float
    status: str
    createTime: BigInt
    updateTime: BigInt


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class FiatPaymentsHistory(BaseModel):
    code: int
    message: str
    data: List[FiatPayment]
    total: int
    success: bool
