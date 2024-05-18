from pydantic import BaseModel, EmailStr
from datetime import date


class SUserReg(BaseModel):
    fio: str
    email: EmailStr
    contact_phone: str
    passport: str
    inn: str
    birthdate: date
    gender: str
    password: str

    class Config:
        orm_mode = True


class SUserAuth(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True