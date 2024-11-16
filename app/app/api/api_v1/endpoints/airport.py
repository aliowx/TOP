from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, models, schemas
from app.api import deps
from app.utils import APIResponseType
from cache import cache, invalidate
from cache.util import ONE_DAY_IN_SECONDS

router = APIRouter()
namespace = "airports"

@router.get('/')
@cache(namespace=namespace, expire=ONE_DAY_IN_SECONDS)
async def read_airports(
    db: AsyncSession = Depends(deps.get_db_async),
    skip: int = 0,
    limit: int = 100,
    _: models.User = Depends(deps.get_current_superuser_from_cookie_or_basic),
)-> list:
    
    airports = await crud.airport.get_airports(db=db, skip=skip, limit=limit)
    if not airports:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="there isn't airport avilabel")



@router.post('/')
@cache(namespace=namespace, expire=ONE_DAY_IN_SECONDS)
async def create_airport(
    airport: schemas.AirportCreate,
    db: AsyncSession = Depends(deps.get_db_async),
    _: models.User = Depends(deps.get_current_superuser_from_cookie_or_basic),
):
    new_airport = await crud.airport.create_airport(db=db, airport=airport)
    return APIResponseType(data=new_airport, message="Airport created successfully")