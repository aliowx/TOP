from sqlalchemy import Boolean, Integer, String, Float, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.db.base_class import Base


class Passenger(Base):
    __tablename__ = 'passenger'

    national_id = mapped_column(Integer, primary_key=True,)
    age = mapped_column(Integer, index=True)
    gender = mapped_column(String, idnex=True)    
    name =  mapped_column(String, index=True)
    user_id = mapped_column(Integer, ForeignKey('users.id'), nullable=True)

    user = relationship("User", back_populates="passenger")

    tickets = relationship("Ticket", back_populates="passenger")
    