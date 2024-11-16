from sqlalchemy.ext.asyncio import AsyncSession
from app.models.flight import Flight
from app.schemas.flight import FlightCreate, FlightUpdate
from app.crud.base import CRUDBase
from datetime import datetime

class CRUDFlight(CRUDBase[Flight, FlightCreate, FlightUpdate]):
    
    async def search_flights(
    db: AsyncSession, 
    origin_code: str, 
    destination_code: str, 
    date: datetime, 
    skip: int = 0, 
    limit: int = 100
):
        pass


flight = CRUDFlight(Flight)