from sqlalchemy import Column, Integer, String, Enum as SQLEnum
from sqlalchemy.orm import declarative_base
from enum import Enum

Base = declarative_base()

class Resultado(Base):
    
    id = Column(Integer, primary_key=True, index=True)
    evento = Column(Integer, nullable=False)
    valor = Column(String, nullable=False)
    recomendacion = Column(String, nullable=True)
    fecha_generacion = Column(String, nullable=False)
    