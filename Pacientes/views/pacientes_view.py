from fastapi import APIRouter, status, Body, Depends, Request
import logic.pacientes_logic as logic
from models.schemas import PacienteCreate, PacienteRead
from pathlib import Path
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from models.db import get_db
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi.responses import RedirectResponse

router = APIRouter()
TEMPLATES_DIR = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

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
    status_code=status.HTTP_200_OK,
    response_class=HTMLResponse,
)
async def get_pacientes(request: Request, db: AsyncSession = Depends(get_db)):
    lista = await logic.get_pacientes(db)
    return templates.TemplateResponse(
        "pacientes.html",
        {
            "request": request,
            "pacientes": lista,
        }
    )

@router.get(
    "/pacientes/crear",
    response_class=HTMLResponse,
    status_code=status.HTTP_200_OK,
)
async def create_paciente_form(request: Request):
    return templates.TemplateResponse(
        "pacientes_create.html",
        {"request": request}
    )
    
@router.post(
    "/pacientes/crear",
    status_code=status.HTTP_303_SEE_OTHER,  # para redirigir tras POST
    response_class=RedirectResponse,
)
async def create_paciente_submit(
    request: Request,
    nombre: str = Form(...),
    edad: int = Form(...),
    ciudad: str = Form(...),
    db: AsyncSession = Depends(get_db),
):
    # Crea el schema y llama a la lógica
    nuevo = PacienteCreate(nombre=nombre, edad=edad, ciudad=ciudad)
    await logic.create_paciente(paciente=nuevo, db=db)
    # Redirige de vuelta a la lista
    return RedirectResponse(url="/pacientes", status_code=status.HTTP_303_SEE_OTHER)

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