from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dataclasses_json import undefined
from dataclasses_json.undefined import Undefined
import strawberry


@strawberry.type
@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class NetworkInfo:
    addressRegex: str
    coin: str
    depositDesc: str
    depositEnable: bool
    isDefault: bool
    memoRegex: str
    minConfig: float
    name: str
    network: str
    resetAddressStatus: str
    specialTips: str
    unlockConfirm: int
    withdrawDesc: str
    withdrawEnable: bool
    withdrawFree: float
    withdrawMin: float
