from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import declarative_base
from datetime import datetime, UTC
from models.core.enums import EventType


Base = declarative_base()

class Events(Base):
    __tablename__ = "events"
    event_id = Column(Integer, primary_key= True, index=True)
    created_at = Column(DateTime, nullable=False)
    event_type = Column(String(50),nullable= False)
    source = Column(String, nullable= False)
    message = Column(String,nullable= True)
