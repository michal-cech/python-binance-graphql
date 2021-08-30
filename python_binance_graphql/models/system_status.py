from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry


@strawberry.type
@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class SystemStatus:
    status: int
    msg: str
