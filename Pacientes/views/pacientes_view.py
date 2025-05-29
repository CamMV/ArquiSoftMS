from fastapi import APIRouter, status, Body
import logic.pacientes_logic as logic
from models.schemas import PacienteCreate, PacienteRead
from models.models import Paciente
from typing import List

router = APIRouter()
ENDPOINT_NAME = "/pacientes"

@router.get(
    "/",
    response_description="Lista de pacientes",
    response_model=List[PacienteRead],
    status_code=status.HTTP_200_OK,
)
async def get_places():
    return await logic.get_pacientes()


@router.get(
    "/{paciente_id}",
    response_description="Obtener un paciente por ID",
    response_model=PacienteRead,
    status_code=status.HTTP_200_OK,
)
async def get_paciente(paciente_id: int):
    return await logic.get_paciente(paciente_id=paciente_id)

@router.post(
    "/",
    response_description="Crear un nuevo paciente",
    response_model=PacienteRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_paciente(paciente: PacienteCreate = Body(...)):
    return await logic.create_paciente(paciente=paciente)

@router.put(
    "/{paciente_id}",
    response_description="Actualizar un paciente",
    response_model=PacienteRead,
    status_code=status.HTTP_200_OK,
)
async def update_paciente(paciente_id: int, paciente: PacienteCreate = Body(...)):
    return await logic.update_paciente(paciente_id=paciente_id, paciente=paciente)

@router.delete(
    "/{paciente_id}",
    response_description="Eliminar un paciente",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_paciente(paciente_id: int):
    await logic.delete_paciente(paciente_id=paciente_id)
    return {"detail": "Paciente eliminado exitosamente"}