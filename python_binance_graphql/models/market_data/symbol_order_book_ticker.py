from dataclasses import dataclass
from python_binance_graphql.models.base_model import BaseModel
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class SymbolOrderBookTicker(BaseModel):
    symbol: str
    bidPrice: float
    bidQty: float
    askPrice: float
    askQty: float
