from sqlalchemy import Integer, String, ForeignKey, DateTime
from app.db import Base
from sqlalchemy.orm import relationship, mapped_column
from datetime import datetime

class Purchase(Base):
    __tablename__ = 'purchases'
    id = mapped_column(Integer, primary_key=True, index=True)
    user_id = mapped_column(Integer, ForeignKey('users.id'))
    purchase_date = mapped_column(DateTime, default=datetime)
    items = mapped_column(String)  
    status = mapped_column(String)

    user = relationship("User", back_populates="purchases")
    tickets = relationship("Ticket", back_populates="purchase")
