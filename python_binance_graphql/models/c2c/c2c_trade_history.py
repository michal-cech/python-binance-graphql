from python_binance_graphql.utils.enums import BinanceOrderStatus
from typing import List, Optional
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses_json.undefined import Undefined
import strawberry
from python_binance_graphql.utils.custom_types import BigInt


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class C2COrder:
    ordeorderNumberrNo: BigInt
    advNo: BigInt
    indicatedAmount: float
    tradeType: str
    asset: str
    fiat: str
    fiatSymbol: str
    amount: float
    totalPrice: float
    unitPrice: float
    orderStatus: BinanceOrderStatus
    createTime: BigInt
    commission: float
    counterPartNickName: str
    advertisementRole: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class C2CTradeHistory:
    code: int
    message: str
    data: List[C2COrder]
    total: int
    success: bool
