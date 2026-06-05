from fastapi import APIRouter

router = APIRouter()

@router.get("/events")
def get_event():
    return ['failed username','failed password']