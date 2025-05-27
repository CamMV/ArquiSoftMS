from fastapi import APIRouter
from views import pacientes_view

API_PREFIX = "/api"
router = APIRouter()

router.include_router(pacientes_view.router, prefix=pacientes_view.ENDPOINT_NAME)