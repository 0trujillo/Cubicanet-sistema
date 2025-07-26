from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.db.connection import get_db   # <— ojo, aquí "backend.db"
from backend.schemas.empleados import EmpleadoCreate  # ← con punto   # ✅ <--- ESTA LÍNEA
from backend.crud.empleados import crear_empleado  
from backend.schemas.empleados import EmpleadoCreate
app = FastAPI()

@app.get("/ping")
def ping(db: Session = Depends(get_db)):
    return {"pong": 1}

@app.post("/empleados")
def crear_nuevo_empleado(empleado: EmpleadoCreate, db: Session = Depends(get_db)):
    return crear_empleado(db, empleado)