from app.dao.base import BaseDAO
from app.object.components.sensors.models import Sensors


class SensorDAO(BaseDAO):
    model = Sensors