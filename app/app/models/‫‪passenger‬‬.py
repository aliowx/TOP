from sqlalchemy import Boolean, Integer, String, Float
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.db.base_class import Base


class Passengers(Base):
    national_id = mapped_column(
        Integer, primary_key=True, autoincrement=True, index=True
    ) 
    age = mapped_column(Integer, index=True)
    gender = mapped_column(String, idnex=True)    
    name =  mapped_column(String, index=True)
