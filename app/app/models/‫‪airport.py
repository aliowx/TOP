from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.db.base_class import Base

class Airport(Base):
    
    __tablename__ = 'airports'
    
    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String, index=True)
    code = mapped_column(String, index=True) 
    city = mapped_column(String)
    country = mapped_column(String)