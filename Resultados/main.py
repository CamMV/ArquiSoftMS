import uvicorn
from fastapi import FastAPI
import views as views
from models import db 

def create_app():
    app = FastAPI(
        docs_url="/resultados/docs",
        openapi_url="/resultados/openapi.json",
        title="Resultados API",
        redoc_url=None,
    )
    
    @app.on_event("startup")
    async def on_startup():
        await db.init_db()
    
    app.include_router(views.router)
    return app

if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8080)