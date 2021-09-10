from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class ExchangeFilter:
    filterType: str
    maxNumOrders: Optional[int] = None
    maxNumAlgoOrders: Optional[int] = None
