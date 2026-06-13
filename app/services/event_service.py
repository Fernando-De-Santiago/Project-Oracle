from models.api.events import EventResponse, EventCreate, EventUpdate
from models.core.enums import EventType
from datetime import datetime, UTC
from sqlalchemy import select, inspect
from sqlalchemy.orm import Session
from models.db.event import Events
events=[EventResponse(event_id=1,event_type=EventType.LOGIN_FAILED,source="SERV-01",message="Failed login detected",created_at=datetime.now()),
    EventResponse(event_id=2,event_type=EventType.LOGIN_SUCCESS,source="SERV-01",message="Login successful",created_at=datetime.now()),
    EventResponse(event_id=3,event_type=EventType.SYSTEM_DOWN,source="SERV-01",message="System down check if powered on",created_at=datetime.now())]

def get_events(db: Session):
    result= db.execute(select(Events)).scalars().all()
    return result

def search_event_by_id(id: int):
    for i in events:
        if i.event_id==id:
            return i
    return None

def create_event(db:Session,event_data: EventCreate):
    new_event= Events(event_type=event_data.event_type,source=event_data.source,message=event_data.message,created_at=datetime.now(UTC))
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

def delete_event_by_id(id:int):
    for event in events:
        if event.event_id == id:
            events.remove(event)
            return event
    return None

def update_event_by_id(event_data: EventUpdate,event_id: int):
    for event in events:
        if event.event_id == event_id:
            event.event_type=event_data.event_type
            event.message=event_data.message
            return event
    return None
