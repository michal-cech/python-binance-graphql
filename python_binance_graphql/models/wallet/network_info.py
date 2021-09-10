from python_binance_graphql.models.base_model import BaseModel
from typing import Optional

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dataclasses_json import undefined
from dataclasses_json.undefined import Undefined
import strawberry


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class NetworkInfo(BaseModel):
    addressRegex: Optional[str] = None
    coin: Optional[str] = None
    depositDesc: Optional[str] = None
    depositEnable: Optional[bool] = None
    isDefault: Optional[bool] = None
    memoRegex: Optional[str] = None
    minConfirm: Optional[float] = None
    name: Optional[str] = None
    network: Optional[str] = None
    resetAddressStatus: Optional[str] = None
    specialTips: Optional[str] = None
    unLockConfirm: Optional[int] = None
    withdrawDesc: Optional[str] = None
    withdrawEnable: Optional[bool] = None
    withdrawFee: Optional[float] = None
    withdrawMin: Optional[float] = None
