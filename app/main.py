from fastapi import FastAPI
from api.events import router as events_router
from api.user import router as user_router

app = FastAPI(
    title="Project Oracle",
    description="Event-driven backend system with authentication and logging",
    version="1.0.0"
)

app.include_router(user_router, prefix="/api/v1/users", tags=["Users"])
app.include_router(events_router, prefix="/api/v1/events", tags=["Events"])

@app.get("/")
def root():
    return {"message": "Project Oracle API running"}