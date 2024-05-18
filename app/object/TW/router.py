from fastapi import APIRouter, Depends
from app.exceptions import CannotAddDataToDatabase

from app.object.TW.dao import TW_DAO
from app.object.TW.schemas import S_TW
from app.users.models import Users
from app.users.dependencies import get_current_admin_user

router_TW = APIRouter(
    prefix="/TW",
    tags=["Техническое обслуживание"],
)

@router_TW.get("/all")
async def get_TW(user: Users = Depends(get_current_admin_user)):
    return await TW_DAO.find_all()

@router_TW.get("/{TW_id}")
async def get_TW(TW_id: int):
    await TW_DAO.find_one_or_none(id=TW_id)


@router_TW.post("/add")
async def add_new_TW(TW_data: S_TW):
    new_TW = await TW_DAO.add(description=TW_data.description, date=TW_data.date, object_id=TW_data.object_id)
    if not new_TW:
        raise CannotAddDataToDatabase
    