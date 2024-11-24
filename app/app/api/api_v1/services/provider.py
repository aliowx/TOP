"""
this is a Provider about the  get the ticket 
"""
from abc import ABC, abstractmethod
from app import exceptions as exc
import httpx
from datetime import datetime
import asyncio
import logging
from tenacity import retry, wait_exponential, stop_after_attempt


logger = logging.getLogger(__name__)


class FlightProvider(ABC):
    @abstractmethod
    def search_flights(self, route: str, origin: str, destination: str, date: datetime, way: str, specific_day: datetime):
        pass

    @abstractmethod
    def purchase_ticket(self, flight_id: str):
        pass


class ProviderException(Exception):
    pass

class FlightNotFoundException(Exception):
    pass

class TicketPurchaseException(Exception):
    pass




class BaseProvider(FlightProvider):
    
    BASE_URL = ''
    
    @retry(wait=wait_exponential(multiplier=1), stop=stop_after_attempt(3))
    async def Make_requst(self, endpoint:str, params:dict):
        async with httpx.AsyncClient(timeout=11) as client:
            try:
                response = await client.get(f'{self.BASE_URL}{endpoint}', params=params)
                response.raise_for_status()
            except httpx.HTTPStatusError as e:
                logger.error(f'Http error {self.BASE_URL} : {e}')
                raise ProviderException(f'HTTP error:{e.response.status_code}')
            except httpx.ConnectTimeout:
                logger.error(f'Timeout connecting to {self.BASE_URL}')
                raise ProviderException('Connection timeout!')
            except httpx.ReadError as ea:
                logger.error(f'Error during requst to {self.BASE_URL}: {str(ea)}')
                            


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
        params = {
            "route": route,
            "origin": origin,
            "destination": destination,
            "date": date.strftime("%Y-%m-%d"),
            "way": way,
            "specific_day": specific_day.strftime("%Y-%m-%d"),
        }
        return  await self.Make_requst('/search', params)

        
    async def purchase_ticket(self, flight_id:int):
        params = {"flight_id": flight_id}
        return await self.Make_requst("/purchase", params)
        
    
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
        params = {
            "route": route,
            "origin": origin,
            "destination": destination,
            "date": date.strftime("%Y-%m-%d"),
            "way": way,
            "specific_day": specific_day.strftime("%Y-%m-%d"),
        }
        return  await self.Make_requst('/search', params)

        
    async def purchase_ticket(self, flight_id:int):
        params = {"flight_id": flight_id}
        return await self.Make_requst("/purchase", params)

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
        errors = []
        
        for task in asyncio.as_completed(tasks):
            
            try:
                
                result = await task
                flight_results.append(result)
                
            except  Exception as e:
                logger.error(f'There is a fetching error: {e}')
                errors.append(str(e))
        
        if not flight_results:    
            logger.error('')
        
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
    
    