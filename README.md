# reSnap Supabase Backend

Features:
- Supabase Auth
- PostgreSQL tables
- Storage uploads
- Snaps API
- Message-ready database

Setup:
1. Create Supabase project
2. Run schema.sql in SQL editor
3. Create a Storage bucket called:

media

4. Add environment variables:

SUPABASE_URL=your_url
SUPABASE_KEY=your_key

Run:

pip install -r requirements.txt

uvicorn app.main:app --reload

Deploy anywhere:
- Render
- Fly.io
- VPS
