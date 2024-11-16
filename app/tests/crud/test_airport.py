from sqlalchemy.ext.asyncio import AsyncSession
import pytest

from app import crud 
from app.schemas.airport import AirportCreate,AirportUpdate
from tests.utils.airport import  make_random_airport
@pytest.mark.asyncio
class TestAirport:
    async def test_get_airport(
            self,
            db: AsyncSession
    )-> None:
        airport_data = make_random_airport()

        pass