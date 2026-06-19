from sqlalchemy import Column, Integer, String, DateTime, Enum, func
from models.core.enums import EventType
from db.base import Base


class Events(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True, index=True)

    created_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    event_type = Column(Enum(EventType), nullable=False)

    source = Column(String, nullable=False)

    message = Column(String, nullable=True)