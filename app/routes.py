from fastapi import APIRouter

router = APIRouter(prefix="/api")

users = {}
snaps = []

@router.post("/register")
def register(username: str, email: str, password: str):
    users[username] = {
        "email": email,
        "password": password
    }
    return {"created": True, "username": username}

@router.post("/login")
def login(username: str, password: str):
    if username in users and users[username]["password"] == password:
        return {"token": "demo-token", "username": username}
    return {"error": "invalid login"}

@router.get("/me")
def me(username: str):
    return users.get(username, {})

@router.post("/snaps/send")
def send_snap(sender: str, receiver: str, media_url: str, caption: str = ""):
    snap = {
        "sender": sender,
        "receiver": receiver,
        "media_url": media_url,
        "caption": caption,
        "opened": False
    }
    snaps.append(snap)
    return snap

@router.get("/snaps/inbox")
def inbox(username: str):
    return [s for s in snaps if s["receiver"] == username]

@router.post("/snaps/open")
def open_snap(index: int):
    snaps[index]["opened"] = True
    return snaps[index]
