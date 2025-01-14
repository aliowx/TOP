from sqlalchemy import Integer, ForeignKey, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base_class import Base

class Bot(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    
    description: Mapped[str] = mapped_column(String, nullable=True)
    
    owner_id: Mapped[int] = relationship('user', back_populates='bot')
    
    
    