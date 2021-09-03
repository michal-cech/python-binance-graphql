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
class DribbletDetails:
    transId: BigInt
    serviceChargeAmount: float
    amount: float
    operateTime: BigInt
    transferedAmount: float
    fromAsset: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class Dribblet:
    operateTime: BigInt
    totalTransferedAmount: float
    totalServiceChargeAmount: float
    transId: BigInt
    userAssetDribbletDetails: List[DribbletDetails]


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class DustLog(BaseModel):
    total: int
    userAssetDribblets: List[Dribblet]
