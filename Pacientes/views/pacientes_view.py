from fastapi import APIRouter, status, Body, Depends
import logic.pacientes_logic as logic
from models.schemas import PacienteCreate, PacienteRead
from pathlib import Path
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from models.db import get_db
from fastapi.responses import HTMLResponse

router = APIRouter()
TEMPLATES_DIR = Path(__file__).parent.parent / "templates"

@router.get(
    "/home",
    response_description="Página de inicio de Pacientes",
    status_code=status.HTTP_200_OK,
    response_class=HTMLResponse,
)
async def home():
    html_file = TEMPLATES_DIR / "home.html"
    return HTMLResponse(html_file.read_text(), status_code=status.HTTP_200_OK)


@router.get(
    "/pacientes",
    response_description="Lista de pacientes",
    response_model=List[PacienteRead],
    status_code=status.HTTP_200_OK,
)
async def get_pacientes(db: AsyncSession = Depends(get_db)):
    return await logic.get_pacientes(db)


@router.get(
    "/pacientes/{paciente_id}",
    response_description="Obtener un paciente por ID",
    response_model=PacienteRead,
    status_code=status.HTTP_200_OK,
)
async def get_paciente(paciente_id: int, db: AsyncSession = Depends(get_db)):
    return await logic.get_paciente(paciente_id=paciente_id, db=db)

@router.post(
    "/pacientes",
    response_description="Crear un nuevo paciente",
    response_model=PacienteRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_paciente(paciente: PacienteCreate = Body(...), db: AsyncSession = Depends(get_db)):
    return await logic.create_paciente(paciente=paciente, db=db)

@router.put(
    "/pacientes/{paciente_id}",
    response_description="Actualizar un paciente",
    response_model=PacienteRead,
    status_code=status.HTTP_200_OK,
)
async def update_paciente(paciente_id: int, paciente: PacienteCreate = Body(...), db: AsyncSession = Depends(get_db)):
    return await logic.update_paciente(paciente_id=paciente_id, paciente=paciente, db=db)

@router.delete(
    "/pacientes/{paciente_id}",
    response_description="Eliminar un paciente",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_paciente(paciente_id: int, db: AsyncSession = Depends(get_db)):
    await logic.delete_paciente(paciente_id=paciente_id, db=db)
    return {"detail": "Paciente eliminado exitosamente"}