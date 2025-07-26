# backend/db/models.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Empleado(Base):
    __tablename__ = "empleados"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)
    rut = Column(String(12), unique=True, nullable=False)
    correo_trabajador = Column(String, unique=True)
    fecha_nacimiento = Column(Date, nullable=False)
    estado_civil_id = Column(Integer, ForeignKey("estados_civil.id"))
