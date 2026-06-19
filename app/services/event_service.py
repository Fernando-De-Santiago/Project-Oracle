from sqlalchemy import select
from sqlalchemy.orm import Session
from models.db.event import Events
from models.schemas.events import EventCreate, EventUpdate


def get_events(db: Session):
    return db.execute(select(Events)).scalars().all()


def search_event_by_id(db: Session, id: int):
    return db.get(Events, id)


def create_event(db: Session, event_data: EventCreate):
    new_event = Events(
        event_type=event_data.event_type,
        source=event_data.source,
        message=event_data.message
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return new_event


def delete_event_by_id(db: Session, id: int):
    event = db.get(Events, id)

    if not event:
        return None

    db.delete(event)
    db.commit()

    return event


def update_event_by_id(db: Session, event_id: int, event_data: EventUpdate):
    event = db.get(Events, event_id)

    if not event:
        return None

    event.event_type = event_data.event_type
    event.message = event_data.message

    db.commit()
    db.refresh(event)

    return event