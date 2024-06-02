from app.dao.base import BaseDAO
from app.object.components.sensors.values.models import Values
from app.object.components.sensors.values.schemas import SValue
from sqlalchemy import select
from app.database import async_session_maker

class ValuesDAO(BaseDAO):
    model = Values

    @classmethod
    async def find_values_by_sensor_id(cls, sensor_id: int):
            async with async_session_maker() as session:
                query = select(Values.value).where(Values.sensor_id == sensor_id)
                result = await session.execute(query)
                return result.scalars().all()