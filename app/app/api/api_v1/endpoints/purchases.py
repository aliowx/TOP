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
namespace = 'puechases'



@router.post('/')
@cache(namespace=namespace,expire=ONE_DAY_IN_SECONDS)

async def purchase_ticket(
    db:AsyncSession = Depends(deps.get_db_async),
    _: models.User = Depends(deps.get_current_superuser_from_cookie_or_basic),

    
)-> APIResponseType[schemas.TicketCreate]:
    pass