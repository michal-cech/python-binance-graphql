from python_binance_graphql.models.base_model import BaseModel
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses_json.undefined import Undefined, CatchAll
import strawberry
from python_binance_graphql.utils.custom_types import BigInt
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class AssetDetailInfo:
    minWithdrawAmount: float
    depositStatus: bool
    withdrawFee: int
    withdrawStatus: bool
    depositTip: Optional[str] = None


@dataclass_json(undefined=Undefined.INCLUDE)
@dataclass
@strawberry.type
class AssetDetail(BaseModel):
    data: CatchAll

    def __post_init__(self):
        print(self.data)
        for k, v in self.data.items():
            self.data[k] = AssetDetailInfo.from_dict(v)
