from sqlalchemy import Integer, String, ForeignKey, Float
from sqlalchemy.orm import mapped_column, relationship
from app.db import Base

class Ticket(Base):
    
    __tablename__ = 'tickets'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    purchase_id = mapped_column(Integer, ForeignKey('purchases.id'))
    order_id = mapped_column(Integer, ForeignKey('orders.code')) 
    price = mapped_column(Float)
    airline = mapped_column(String)
    passenger_id = mapped_column(Integer, ForeignKey('passengers.id'))
    ticket_code = mapped_column(String, unique=True, nullable=False)
    departure_time = mapped_column(String)
    arrival_time = mapped_column(String)
    status = mapped_column(String, default='issued')

    passenger = relationship("Passenger", back_populates="tickets")
    order = relationship("Order", back_populates="tickets")
