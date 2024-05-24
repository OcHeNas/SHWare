from fastapi import APIRouter, Depends
from app.exceptions import CannotAddDataToDatabase
from app.database import async_session_maker
from sqlalchemy import select, update

from app.object.components.manufacturer.dao import ManufacturerDAO
from app.object.components.manufacturer.schemas import SManufacturer
from app.object.components.manufacturer.models import Manufacturer
from app.users.models import Users
from app.users.dependencies import get_current_admin_user

router_manufacturer = APIRouter(
    prefix="/manufacturer",
    tags=["Производители"],
)

@router_manufacturer.get("/all")
async def get_manufacturer(
    #user: Users = Depends(get_current_admin_user)
    ):
    return await ManufacturerDAO.find_all()

@router_manufacturer.get("/{manufacturer_id}")
async def get_manufacturer(manufacturer_id: int):
    return await ManufacturerDAO.find_one_or_none(id = manufacturer_id)


@router_manufacturer.post("/add")
async def add_new_manufacturer(manufacturer_data: SManufacturer
                               #, user: Users = Depends(get_current_admin_user)
                               ):
    new_manufacturer = await ManufacturerDAO.add(name=manufacturer_data.name, email=manufacturer_data.email, contact_phone=manufacturer_data.contact_phone, address=manufacturer_data.address)
    if not new_manufacturer:
        raise CannotAddDataToDatabase
    
@router_manufacturer.put("/edit")
async def update_specific_manufacturer(manufacturer_id: int, new_manufacturer: SManufacturer
                                       #, user: Users = Depends(get_current_admin_user)
                                       ):
    async with async_session_maker() as session:
        query = select(Manufacturer).where(Manufacturer.id == manufacturer_id)
        existing_manufacturer = (await session.execute(query)).scalar_one_or_none()
        if existing_manufacturer:
            stmt = (
                update(Manufacturer)
                .where(Manufacturer.id == manufacturer_id)
                .values(**new_manufacturer.dict())
            )
            await session.execute(stmt)
            await session.commit()
            return {"status": "success", "message": f"Department with description '{manufacturer_id}' updated successfully"}
        else:
            return {"status": "error", "message": f"Department with description '{manufacturer_id}' not found"}
        
@router_manufacturer.delete("/{manufacturer_id}")
async def remove_manufacturer(manufacturer_id: int
                              #, user: Users = Depends(get_current_admin_user)
                              ):
    await ManufacturerDAO.delete(id=manufacturer_id)