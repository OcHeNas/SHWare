from sqlalchemy import Column, Integer, VARCHAR, TEXT, ForeignKey

from app.database import Base

class Object(Base):
    __tablename__ = "object"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    description = Column(TEXT)
    status = Column(VARCHAR, nullable=False)
    responsible_person_id = Column(Integer, ForeignKey("users.id"))
