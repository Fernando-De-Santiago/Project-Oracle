from fastapi import APIRouter
from services.event_service import get_events

router = APIRouter()

@router.get("/events")

def get_events_route():
    events=get_events()
    return events
