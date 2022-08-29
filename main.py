from fastapi import FastAPI

from routes import router as TrackRouter

app = FastAPI()

app.include_router(TrackRouter, tags=["Track"], prefix="/track")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}