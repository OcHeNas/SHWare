from pydantic import BaseModel
from decimal import Decimal


class SSensor(BaseModel):
    name: str
    description: str
    type: str
    units_of_measurement: str
    min_value: Decimal
    max_value: Decimal
    components_id: int

    class Config:
        orm_mode = True

class SSensorGet(BaseModel):
    id: int
    name: str
    description: str
    type: str
    units_of_measurement: str
    min_value: Decimal
    max_value: Decimal
    components_id: int

    class Config:
        orm_mode = True