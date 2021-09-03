from dataclasses import dataclass
from python_binance_graphql.models.base_model import BaseModel
from typing import List
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry
from python_binance_graphql.utils.custom_types import BigInt


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class OrderBook(BaseModel):
    lastUpdateId: BigInt
    bids: List[List[float]]
    asks: List[List[float]]
