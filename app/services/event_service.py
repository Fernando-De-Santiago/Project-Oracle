from models.events import Event, EventType, EventCreate

events=[Event(event_id=1,event_type=EventType.LOGIN_FAILED,source="SERV-01",message="Failed login detected"),
    Event(event_id=2,event_type=EventType.LOGIN_SUCCESS,source="SERV-01",message="Login successful"),
    Event(event_id=3,event_type=EventType.SYSTEM_DOWN,source="SERV-01",message="System down check if powered on")]

def get_events():
    return events

def search_event_by_id(id: int):
    for i in events:
        if i.event_id==id:
            return i
    return None

def create_event(event_data: EventCreate):
    max_id=0
    for i in events:
        if i.event_id > max_id:
            max_id=i.event_id
    new_event= Event(event_id=max_id+1,event_type=event_data.event_type,source=event_data.source,message=event_data.message)
    events.append(new_event)
    return new_event

