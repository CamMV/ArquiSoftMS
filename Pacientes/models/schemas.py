from pydantic import BaseModel
from enum import Enum

class CiudadEnum(str, Enum):
    BOGOTA = "Bogotá"
    MEDELLIN = "Medellín"
    CALI = "Cali"
    
class PacienteCreate(BaseModel):
    nombre: str
    edad: int
    ciudad: CiudadEnum
    
class PacienteRead(PacienteCreate):
    id: int
    
    class Config:
        orm_mode = True  # Permite que Pydantic lea los datos de los modelos de SQLAlchemy