from pydantic import BaseModel


class SComponents(BaseModel):
    name: str
    description: str
    type: str
    model: str
    object_id: int
    manufacturer_id: int

    class Config:
        orm_mode = True
