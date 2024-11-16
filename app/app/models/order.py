from sqlalchemy import Boolean, Integer, String, Float
from sqlalchemy.orm import mapped_column, Mapped
from app.db.base_class import Base

class Order(Base):
    code: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    
    price: Mapped[float] = mapped_column(Float, index=True)
