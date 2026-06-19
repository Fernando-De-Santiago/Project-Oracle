from pydantic import BaseModel
from datetime import datetime
from models.core.enums import EventType


class EventResponse(BaseModel):
    event_id: int
    created_at: datetime

    event_type: EventType
    source: str
    message: str | None = None

    model_config = {
        "from_attributes": True
    }


class EventCreate(BaseModel):
    event_type: EventType
    source: str
    message: str


class EventUpdate(BaseModel):
    event_type: EventType
    message: str


class EventDelete(BaseModel):
    message: str