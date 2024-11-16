from sqlalchemy import Boolean, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from app.db.base_class import Base

class Order(Base):

    __tablename__ = 'orders'

    code = mapped_column(Integer, primary_key=True)
    price = mapped_column(Float, index=True)
    order_data = mapped_column(DateTime)
    user_id = mapped_column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates='orders')