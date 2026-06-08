from fastapi import APIRouter, HTTPException, status
from services.event_service import get_events, search_event_by_id,create_event
from models.events import EventCreate

router = APIRouter()

@router.get("/events")

def get_events_route():
    events=get_events()
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