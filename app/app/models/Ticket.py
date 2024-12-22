from sqlalchemy import Boolean, Integer
from sqlalchemy.orm import mapped_column, Mapped

from app.db.base_class import Base


class ticket(Base):
    ticket_number: Mapped[int] = mapped_column(Integer,ForeignKey=True )


    