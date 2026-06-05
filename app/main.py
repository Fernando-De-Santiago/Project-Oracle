from fastapi import FastAPI
from api.events import router

app = FastAPI()
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello world"}