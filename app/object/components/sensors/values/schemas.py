from pydantic import BaseModel
from decimal import Decimal
from datetime import date


class SValue(BaseModel):
    value: Decimal
    date: date
    sensor_id: int

    class Config:
        orm_mode = True