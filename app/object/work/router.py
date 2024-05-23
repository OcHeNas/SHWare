from fastapi import APIRouter, Depends
from app.exceptions import CannotAddDataToDatabase

from app.object.work.dao import WorkDAO
from app.object.work.schemas import SWork
from app.users.models import Users
from app.users.dependencies import get_current_admin_user

router_Work = APIRouter(
    prefix="/Work",
    tags=["Технические работы"],
)

@router_Work.get("/all")
async def get_Work(
    #user: Users = Depends(get_current_admin_user)
    ):
    return await WorkDAO.find_all()

@router_Work.get("/{id_object}")
async def get_Work(id_object: int):
    await WorkDAO.find_all(object_id=id_object)


@router_Work.post("/add")
async def add_new_Work(Work_data: SWork):
    new_Work = await WorkDAO.add(description=Work_data.description, start_date=Work_data.start_date, end_date=Work_data.end_date, object_id=Work_data.object_id)
    if not new_Work:
        raise CannotAddDataToDatabase