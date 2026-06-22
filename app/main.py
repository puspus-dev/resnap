from fastapi import FastAPI
from .routes import router

app = FastAPI(title="reSnap API")

app.include_router(router)

@app.get("/")
def root():
    return {"status": "reSnap backend online"}
