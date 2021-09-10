from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class FlexibleProduct:
    asset: str
    avgAnnualInterestRate: float
    canPurchase: bool
    canRedeem: bool
    dailyInterestPerThousand: float
    featured: bool
    minPurchaseAmount: float
    productId: str
    purchasedAmount: float
    status: str
    upLimit: float
    upLimitPerUser: float
