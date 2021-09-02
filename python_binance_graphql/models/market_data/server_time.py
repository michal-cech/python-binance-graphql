from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry
from python_binance_graphql.utils.custom_types import BigInt


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class ServerTime:
    serverTime: BigInt
