from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from backend.db.connection import get_db  # Ojo que la ruta debe estar bien configurada

app = FastAPI()

# Configuración CORS para permitir peticiones desde el frontend (Vite)
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoints
@app.get("/ping")
def ping(db: Session = Depends(get_db)):
    return {"pong": 1}
