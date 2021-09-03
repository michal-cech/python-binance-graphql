from dataclasses import dataclass
from python_binance_graphql.models.base_model import BaseModel
from dataclasses_json import dataclass_json
from dataclasses_json.undefined import Undefined
import strawberry
from python_binance_graphql.utils.custom_types import BigInt


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class Kline(BaseModel):
    open_time: BigInt
    open: float
    high: float
    low: float
    close: float
    volume: float
    close_time: BigInt
    quote_asset_volume: float
    number_of_trades: BigInt
    taker_buy_base_asset_volume: float
    taker_buy_quote_asset_volume: float
    ignore: float

    @classmethod
    def serialize(cls, data):
        return Kline(*data)

    def deserialize(self):
        return [value for value in self.__dict__.values()]
