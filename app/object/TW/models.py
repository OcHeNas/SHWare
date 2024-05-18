from sqlalchemy import Column, Integer, TEXT, ForeignKey, DATE

from app.database import Base

class TW(Base):
    __tablename__ = "TW"

    id = Column(Integer, primary_key=True)
    description = Column(TEXT)
    date = Column(DATE, nullable=False)
    object_id = Column(Integer, ForeignKey("object.id"))