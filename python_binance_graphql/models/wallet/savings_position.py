from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class SavingsPosition:
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
