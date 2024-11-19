from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.base import CRUDBase

from app.schemas.airport import AirportCreate, AirportUpdate
from typing import Optional, List
from app.models import Airport

from datetime import datetime

class CRUDAirport(CRUDBase[Airport, AirportCreate, AirportUpdate]):

    async def get_airports(
            self,
            db: AsyncSession,
            origin: Optional[str] = None,
            destination: Optional[str] = None,
            date: Optional[datetime] = None,
            way: Optional[str] = None,
            specific_day: Optional[datetime] = None,
    ) -> List[Airport]:
        query = select(Airport)

        if origin:
            query = query.filter(Airport.origin == origin)
        
        if destination:
            query = query.filter(Airport.destination == destination)

        if date:
            query = query.filter(Airport.date == date)
        
        if way:
            query = query.filter(Airport.way == way)
        
        if specific_day:
            query = query.filter(Airport.specific_day == specific_day)

        result = await db.execute(query)
        airports = result.scalars().all()
    
        return airports


airport = CRUDAirport(Airport)

