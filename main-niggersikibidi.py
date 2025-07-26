from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.db.connection import get_db   # <— ojo, aquí "backend.db"

app = FastAPI()

@app.get("/ping")
def ping(db: Session = Depends(get_db)):
    return {"pong": 1}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar los orígenes permitidos (en este caso, el frontend en Vue)
origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # o ["*"] para todos, pero no recomendado en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

