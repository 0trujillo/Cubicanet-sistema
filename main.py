from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
<<<<<<< HEAD
from backend.db.connection import get_db   # <— ojo, aquí "backend.db"
from backend.schemas.empleados import EmpleadoCreate  # ← con punto   # ✅ <--- ESTA LÍNEA
from backend.crud.empleados import crear_empleado  
from backend.schemas.empleados import EmpleadoCreate
=======
from fastapi.middleware.cors import CORSMiddleware
from backend.db.connection import get_db  # Ojo que la ruta debe estar bien configurada

>>>>>>> yojansel-nueva
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

@app.post("/empleados")
def crear_nuevo_empleado(empleado: EmpleadoCreate, db: Session = Depends(get_db)):
    return crear_empleado(db, empleado)