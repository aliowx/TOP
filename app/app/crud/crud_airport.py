from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.base import CRUDBase
from app.db.base_class import Base
from app.schemas.airport import AirportCreate, AirportUpdate
from typing import Any

from app.models import Airport


class CRUDAirport(CRUDBase[AirportCreate,AirportUpdate]):
    
    async def create_airport(db: AsyncSession, airport: AirportCreate):
        db_airport = AirportCreate(name=airport.name, code=airport.code)
        db.add(db_airport)
        db.commit()
        db.refresh(db_airport)
        return db_airport

    async def get_airport(db: AsyncSession, airport_id: int):
        return db.query(AirportCreate).filter(AirportCreate.code == airport_id).first()


    async def get_airports(db:AsyncSession, skip: int = 0, limit: int = 100):
        return db.query(AirportCreate).offset(skip).limit(limit).all()
    
    async def delete_airport(db: AsyncSession, airport_id: int):
        db_airport = db.query(AirportCreate).filter(AirportCreate.code == airport_id).first()
        if db_airport:
            db.delete(db_airport)
            db.commit()
            return db_airport
        return None
    
    
airport = CRUDAirport()

