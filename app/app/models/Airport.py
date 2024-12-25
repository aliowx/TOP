from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from app.db.base_class import Base


class airport(Base):
    name: Mapped[str] = mapped_column(String)
    code: Mapped[int] = mapped_column(Integer,primary_key=True)

    