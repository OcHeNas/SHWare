from sqlalchemy import Column, Integer, VARCHAR, TEXT, DATE, ForeignKey

from app.database import Base


class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(VARCHAR, nullable=False)
    description = Column(TEXT, nullable=False)



class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    fio = Column(VARCHAR, nullable=False)
    email = Column(VARCHAR, nullable=False)
    contact_phone = Column(VARCHAR, nullable=False)
    passport = Column(VARCHAR, nullable=False)
    inn = Column(VARCHAR, nullable=False)
    birthdate = Column(DATE, nullable=False)
    gender = Column(VARCHAR, nullable=False)
    hashed_password = Column(VARCHAR, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))


    def __str__(self):
        return f"Пользователь {self.email}"