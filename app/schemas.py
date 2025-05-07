"""Esquemas para el manejo de información para la base de datos"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    """Esquema de datos para crear un usuario (entrada)"""

    nombre_usuario: str
    apellido_usuario: str
    email_usuario: str
    foto_usuario: Optional[str] = None
    telefono_usuario: Optional[str] = None
    uuid_usuario: str
    tipo_login: str

    class Config:
        """Leer archivos ORM de SQLAlchemy, no solo dicts"""

        from_attributes = True


class UserOut(BaseModel):
    """Esquema para devolver los datos de un usuario (salida)"""

    id: int
    nombre_usuario: str
    apellido_usuario: str
    email_usuario: str
    foto_usuario: Optional[str] = None
    telefono_usuario: Optional[str] = None
    uuid_usuario: str
    tipo_login: str
    fecha_creacion_usuario: datetime

    class Config:
        """Leer archivos ORM de SQLAlchemy, no solo dicts"""

        from_attributes = True


class DireccionUserCreate(BaseModel):
    """Esquema para creacion de direccion de usuario (entrada)"""

    ciudad: str
    direccion: str
    codigo_postal: str
    referencia: str

    class Config:
        """Leer archivos ORM de SQLAlchemy, no solo dicts"""

        from_attributes = True


class DireccionUserOut(BaseModel):
    """Esquema para devolver la direccion de usuario (salida)"""

    id: int
    ciudad: str
    direccion: str
    codigo_postal: str
    referencia: str

    class Config:
        """Leer archivos ORM de SQLAlchemy, no solo dicts"""

        from_attributes = True
