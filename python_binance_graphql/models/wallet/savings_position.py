from dataclasses import dataclass
from python_binance_graphql.models.base_model import BaseModel
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class SavingsPosition(BaseModel):
    annualInterestRate: float
    asset: str
    avgAnnualInterestRate: float
    canRedeem: bool
    dailyInterestRate: float
    freeAmount: float
    freezeAmount: float
    lockedAmount: float
    productId: str
    productName: str
    redeemingAmount: float
    todayPurchasedAmount: float
    totalAmount: float
    totalInterest: float
