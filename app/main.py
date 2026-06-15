from fastapi import FastAPI
from api.events import router as r1
from api.user import router as r2

app = FastAPI()
app.include_router(r1)
app.include_router(r2)


@app.get("/")
async def root():
    return {"message": "Hello world"}