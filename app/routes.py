import os
from fastapi import APIRouter, UploadFile, File
from supabase import create_client

router = APIRouter(prefix="/api")

supabase = create_client(
    os.getenv("SUPABASE_URL",""),
    os.getenv("SUPABASE_KEY","")
)

@router.post("/register")
def register(email: str, password: str):
    result = supabase.auth.sign_up({
        "email": email,
        "password": password
    })
    return result.model_dump() if hasattr(result, "model_dump") else result

@router.post("/login")
def login(email: str, password: str):
    result = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })
    return result.model_dump() if hasattr(result, "model_dump") else result

@router.post("/snaps/send")
def send_snap(sender_id: str, receiver_id: str, media_url: str, caption: str=""):
    result = supabase.table("snaps").insert({
        "sender_id": sender_id,
        "receiver_id": receiver_id,
        "media_url": media_url,
        "caption": caption
    }).execute()
    return result.data

@router.get("/snaps/inbox/{user_id}")
def inbox(user_id: str):
    result = supabase.table("snaps").select("*").eq(
        "receiver_id", user_id
    ).execute()
    return result.data

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    data = await file.read()
    path = f"uploads/{file.filename}"
    result = supabase.storage.from_("media").upload(path, data)
    return {"path": path, "result": str(result)}
