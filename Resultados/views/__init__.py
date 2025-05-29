from fastapi import APIRouter
from Resultados.views import resultados_view

API_PREFIX = "/api"
router = APIRouter()

router.include_router(resultados_view.router, prefix=resultados_view.ENDPOINT_NAME)