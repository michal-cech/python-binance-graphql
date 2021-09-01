from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses_json.undefined import Undefined
import strawberry
from python_binance_graphql.utils.custom_types import BigInt
from typing import Dict


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class AccountTradingStatusTriggerCondition:
    GCR: int
    IFER: int
    UFR: int


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class AccountTradingStatusData:
    isLocked: bool
    plannedRecoverTime: int
    triggerCondition: AccountTradingStatusTriggerCondition
    indicators: Dict  # possible TODO
    updateTime: BigInt


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class AccountTradingStatus:
    data: str
