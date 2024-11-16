from sqlalchemy.ext.asyncio import AsyncSession


from app import crud
from app.schemas.airport import AirportCreate
from tests.utils.utils import random_lower_string ,reandom_datetime


async def make_random_airport(db: AsyncSession)-> AirportCreate:

    origin = random_lower_string()
    destination = random_lower_string()
    data = reandom_datetime()
    way = random_lower_string()
    specific_day = reandom_datetime()

    airport = await crud.airport.get_airports(
        db=db,
        origin=origin,
        destination=destination,
        data=data,
        way=way,
        specific_day=specific_day
    )
    return airport
