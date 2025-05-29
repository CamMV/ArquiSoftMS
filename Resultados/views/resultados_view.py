from fastapi import APIRouter, status, Body
import Resultados.logic.resultados_logic as logic
from models.schemas import ResultadoRead, ResultadoCreate
from models.models import Resultado

router = APIRouter()
ENDPOINT_NAME = "/resultados"

@router.get(
    "/",
    response_description="Lista de resultados",
    response_model=list[ResultadoRead],
    status_code=status.HTTP_200_OK,
)
async def get_resultados():
    return await logic.get_resultados()


@router.get(
    "/{resultado_id}",
    response_description="Obtener un resultado por ID",
    response_model=ResultadoRead,
    status_code=status.HTTP_200_OK,
)
async def get_resultado(resultado_id: int):
    return await logic.get_resultado(resultado_id=resultado_id)

@router.post(
    "/",
    response_description="Crear un nuevo paciente",
    response_model=ResultadoRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_resultado(resultado: ResultadoCreate = Body(...)):
    return await logic.create_resultado(resultado=resultado)

@router.put(
    "/{resultado_id}",
    response_description="Actualizar un paciente",
    response_model=ResultadoCreate,
    status_code=status.HTTP_200_OK,
)
async def update_resultado(resultado_id: int, resultado: ResultadoCreate = Body(...)):
    return await logic.update_resultado(resultado_id=resultado_id, resultado=resultado)

@router.delete(
    "/{resultado_id}",
    response_description="Eliminar un paciente",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_resultado(resultado_id: int):
    await logic.delete_resultado(resultado_id=resultado_id)
    return {"detail": "Resultado eliminado exitosamente"}

@router.get(
    "/eventos/{evento_id}/resultados",
    response_description="Obtener resultados por evento",
    response_model=list[ResultadoRead],
    status_code=status.HTTP_200_OK,
)
async def get_resultados_por_evento(evento_id: int):
    return await logic.get_resultados_por_evento(evento_id=evento_id)    