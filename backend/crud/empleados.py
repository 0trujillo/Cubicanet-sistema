from sqlalchemy.orm import Session
from backend.schemas.empleados import EmpleadoCreate
from backend.db.models import Empleado

def crear_empleado(db: Session, empleado: EmpleadoCreate):
    db_empleado = Empleado(**empleado.dict())
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado