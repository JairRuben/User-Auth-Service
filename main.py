"""Archivo principal, Servicio de Usuarios"""

from sqlalchemy import inspect
from fastapi import FastAPI
from app.routes import users
from app.database import engine
from app.models import Base


inspector = inspect(engine)
tables = inspector.get_table_names()

if not tables:
    print("No se encontraron tablas, creando las tablas...")
    Base.metadata.create_all(bind=engine)
else:
    print("Tablas existentes en la base de datos:", tables)

app = FastAPI(title="API de Usuarios", version="1.0.0")

app.include_router(
    users.router,
    prefix="/users",
    tags=["Usuarios"],
    responses={404: {"description": "No encontrado"}},
)
