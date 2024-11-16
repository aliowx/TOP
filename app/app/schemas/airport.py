from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class AirportBase(BaseModel):
    origin: Optional[str] = None,
    destination: Optional[str] = None,
    date: Optional[datetime] = None,
    way: Optional[str] = None,
    specific_day: Optional[datetime] = None,

    class Config:
        orm_mode = True
        
        
class AirportCreate(AirportBase):
    pass

class AirportResponse(AirportBase):
    pass
class AirportDelet(AirportBase):
    pass

class AirportUpdate(AirportBase):
    pass