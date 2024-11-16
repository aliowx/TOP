from pydantic import BaseModel
from typing import Optional


class PassengerCreate(BaseModel):
    age: int
    gender: str

    class Config:
        orm_mode = True


class PassengerResponse(BaseModel):
    national_id: int
    age: int
    gender: str

    class Config:
        orm_mode = True
        
        
class PassengerUpdate(BaseModel):
    age: Optional[int]
    gender: Optional[str]

    class Config:
        orm_mode = True
        
        
class PassengerDelet(BaseModel):
    age: Optional[int]
    gender: Optional[str]

    class Config:
        orm_mode = True