from sqlalchemy import Column, Integer, VARCHAR, TEXT, ForeignKey, DECIMAL

from app.database import Base


class Sensors(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    description = Column(TEXT)
    type = Column(VARCHAR, nullable=False)
    units_of_measurement = Column(VARCHAR, nullable=False)
    min_value = Column(DECIMAL, nullable=False)
    max_value = Column(DECIMAL, nullable=False)
    components_id = Column(Integer, ForeignKey("components.id"))