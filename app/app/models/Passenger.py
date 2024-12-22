from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from app.db.base_class import Base



class Passenger(Base):
    nationa_id: Mapped[int] = mapped_column(Integer, primary_key=True) 
    name: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String)
