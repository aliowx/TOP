from sqlalchemy.ext.asyncio import AsyncSession
                                                    
from app import crud
from app import exceptions as exc
from app import schemas
from app.utils import MessageCodes
from datetime import datetime

async def read_airports(
    db: AsyncSession,
    origin: str = None,
    destination: str = None,
    date: datetime = None,
    way: str = None,
    specific_day: datetime = None,

)-> schemas.airport:
    
    airport = await crud.airport.get_airports(
        db=db,
        origin=origin,
        destination=destination,
        date=date,
        way=way,
        specific_day=specific_day

    )
    if not airport:
        raise exc.NotFoundException(
            detail="there isn't any airport here! sorry"
            
        )
    return airport

