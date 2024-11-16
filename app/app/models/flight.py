from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, mapped_column
from app.db.base_class import Base



class Flight(Base):
    
    __tablename__ = 'flights'

    id = mapped_column(Integer, primary_key=True, index=True)
    flight_code = mapped_column(String, index=True)  
    departure_time = mapped_column(DateTime) 
    arrival_time = mapped_column(DateTime)  
    origin_id = mapped_column(Integer, ForeignKey('airports.id'))  
    destination_id = mapped_column(Integer, ForeignKey('airports.id')) 

    origin = relationship('Airport', foreign_keys=[origin_id])
    destination = relationship('Airport', foreign_keys=[destination_id])