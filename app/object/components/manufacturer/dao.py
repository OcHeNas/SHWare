from app.dao.base import BaseDAO
from app.object.components.manufacturer.models import Manufacturer


class ManufacturerDAO(BaseDAO):
    model = Manufacturer