from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class SymbolFilter:
    filterType: str
    minPrice: Optional[float] = None
    maxPrice: Optional[float] = None
    tickSize: Optional[float] = None
    multiplierUp: Optional[float] = None
    multiplierDown: Optional[float] = None
    avgPriceMins: Optional[float] = None
    minQty: Optional[float] = None
    maxQty: Optional[float] = None
    stepSize: Optional[float] = None
    minNotional: Optional[float] = None
    applyToMarket: Optional[bool] = None
    avgPriceMins: Optional[float] = None
    limit: Optional[float] = None
    maxNumOrders: Optional[int] = None
    maxNumAlgoOrders: Optional[int] = None
    maxNumIcebergOrders: Optional[int] = None
    maxPosition: Optional[float] = None
