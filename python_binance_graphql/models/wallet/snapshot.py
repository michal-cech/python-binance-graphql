from dataclasses import dataclass
from python_binance_graphql.models.base_model import BaseModel
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry
from python_binance_graphql.utils.custom_types import BigInt
from typing import Dict, Union, List

from .snapshot_types import FuturesData, SpotData, MarginData


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class SnapshotData:
    type: str
    updateTime: BigInt
    data: Union[FuturesData, MarginData, SpotData]

    def __post_init__(self) -> "SnapshotData":
        if self.type == 'spot':
            self.data = SpotData.from_dict(self.data)
        elif self.type == 'margin':
            self.data = MarginData.from_dict(self.data)
        else:
            self.data = FuturesData.from_dict(self.data)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class Snapshot(BaseModel):
    code: int
    msg: str
    snapshotVos: List[SnapshotData]
