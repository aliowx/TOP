from typing import Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_, select,desc
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Passenger
from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.db.base_class import Base
from app.models import Passenger


from app.schemas.passenger import PassengerCreate, PassengerCreate

class CRUDPassenger(CRUDBase[Passenger,PassengerCreate, PassengerCreate]):

    async def get_passenger(
            self,
            db:AsyncSession,
            user_id: int
    )->list[Passenger]:
        
        query = (
            select(pasenger)
            .where(pasenger.user_id == user_id)
            .order_by(desc(pasenger.purchase_date))  
            .limit(10)  
        )

        
        result = await db.execute(query)
        return result.scalars().all()
    


    async def insert_passenger(
        self,
        db: AsyncSession,
        user_id: int,
        name: str,
        age: int,
        nationa_id: int

    ):
        new_passenger = pasenger(
            user_id=user_id,
            name=name,
            age=age,
            nationa_id=nationa_id
        )

        db.add(new_passenger)


pasenger = CRUDPassenger(Passenger)
