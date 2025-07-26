from pydantic import BaseModel
from typing import Optional
from datetime import date

class EmpleadoCreate(BaseModel):
    nombre: str
    rut: str
    correo_trabajador: Optional[str]
    fecha_nacimiento: date
    estado_civil_id: int