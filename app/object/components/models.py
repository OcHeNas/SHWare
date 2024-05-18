from sqlalchemy import Column, Integer, VARCHAR, TEXT, ForeignKey

from app.database import Base
from app.object.components.manufacturer.models import Manufacturer

class Components(Base):
    __tablename__ = "components"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    description = Column(TEXT)
    type = Column(VARCHAR, nullable=False)
    model = Column(VARCHAR, nullable=False)
    object_id = Column(Integer, ForeignKey("object.id"))
    manufacturer_id = Column(Integer, ForeignKey(Manufacturer.id))