from python_binance_graphql.models.base_model import BaseModel
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses_json.undefined import Undefined
import strawberry
from python_binance_graphql.utils.custom_types import BigInt
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class APIKeyPermissions(BaseModel):
    ipRestrict: bool
    createTime: BigInt
    enableWithdrawals: bool
    enableInternalTransfer: bool
    permitsUniversalTransfer: bool
    enableVanillaOptions: bool
    enableReading: bool
    enableFutures: bool
    enableMargin: bool
    enableSpotAndMarginTrading: bool
    tradingAuthorityExpirationTime: Optional[BigInt] = None
