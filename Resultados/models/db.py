from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

Base = declarative_base()

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+asyncpg://resultados_user:isis2503@10.128.0.81:5434/resultados_db"
)

engine = create_async_engine(DATABASE_URL, echo=True, future=True, pool_recycle=3600)

AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False # Esto evita que los objetos cargados expiren después de un commit
)

async def init_db():
    """
    Función para inicializar la base de datos (crear tablas si no existen).
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Dependencia para obtener una sesión de base de datos
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session