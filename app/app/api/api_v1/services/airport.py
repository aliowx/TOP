from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app import exceptions as exc
from app import models, schemas
from app.utils import MessageCodes




async def read_airports(
    db: AsyncSession,
    skip: int,
    limit: int = 100,
)->schemas:
    airport = await crud.