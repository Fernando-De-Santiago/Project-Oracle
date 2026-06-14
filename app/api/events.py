from fastapi import APIRouter, HTTPException, status, Depends
from services.event_service import get_events, search_event_by_id,create_event, delete_event_by_id, update_event_by_id
from models.api.events import EventCreate, EventUpdate,EventResponse, EventDelete
from sqlalchemy.orm import Session
from sqlalchemy import select
from db.session import get_db
from models.db.event import Events
router = APIRouter()

@router.get("/events",response_model=list[EventResponse])

def get_events_route(db: Session = Depends(get_db)):
    return get_events(db)

@router.get("/events/{id}",response_model=EventResponse)

def get_event_by_id(id:int,db: Session = Depends(get_db)):
    
    event = search_event_by_id(db,id)
    if event is None:
        raise HTTPException(status_code=404,detail="Event not found")
    return event

@router.post("/events",response_model=EventResponse,status_code=status.HTTP_201_CREATED)

def create_event_route(event:EventCreate,db: Session = Depends(get_db)):
    return create_event(db,event)

@router.delete("/events/{id}",response_model=EventDelete)

def delete_event(id: int,db: Session = Depends(get_db)):
    event = delete_event_by_id(db,id)
    if event is None:
        raise HTTPException(status_code=404,detail="Event not found")
    return {"message": f"Event {event.event_id} deleted\n"}


@router.put("/events/{id}", response_model=EventResponse)

def update_event(event:EventUpdate,id: int,db:Session = Depends(get_db)):
    updated_event = update_event_by_id(event,id,db)
    if updated_event is None:
        raise HTTPException(status_code=404, detail = "Event not found")
    return updated_event
