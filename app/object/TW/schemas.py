from pydantic import BaseModel
from datetime import date

class S_TW(BaseModel):
    description: int
    date: date
    object_id: int

    class Config:
        orm_mode = True