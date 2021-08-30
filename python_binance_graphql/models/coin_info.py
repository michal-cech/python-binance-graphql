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
    coin: str
    free: float
    freeze: float
    ipoable: float
    ipoing: float
    isLegalMoney: bool
    locked: float
    name: str
    networkList: List[NetworkInfo]
    storage: float
    trading: bool
    withdrawAllEnable: bool
    withdrawMin: float
