from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry
from .trade import Trade


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class RecentTrade(Trade):
    pass
