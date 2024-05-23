from fastapi import APIRouter, Depends
from app.exceptions import CannotAddDataToDatabase
from app.database import async_session_maker
from sqlalchemy import select, update

from app.object.dao import ObjectDAO
from app.object.schemas import SObject, SObjectEdit
from app.object.models import Object
from app.users.models import Users
from app.users.dependencies import get_current_user, get_current_admin_user

router_object = APIRouter(
    prefix="/objects",
    tags=["Объекты"],
)

@router_object.get("/all")
async def get_objects(
    #user: Users = Depends(get_current_admin_user)
    ):
    return await ObjectDAO.find_all()


@router_object.get("/my")
async def get_my_objects(user: Users = Depends(get_current_user)):
    return await ObjectDAO.find_all(responsible_person_id=user.id)

@router_object.post("/add")
async def add_new_object(object_data: SObject
                         #, user: Users = Depends(get_current_admin_user)
                         ):
    new_object = await ObjectDAO.add(name=object_data.name, description=object_data.description, status=object_data.status)
    if not new_object:
        raise CannotAddDataToDatabase
    
@router_object.put("/edit")
async def update_specific_object(object_id: int, new_object: SObjectEdit
                                 #, user: Users = Depends(get_current_admin_user)
                                 ):
    async with async_session_maker() as session:
        query = select(Object).where(Object.id == object_id)
        existing_object = (await session.execute(query)).scalar_one_or_none()
        if existing_object:
            stmt = (
                update(Object)
                .where(Object.id == object_id)
                .values(**new_object.dict())
            )
            await session.execute(stmt)
            await session.commit()
            return {"status": "success", "message": f"Department with description '{object_id}' updated successfully"}
        else:
            return {"status": "error", "message": f"Department with description '{object_id}' not found"}
        
@router_object.delete("/{object_id}")
async def remove_object(object_id: int
                        #, user: Users = Depends(get_current_admin_user)
                        ):
    await ObjectDAO.delete(id=object_id)
