from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from models.models import Paciente  # Importa tus modelos aquí


Base = declarative_base()

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+asyncpg://pacientes_user:isis2503@10.128.0.81:5433/pacientes_db"
)

engine = create_async_engine(DATABASE_URL, echo=True, future=True, pool_recycle=3600)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Dependencia para obtener una sesión de base de datos
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session