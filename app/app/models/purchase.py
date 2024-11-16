from sqlalchemy import Column, Integer, String, ForeignKey
from app.db import Base
from sqlalchemy.orm import relationship

class Purchase(Base):
    __tablename__ = 'purchases'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    purchase_date = Column(String)
    total_amount = Column(Integer)

    user = relationship("User", back_populates="purchases")