from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.base import CRUDBase
from sqlalchemy.future import select
from app.schemas.airport import AirportCreate, AirportUpdate
from typing import Optional, List
from app.models import Airport
from app import models
from datetime import datetime

class CRUDAirport(CRUDBase[AirportCreate,AirportUpdate]):

    async def get_airports(
            self,
            db: AsyncSession,
            origin: Optional[str] = None,
            destination: Optional[str] = None,
            date: Optional[datetime] = None,
            way: Optional[str] = None,
            specific_day: Optional[datetime] = None,
    )-> list[Airport]:
        query = select(Airport)

        if origin:
            query = query.filter(models.Airport.origin == origin)
        
        if destination:
            query = query.filter(models.Airport.destination == destination)

        if date:
            query = query.filter(models.Airport.date == date)
        
        if way:
            query = query.filter(models.Airport.way == way)
        
        if specific_day:
            query = query.filter(models.Airport.specific_day == specific_day)

        result = await db.execute(query)
        airports = result.scalars().all()
    
        return airports
    async def get_multi_airpot(
            self,
            db:AsyncSession,
            objects_in: list
    ):
        pass

airport = CRUDAirport()

