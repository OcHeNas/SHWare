from pydantic import BaseModel
from datetime import datetime

class SWork(BaseModel):
    description: str
    start_date: datetime
    end_date: datetime
    object_id: int


    class Config:
        orm_mode = True