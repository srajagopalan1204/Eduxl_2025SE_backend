from fastapi import FastAPI, Depends
from sqlalchemy import text
from db import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check():
    """Simple check to see if the app is running."""
    return {"status": "ok"}

@app.get("/db-check")
def db_check(db=Depends(get_db)):
    """
    Simple check to see if we can reach the database.
    It runs SELECT 1 and returns db_ok: true/false.
    """
    result = db.execute(text("SELECT 1")).scalar()
    return {"db_ok": bool(result)}
