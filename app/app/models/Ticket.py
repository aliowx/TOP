from sqlalchemy import Boolean, Integer,ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.db.base_class import Base


class ticket(Base):
    ticket_number: Mapped[int] = mapped_column(Integer, primary_key=True,index=True)

    passenger_id : Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            'Passenger.nationa_id',ondelete='SET NULL', onupdate='CASCADE'
        ),
        nullable=True
    ) 
    passenger_rel = relationship('Passenger', foreign_keys=passenger_id)
    