from fastapi import APIRouter, HTTPException
from services.event_service import get_events, search_event_by_id

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