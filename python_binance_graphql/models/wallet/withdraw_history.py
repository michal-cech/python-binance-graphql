from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses_json.undefined import Undefined
import strawberry


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class WithdrawHistory:
    address: str
    amount: float
    applyTime: str
    coin: str
    id: str
    withdrawOrderId: str
    network: str
    transferType: int
    status: int
    transactionFee: float
    txId: str
