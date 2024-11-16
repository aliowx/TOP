from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship, mapped_column

from app.db.base_class import Base


class User(Base):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key=True)
    password = mapped_column(String,unique=True)
    name = mapped_column(String, nullable=False)
    email = mapped_column(String, nullable=False)
    phone = mapped_column(String,nullable=False)
    hashed_password = mapped_column(String, nullable=False)

    purchases = relationship("Purchase", back_populates="user")
    passengers = relationship("Passenger", back_populates="user")
    orders = relationship('Order', back_populates="user")