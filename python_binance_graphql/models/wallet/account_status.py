from python_binance_graphql.models.base_model import BaseModel
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses_json.undefined import Undefined
import strawberry


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class AccountStatus(BaseModel):
    data: str
