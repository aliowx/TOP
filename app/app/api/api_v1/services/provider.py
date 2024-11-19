from abc import ABC, abstractmethod
from app import exceptions as exc
import httpx
from datetime import datetime
import asyncio
import logging



logger = logging.getLogger(__name__)


class FlightProvider(ABC):
    @abstractmethod
    def search_flights(self, route: str, origin: str, destination: str, date: datetime, way: str, specific_day: datetime):
        pass

    @abstractmethod
    def purchase_ticket(self, flight_id: str):
        pass


class BaseProvider(FlightProvider):
    BASE_URL = ''
    
    async def Make_requst(self, endpoint:str, params:dict):
        async with httpx.AsyncClient(timeout=11) as client:
            try:
                response = await client.get(f'{self.BASE_URL}{endpoint}', params=params)
                response.raise_for_status()
                
            except httpx.HTTPStatusError as e:
                logger.error(f'Http error {self.BASE_URL} : {e}')
                raise 
            


class providerA(BaseProvider):
    async def search_flights(
        self, 
        route: str,
        origin:str,
        destination: str,
        date: datetime,
        way: str,
        specific_day: datetime
    ):
        async with httpx.AsyncClient() as client:
            response = await client.get('')
            try:
                if response.status_code == 200:
                    return response.json()
            
            except ConnectionError as e:
                logger.error(f'Error conecting to {str(e)}')    
        
    async def purchase_ticket(self, flight_id: int):
        async with httpx.AsyncClient() as clinet:
            response = await clinet.get('')
            try:
                if response.status_code ==200:
                    return response.json()
                
            except ConnectionError as e:
                logger.error(f'Error conecting to {str(e)}')

    
class providerB(BaseProvider):
    async def search_flights(
        self, 
        route: str,
        origin:str,
        destination: str,
        date: datetime,
        way: str,
        specific_day: datetime
    ):
        async with httpx.AsyncClient() as client:
            response = await client.get('')
            try:
                if response.status_code == 200:
                    return response.json()
            
            except ConnectionError as e:
                print(f'Error connecting to provider: {str(e)}')
                    
    async def purchase_ticket(self, flight_id: int):
        async with httpx.AsyncClient() as clinet:
            response = await clinet.get('')
            try:
                
                if response.status_code ==200:
                    return response.json()
                
            except ConnectionError as c:
                print('try again latter to buy ticket')
    

class FlightService:
    
    def __init__(self, providers: list[FlightProvider]):
        self.providers = providers
    
        
    async def search_all_flights(
        self, 
        route: str,
        origin:str,
        destination: str,
        date: datetime,
        way: str,
        specific_day: datetime
    ):

        tasks = []
            
            
        for provider in self.providers:
            tasks.append(
                asyncio.create_task(
                provider.search_flights(route, origin, destination, date, way, specific_day)
                )
            )
            
        flight_results = []
        
        for task in asyncio.as_completed(tasks):
            
            try:
                
                result = await task
                flight_results.append(result)
                
            except  Exception as e:
                logger.error(f'There is a fetching error: {e}')
        
        return flight_results
    
    
    async def purchase_ticket(self,flight_id: int, provider_name: str):
        
        provider = next(
            (p for p in self.providers if provider_name.lower() in p.__class__.__name__.lower())
        ) 
        if not provider:
            raise exc.NotFoundException(
                detail=(f'provider {provider_name} not found')
            )
        return provider.purchase_ticket(flight_id=flight_id)
    
    