from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas
from app.api import deps
from app.utils import APIResponse, APIResponseType
from app.api.api_v1 import services
from app.utils import APIResponseType
from cache import cache
from cache.util import ONE_DAY_IN_SECONDS, ONE_MONTH_IN_SECONDS  


router = APIRouter()
namespace = 'puechases'

@router.post('/purchase_ticket/')
@cache(namespace=namespace, expire=ONE_DAY_IN_SECONDS)

async def purchase_ticket(
    db: AsyncSession = Depends(deps.get_db_async),
    _: models.User = Depends(deps.get_current_superuser_from_cookie_or_basic),
    ticket_id: int = None,
    
)-> APIResponseType[schemas.TicketCreate]:
    
    response = await services.purchase_ticket(bd=db, ticket_id=ticket_id )
    return response


@router.get('/get_ticket/{id_ticket}')
@cache(namespace=namespace, expire=ONE_MONTH_IN_SECONDS)

async def get_ticket_id(
    db: AsyncSession = Depends(deps.get_db_async),
    _: models.User = Depends(deps.get_current_superuser_from_cookie_or_basic),
    ticket_id: int = None
) -> APIResponseType[schemas.TicketResponse]:

    response = await services.get_ticket_id()
    
    return APIResponse(response)