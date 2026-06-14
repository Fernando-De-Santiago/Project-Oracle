from models.api.events import EventResponse, EventCreate, EventUpdate
from models.core.enums import EventType
from datetime import datetime, UTC
from sqlalchemy import select, inspect
from sqlalchemy.orm import Session
from models.db.event import Events


def get_events(db: Session):
    result= db.execute(select(Events)).scalars().all()
    return result

def search_event_by_id(db:Session,id: int):
    event=db.get(Events,id)
    if event is None:
        return None
    return event

def create_event(db:Session,event_data: EventCreate):
    new_event= Events(event_type=event_data.event_type,source=event_data.source,message=event_data.message,created_at=datetime.now(UTC))
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

def delete_event_by_id(db:Session,id:int):
    deleted_event=db.get(Events,id)
    if deleted_event is None:
        return None
    db.delete(deleted_event)
    db.commit()
    return deleted_event

def update_event_by_id(event_data: EventUpdate,event_id: int, db : Session):
    update_event = db.get(Events,event_id)
    if update_event is None:
        return None
    update_event.event_type = event_data.event_type
    update_event.message=event_data.message
    db.commit()
    db.refresh(update_event)
    return update_event
