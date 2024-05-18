from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

from app.database import Base

class Manufacturer(Base):
    __tablename__ = "manufacturer"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    email = Column(VARCHAR, nullable=False)
    contact_phone = Column(VARCHAR, nullable=False)
    address = Column(VARCHAR, nullable=False)