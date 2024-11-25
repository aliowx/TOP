from pydantic import BaseModel
from typing import Optional



class OrderBase(BaseModel):
    price: float
    
    
class OrderCreate(OrderBase):
    code: Optional[int] = None 
    


class OrderUpdate(OrderBase):
    price: Optional[float] = None 
    
class Order(OrderBase):
    code: int

    class Config:
        orm_mode = True 



class OrderDelet(Order):
    pass