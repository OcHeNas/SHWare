from fastapi import APIRouter, Depends
from app.exceptions import CannotAddDataToDatabase
from app.database import async_session_maker
from sqlalchemy import select, update

from app.object.components.dao import ComponentsDAO
from app.object.components.schemas import SComponents
from app.object.components.models import Components
from app.users.models import Users
from app.users.dependencies import get_current_admin_user

router_components = APIRouter(
    prefix="/components",
    tags=["Компоненты"],
)

@router_components.get("/all")
async def get_components(user: Users = Depends(get_current_admin_user)):
    return await ComponentsDAO.find_all()

@router_components.get("/{component_id}")
async def get_component(component_id: int):
    return await ComponentsDAO.find_one_or_none(id=component_id)


@router_components.post("/add")
async def add_new_component(component_data: SComponents, user: Users = Depends(get_current_admin_user)):
    new_component = await ComponentsDAO.add(name=component_data.name, description=component_data.description, type=component_data.type, model=component_data.model, object_id=component_data.object_id,  manufacturer_id=component_data.manufacturer_id)
    if not new_component:
        raise CannotAddDataToDatabase
    
@router_components.put("/edit")
async def update_specific_component(component_id: int, new_component: SComponents, user: Users = Depends(get_current_admin_user)):
    async with async_session_maker() as session:
        query = select(Components).where(Components.id == component_id)
        existing_component = (await session.execute(query)).scalar_one_or_none()
        if existing_component:
            stmt = (
                update(Components)
                .where(Components.id == component_id)
                .values(**new_component.dict())
            )
            await session.execute(stmt)
            await session.commit()
            return {"status": "success", "message": f"Department with description '{component_id}' updated successfully"}
        else:
            return {"status": "error", "message": f"Department with description '{component_id}' not found"}
        
@router_components.delete("/{component_id}")
async def remove_component(component_id: int, user: Users = Depends(get_current_admin_user)):
    await ComponentsDAO.delete(id=component_id)