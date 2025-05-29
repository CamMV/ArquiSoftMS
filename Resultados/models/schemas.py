from pydantic import BaseModel
from enum import Enum

    
class ResultadoCreate(BaseModel):
    evento : int
    valor: str
    recomendacion: str 
    fecha_generacion: str
    
class ResultadoRead(ResultadoCreate):
    id: int
    
    class Config:
        orm_mode = True  # Permite que Pydantic lea los datos de los modelos de SQLAlchemy