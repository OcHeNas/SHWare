from fastapi import APIRouter, Depends
from app.exceptions import CannotAddDataToDatabase
from app.database import async_session_maker
from sqlalchemy import select, update

from app.object.components.sensors.dao import SensorDAO
from app.object.components.sensors.schemas import SSensor, SSensorGet
from app.object.components.sensors.models import Sensors
from app.users.models import Users
from app.users.dependencies import get_current_admin_user

router_sensor = APIRouter(
    prefix="/sensor",
    tags=["Датчики"],
)

@router_sensor.get("/all")
async def get_sensor(user: Users = Depends(get_current_admin_user)) -> list[SSensorGet]:
    return await SensorDAO.find_all()

@router_sensor.get("/{sensr_id}")
async def get_sensor(sensor_id: int):
    await SensorDAO.find_one_or_none(id=sensor_id)


@router_sensor.post("/add")
async def add_new_sensor(sensor_data: SSensor):
    new_sensor = await SensorDAO.add(name=sensor_data.name, description=sensor_data.description, type=sensor_data.type, units_of_measurement=sensor_data.units_of_measurement, min_value=sensor_data.min_value, max_value=sensor_data.max_value, components_id=sensor_data.components_id)
    if not new_sensor:
        raise CannotAddDataToDatabase
    
@router_sensor.put("/edit")
async def update_specific_sensor(sensor_id: int, new_sensor: SSensor):
    async with async_session_maker() as session:
        query = select(Sensors).where(Sensors.id == sensor_id)
        existing_sensor = (await session.execute(query)).scalar_one_or_none()
        if existing_sensor:
            stmt = (
                update(Sensors)
                .where(Sensors.id == sensor_id)
                .values(**new_sensor.dict())
            )
            await session.execute(stmt)
            await session.commit()
            return {"status": "success", "message": f"Department with description '{sensor_id}' updated successfully"}
        else:
            return {"status": "error", "message": f"Department with description '{sensor_id}' not found"}
        
@router_sensor.delete("/{sensor_id}")
async def remove_sensor(sensor_id: int):
    await SensorDAO.delete(id=sensor_id)