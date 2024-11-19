from sqlalchemy import Integer, String,DateTime
from sqlalchemy.orm import mapped_column, relationship
from app.db.base_class import Base


class Airport(Base):
    __tablename__ = 'airports'
    
    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String, index=True)
    code = mapped_column(String, index=True) 
    city = mapped_column(String)
    origin = mapped_column(String)
    destination = mapped_column(String)
    date = mapped_column(DateTime)
    way = mapped_column(String)
    specific_day = mapped_column(DateTime)
