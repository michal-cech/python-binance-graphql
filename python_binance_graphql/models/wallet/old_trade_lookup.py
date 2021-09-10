from dataclasses import dataclass
from python_binance_graphql.models.base_model import BaseModel
from typing import Optional

from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
from python_binance_graphql.utils.custom_types import BigInt
import strawberry


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class OldTradeLookup(BaseModel):
    id: Optional[int] = None
    price: Optional[float] = None
    qty: Optional[float] = None
    quoteQty: Optional[float] = None
    time: Optional[BigInt] = None  # since graphql cannot represent >32 bit Int
    isBuyerMaker: Optional[bool] = None
    isBestMatch: Optional[bool] = None
