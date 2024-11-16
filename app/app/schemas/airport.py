from pydantic import BaseModel

class AirportBase(BaseModel):
    name: str
    code: str

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