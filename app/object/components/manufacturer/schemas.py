from pydantic import BaseModel, EmailStr


class SManufacturer(BaseModel):
    name: str
    email: EmailStr
    contact_phone: str
    address: str

    class Config:
        orm_mode = True