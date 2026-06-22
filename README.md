# reSnap Backend

Simple FastAPI backend starter.

Run locally:

pip install -r requirements.txt

uvicorn app.main:app --reload

API:
GET /
POST /api/register
POST /api/login
POST /api/snaps/send
GET /api/snaps/inbox

For Railway:
- create a new service
- deploy this repo
- start command:

uvicorn app.main:app --host 0.0.0.0 --port $PORT
