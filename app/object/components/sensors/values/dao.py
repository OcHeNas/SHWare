from app.dao.base import BaseDAO
from app.object.components.sensors.values.models import Values


class ValuesDAO(BaseDAO):
    model = Values