from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base_class import Base

class order(Base):
    code: Mapped[int] = mapped_column(Integer, primary_key=True)
    price: Mapped[str] = mapped_column(String)