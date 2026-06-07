from models.events import Event, EventType

def get_events():
    event_1 = Event(event_id=1,event_type=EventType.LOGIN_FAILED,source="SERV-01",message="Failed login detected")

    event_2 = Event(event_id=2,event_type=EventType.LOGIN_SUCCESS,source="SERV-01",message="Login successful")

    event_3 = Event(event_id=3,event_type=EventType.SYSTEM_DOWN,source="SERV-01",message="System down check if powered on")
    return[event_1,event_2,event_3]

def get_event_by_id(id):
    events=get_events()
    for i in events:
        if i.event_id==id:
            return i
    return None

