"""Definición de la tablas de la bases de datos"""

from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Users(Base):
    """Base de datos de Usuarios"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_usuario = Column(String(255), nullable=False)
    apellido_usuario = Column(String(255), nullable=False)
    email_usuario = Column(String(255), unique=True, nullable=False, index=True)
    foto_usuario = Column(String(255))
    telefono_usuario = Column(String(20))
    uuid_usuario = Column(String(50), nullable=False)
    tipo_login = Column(String(50), nullable=False)
    fecha_creacion_usuario = Column(DateTime, default=datetime.utcnow)


class DireccionUsers(Base):
    """Base de datos de Dirección de Envio de Usuarios"""

    __tablename__ = "direccion_users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("users.id"), nullable=False)
    ciudad = Column(String(255), nullable=False)
    direccion = Column(String(255), nullable=False)
    codigo_postal = Column(String(10), nullable=False)
    referencia = Column(String(100), nullable=False)

    usuario = relationship("Users", backref="direcciones")
