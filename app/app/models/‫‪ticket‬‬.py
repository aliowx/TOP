from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.db import Base

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    purchase_id = Column(Integer, ForeignKey('purchases.id'))
    passenger_id = Column(Integer, ForeignKey('passengers.id'))
    ticket_code = Column(String, unique=True, nullable=False)
    departure_time = Column(String)
    arrival_time = Column(String)
    status = Column(String, default='issued')

    purchase = relationship("Purchase", back_populates="tickets")
    passenger = relationship("Passenger", back_populates="tickets")
