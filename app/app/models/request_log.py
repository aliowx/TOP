from sqlalchemy import Integer, String, Text, Float
from sqlalchemy.orm import mapped_column, relationship

from app.db.base_class import Base


class RequestLog(Base):

    __tablename__ = 'requestlog'

    id =  mapped_column(Integer, primary_key=True)

    user_id = mapped_column(String(50))
    method = mapped_column(String(10))
    service_name = mapped_column(Text)
    processing_time = mapped_column(Float)
    tracker_id= mapped_column(String(100))
    ip = mapped_column(String(50))
    request = mapped_column(Text)
    response = mapped_column(Text)
    trace = mapped_column(Text, default="")
