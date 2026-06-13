from fastapi import APIRouter, HTTPException, status, Depends
from services.event_service import get_events, search_event_by_id,create_event, delete_event_by_id, update_event_by_id
from models.api.events import EventCreate, EventUpdate,EventResponse
from sqlalchemy.orm import Session
from sqlalchemy import select
from db.session import get_db
from models.db.event import Events
router = APIRouter()

@router.get("/events",response_model=list[EventResponse])

def get_events_route(db: Session = Depends(get_db)):
    events=db.scalars(select(Events)).all()
    return events

@router.get("/events/{id}")

def get_event_by_id(id: int):
    
    event = search_event_by_id(id)
    if event == None:
        raise HTTPException(status_code=404,detail="Event not found")
    return event

@router.post("/events",status_code=status.HTTP_201_CREATED)

def create_event_route(event: EventCreate):
    new_event=create_event(event)
    return new_event

@router.delete("/events/{id}",status_code=status.HTTP_200_OK)

def delete_event(id: int):
    event = delete_event_by_id(id)
    if event==None:
        raise HTTPException(status_code=404,detail="Event not found")
    return {"message": f"Event {event.event_id} deleted\n",
            "message": f"{event}"}

@router.put("/events/{id}", status_code=status.HTTP_200_OK)

def update_event(event:EventUpdate,id: int):
    updated_event = update_event_by_id(event,id)
    if updated_event == None:
        raise HTTPException(status_code=404, detail = "Event not found")
    return updated_event
