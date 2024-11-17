from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas
from app.api import deps
from app.utils import APIResponse, APIResponseType
from app.api.api_v1 import services
from app.utils import APIResponseType
from cache import cache
from cache.util import ONE_DAY_IN_SECONDS 
from app.api.api_v1.services import provider_A, provider_B, FlightService


router = APIRouter()
namespace = 'puechases'


providers = [provider_A,provider_B]

flight_service = FlightService(providers)

@router.post('/purchase_ticket/')
@cache(namespace=namespace, expire=ONE_DAY_IN_SECONDS)

async def purchase_ticket(
    db: AsyncSession = Depends(deps.get_db_async),
    _: models.User = Depends(deps.get_current_superuser_from_cookie_or_basic),
    flight_id: int = None,
    
)-> APIResponseType[schemas.TicketCreate]:
    
    response = await flight_service.purchase_ticket(flight_id=flight_id,)
    return APIResponse(response)

