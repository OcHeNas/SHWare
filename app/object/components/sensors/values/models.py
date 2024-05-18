from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, TIMESTAMP

from app.database import Base


class Values(Base):
    __tablename__ = "values"

    id = Column(Integer, primary_key=True)
    value = Column(DECIMAL, nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    sensor_id = Column(Integer, ForeignKey("sensors.id"))