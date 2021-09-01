from typing import Optional

from dataclasses import dataclass
from typing import List
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
from .network_info import NetworkInfo
import strawberry


@strawberry.type
@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class CoinInfo:
    coin: Optional[str] = None
    free: Optional[float] = None
    freeze: Optional[float] = None
    ipoable: Optional[float] = None
    ipoing: Optional[float] = None
    isLegalMoney: Optional[bool] = None
    locked: Optional[float] = None
    name: Optional[str] = None
    networkList: Optional[List[NetworkInfo]] = None
    storage: Optional[float] = None
    trading: Optional[bool] = None
    withdrawAllEnable: Optional[bool] = None
    withdrawing: Optional[float] = None
