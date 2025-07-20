from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.db.connection import get_db   # <— ojo, aquí "backend.db"

app = FastAPI()

@app.get("/ping")
def ping(db: Session = Depends(get_db)):
    return {"pong": 1}
