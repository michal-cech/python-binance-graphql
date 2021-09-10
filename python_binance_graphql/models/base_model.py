from dataclasses_json import dataclass_json
from dataclasses import dataclass
from dataclasses_json.undefined import Undefined
import strawberry


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
@strawberry.type
class BaseModel():
    @classmethod
    def serialize(cls, data):
        return cls.from_dict(data)

    def deserialize(self):
        return self.to_dict()
