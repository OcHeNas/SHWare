from sqlalchemy import Column, Integer, TEXT, ForeignKey, TIMESTAMP

from app.database import Base

class Work(Base):
    __tablename__ = "work"

    id = Column(Integer, primary_key=True)
    description = Column(TEXT)
    start_date = Column(TIMESTAMP, nullable=False)
    end_date = Column(TIMESTAMP, nullable=False)
    object_id = Column(ForeignKey("object.id"))