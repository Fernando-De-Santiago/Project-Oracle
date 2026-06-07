from fastapi import APIRouter
from services.event_service import get_events

router = APIRouter()

@router.get("/events")

def get_events():
    events=get_events()
    return events
