from pydantic import BaseModel
from datetime import datetime

class FlightSearchRequest(BaseModel):
    origin_code: str
    destination_code: str
    date: datetime

    class Config:
        orm_mode = True
        
        
        
class FlightCreate(BaseModel):
    origin_code: str
    destination_code: str
    date: datetime

    class Config:
        orm_mode = True
        
        
class FlightUpdate(BaseModel):
    origin_code: str
    destination_code: str
    date: datetime

    class Config:
        orm_mode = True        