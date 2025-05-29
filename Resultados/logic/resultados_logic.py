"""Logic functions for managing 'Resultado' entities."""

from models.models import Resultado
from models.db import get_db
from models.schemas import ResultadoCreate, ResultadoRead
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from typing import List

db = get_db()

async def get_resultados(db: AsyncSession = db) :
    resultados = await db.execute(select(Resultado))
    list = resultados.scalars().all()
    return list

async def get_resultado(resultado_id: int, db: AsyncSession = db):
    resultado = await db.execute(select(Resultado).where(Resultado.id == resultado_id))
    resultado = resultado.scalar_one_or_none()
    if not resultado:
        raise HTTPException(status_code=404, detail="Resultado no encontrado")
    return resultado

async def create_resultado(resultado: ResultadoCreate, db: AsyncSession = db):
    nuevo_resultado = Resultado(**resultado.dict())
    db.add(nuevo_resultado)
    await db.commit()
    await db.refresh(nuevo_resultado)
    return nuevo_resultado

async def update_resultado(resultado_id: int, resultado: ResultadoCreate, db: AsyncSession = db):
    resultado_db = await db.execute(select(Resultado).where(Resultado.id == resultado_id))
    resultado_db = resultado_db.scalar_one_or_none()
    if not resultado_db:
        raise HTTPException(status_code=404, detail="Resultado no encontrado")
    
    for key, value in resultado.dict().items():
        setattr(resultado_db, key, value)
    
    await db.commit()
    await db.refresh(resultado_db)
    return resultado_db

async def delete_resultado(resultado_id: int, db: AsyncSession = db):
    resultado_db = await db.execute(select(Resultado).where(Resultado.id == resultado_id))
    resultado_db = resultado_db.scalar_one_or_none()
    if not resultado_db:
        raise HTTPException(status_code=404, detail="Resultado no encontrado")
    
    await db.delete(resultado_db)
    await db.commit()
    return {"detail": "Resultado eliminado exitosamente"}

async def get_resultados_by_evento(evento_id: int, db: AsyncSession = db):
    resultados = await db.execute(select(Resultado).where(Resultado.evento == evento_id))
    list = resultados.scalars().all()
    if not list:
        raise HTTPException(status_code=404, detail="No se encontraron resultados para el evento especificado")
    return list