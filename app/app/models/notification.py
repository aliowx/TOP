from sqlalchemy import Integer, ForeignKey, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base_class import Base

class Notifications(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    airport_code: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('airport.code', ondelete='SET NULL', onupdate='CASCADE'),
        nullable=True
    )
    airport_rel = relationship('airport', foreign_keys=airport_code)
    
    order_code: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            'order.id',ondelete='SET NULL', onupdate='CASCADE'
        ),
        nullable=True
    )
    order_rel = relationship('order', foreign_keys=order_code)
     
    is_read: Mapped[bool] = mapped_column(
        Boolean, default=False, index=True, nullable=True
    )
    text: Mapped[str] = mapped_column(String, nullable=True)
    
    type_notice: Mapped[str] = mapped_column(String, nullable=True)