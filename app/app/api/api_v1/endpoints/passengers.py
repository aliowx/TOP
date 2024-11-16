from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, models, schemas
from app.api import deps
from app.utils import APIResponse, APIResponseType
from app.api.api_v1 import services
from app.utils import APIResponseType
from cache import cache, invalidate
from cache.util import ONE_DAY_IN_SECONDS
from datetime import datetime



router = APIRouter()
namespace = "passengers"


@router.get('/')
@cache(namespace=namespace, expire=ONE_DAY_IN_SECONDS)
async def read_passengers(
    db:AsyncSession=Depends(deps.get_db_async()),
    user_in: int = None,
    _: models.User = Depends(deps.get_current_superuser_from_cookie_or_basic),
)-> APIResponseType[schemas.PassengerResponse]:
    
    response = await services.read_passengers(db=db,user_in=user_in)

    return APIResponse(response)


@router.post('/register/passenger')
@cache(namespace=namespace, expire=ONE_DAY_IN_SECONDS)
async def create_passenger(
    user_in: schemas.PassengerCreate,
    name: str,
    age: int,
    nationa_id: int,
    db: AsyncSession = Depends(deps.get_db_async),
    _:models.User = Depends(deps.get_current_superuser_from_cookie)

)-> APIResponseType[schemas.PassengerResponse]:
    "Create the new passenger"
    response = await services.create_passenger(
        db=db,
        user_id=user_in,
        name=name,
        age=age,
        nationa_id=nationa_id
    )

    return APIResponse(response)
