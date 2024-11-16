from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas
from app.api import deps
from app.schemas.airport import AirportBase
from app.utils import APIResponse 
from app.api.api_v1 import services
from cache import cache
from cache.util import ONE_DAY_IN_SECONDS
from datetime import datetime

router = APIRouter()
namespace = "airports"

@router.get('/', response_model=list[AirportBase])
@cache(namespace=namespace, expire=ONE_DAY_IN_SECONDS)
async def read_airports(
    db: AsyncSession = Depends(deps.get_db_async()),
    origin: str = None,
    destination: str = None,
    date: datetime = None,
    way: str = None,
    specific_day: datetime = None,
    _: models.User = Depends(deps.get_current_superuser_from_cookie_or_basic),

)-> list[schemas.Ariport]:
    
    response = await services.read_airports(
        db=db,
        origin=origin,
        destination=destination,
        date=date,
        way=way,
        specific_day=specific_day
    )
    return APIResponse(response)