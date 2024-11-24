from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas
from app.api import deps
from app.schemas.airport import AirportBase
from app.utils import APIResponse 
from cache import cache
from cache.util import ONE_DAY_IN_SECONDS
from app.api.api_v1.services import providerA, providerB, FlightService
from datetime  import datetime

router = APIRouter()

namespace = "airports"


providers = [providerA,providerB]

flight_service = FlightService(providers)


@router.get('/', response_model=list[AirportBase])
@cache(namespace=namespace, expire=ONE_DAY_IN_SECONDS)
async def read_airports(
    db: AsyncSession = Depends(deps.get_db_async()),
    _: models.User = Depends(deps.get_current_superuser_from_cookie_or_basic),
        route: str = None,
        origin:str = None,
        destination: str = None,
        date: datetime = None,
        way: str = None,
        specific_day: datetime = None

)-> list[schemas.AirportBase]:
    
    response = await flight_service.search_all_flights(
        route=route,
        origin=origin,
        destination=destination,
        date=date,
        way=way,
        specific_day=specific_day
    )
    return APIResponse(response)



