import pytest
from httpx import AsyncClient 
from datetime import datetime
from app.core.config import settings

@pytest.mark.asyncio
class TestAirport:
    origin: str = 'Imam Khomeini Airoport',
    destination: str = "germany",
    date: datetime = datetime(2024,11,15)
    way: str = 'oneway',
    specific_day: datetime = datetime(2024,11,15)

    @property
    def data(self):
        return {
            'origin': TestAirport.origin,
            'destination': TestAirport.destination,
            'date': TestAirport.date.isocalendar(),
            'way': TestAirport.way,
            'specific_day': TestAirport.specific_day.isocalendar()
        }

    async def test_register_input(
            self,
            client: AsyncClient
    )-> None:
        # normal register
        response = await client.post(
            f"{settings.API_V1_STR}/",
            json=self.data
        )
        assert response.status_code == 200

        # duplicate register
        response = await client.post(
            f"{settings.API_V1_STR}/",
            json=self.data
        )
        assert response.status_code == 409

    async def test_multiplt_requests(self, client: AsyncClient):
        
        for i in range(10):
            response = await client.post(
                f'{settings.API_V1_STR}/',
                json=self.data
            )
            
            try:
                assert response.status_code == 200
                
            except:                
                assert response.status_code == 404

    async def test_missing_data(
            slef,
            client: AsyncClient
    ):
        response = await client.get(f'{settings.API_V1_STR}/')
        assert response.status_code == 400

    async def test_get_registered_flights(self, client: AsyncClient):

        response = await client.post(
            f"{settings.API_V1_STR}/",
            json=self.data
        )

        assert response.status_code == 200
        response = await client.get(f"{settings.API_V1_STR}/flights")
        assert response.status_code == 200
        flights = response.json()

        assert isinstance(flights, list)
        assert len(flights) > 0
        first_flight = flights[0]

        assert first_flight['origin'] == self.data['origin']
        assert first_flight['destination'] == self.data['destination']
        assert first_flight['date'] == self.data['date']
        assert first_flight['way'] == self.data['way']
        assert first_flight['specific_day'] == self.data['specific_day']