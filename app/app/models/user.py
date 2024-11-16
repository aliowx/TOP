from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship, mapped_column

from app.db.base_class import Base


class User(Base):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String, nullable=False)
    email = mapped_column(String, nullable=False)
    phone = mapped_column(String,nullable=False)

    purchases = relationship("Purchase", back_populates="user")
    passengers = relationship("Passenger", back_populates="user")