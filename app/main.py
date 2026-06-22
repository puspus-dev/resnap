from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="reSnap Supabase Backend")
app.include_router(router)

@app.get("/")
def root():
    return {"status":"reSnap Supabase backend online"}
