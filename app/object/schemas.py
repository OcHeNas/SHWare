from pydantic import BaseModel


class SObject(BaseModel):
    name: str
    description: str
    status: str

    class Config:
        orm_mode = True

class SObjectEdit(BaseModel):
    name: str
    description: str
    status: str
    responsible_person_id: int

    class Config:
        orm_mode = True



