from  models.models import Paciente
from  models.db import get_db
from  models.schemas import PacienteCreate
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, Depends
from typing import List


async def get_pacientes(db: AsyncSession ) :
    pacientes = await db.execute(select(Paciente))
    list = pacientes.scalars().all()
    return list

async def get_paciente(paciente_id: int, db: AsyncSession = db):
    paciente = await db.execute(select(Paciente).where(Paciente.id == paciente_id))
    paciente = paciente.scalar_one_or_none()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

async def create_paciente(paciente: PacienteCreate, db: AsyncSession = db):
    nuevo_paciente = Paciente(**paciente.dict())
    db.add(nuevo_paciente)
    await db.commit()
    await db.refresh(nuevo_paciente)
    return nuevo_paciente

async def update_paciente(paciente_id: int, paciente: PacienteCreate, db: AsyncSession = db):
    paciente_db = await db.execute(select(Paciente).where(Paciente.id == paciente_id))
    paciente_db = paciente_db.scalar_one_or_none()
    if not paciente_db:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    
    for key, value in paciente.dict().items():
        setattr(paciente_db, key, value)
    
    await db.commit()
    await db.refresh(paciente_db)
    return paciente_db

async def delete_paciente(paciente_id: int, db: AsyncSession = db):
    paciente_db = await db.execute(select(Paciente).where(Paciente.id == paciente_id))
    paciente_db = paciente_db.scalar_one_or_none()
    if not paciente_db:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    
    await db.delete(paciente_db)
    await db.commit()
    return {"detail": "Paciente eliminado exitosamente"}