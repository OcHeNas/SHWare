from fastapi import APIRouter#, Depends

from app.object.components.sensors.values.dao import ValuesDAO
#from app.users.models import Users
#from app.users.dependencies import get_current_admin_user

router_values = APIRouter(
    prefix="/values",
    tags=["Показания датчика"],
)

@router_values.get("/all")
async def get_values(
    #user: Users = Depends(get_current_admin_user)
    ):
    return await ValuesDAO.find_all()

@router_values.get("/{id_sensor}")
async def get_component(id_sensor: int):
    return await ValuesDAO.find_values_by_sensor_id(id_sensor)