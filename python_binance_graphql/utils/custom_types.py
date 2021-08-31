from typing import NewType
import strawberry

BigInt = strawberry.scalar(
    NewType("BigInt", int),
    serialize=lambda v: int(v),
    parse_value=lambda v: int(v)
)
