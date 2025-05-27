from sqlalchemy import Column, Integer, String, Enum as SQLEnum
from sqlalchemy.orm import declarative_base
from enum import Enum

class CiudadEnum(str, Enum):
    BOGOTA = "Bogotá"
    MEDELLIN = "Medellín"
    CALI = "Cali"
    

Base = declarative_base()

class Paciente(Base):
    __tablename__ = 'pacientes'
    
    id = Column(Integer,primary_key=True, autoincrement=True, index=True)
    nombre = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    ciudad = Column(SQLEnum(CiudadEnum), nullable=False)
    