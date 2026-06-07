from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class EventType(str, Enum):
    LOGIN_SUCCESS = "LOGIN_SUCCESS"
    LOGIN_FAILED = "LOGIN_FAILED"
    SYSTEM_DOWN = "SYSTEM_DOWN"
    HIGH_CPU_USAGE = "HIGH_CPU_USAGE"
    PORT_SCAN_DETECTED = "PORT_SCAN_DETECTED"
    UNAUTHORIZED_ACCESS = "UNAUTHORIZED_ACCESS"

class Event(BaseModel):
    event_id: int
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    event_type: EventType
    source: str

    message: str

    username: Optional[str] = None
    ip_address: Optional[str] = None
    hostname: Optional[str] = None
    service_name: Optional[str] = None
    error_code: Optional[str] = None
    authentication_reason: Optional[str] = None