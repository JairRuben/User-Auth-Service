"""CRUD para manejar las operaciones en la base de datos"""

from sqlalchemy.orm import Session
from app.models import DireccionUsers, Users
from app.schemas import UserCreate, DireccionUserCreate


def create_user(db: Session, user: UserCreate):
    """Crear nuevo usuario en la base de datos"""
    db_user = Users(
        nombre_usuario=user.nombre_usuario,
        apellido_usuario=user.apellido_usuario,
        email_usuario=user.email_usuario,
        foto_usuario=user.foto_usuario,
        telefono_usuario=user.telefono_usuario,
        uuid_usuario=user.uuid_usuario,
        tipo_login=user.tipo_login,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    """Obtener usuario por correo electrónico"""
    return db.query(Users).filter(Users.email_usuario == email).first()


def get_user_by_uuid(db: Session, uuid: str):
    """Obtener usuario por UUID (Firebase)"""
    return db.query(Users).filter(Users.uuid_usuario == uuid).first()


def create_user_address(db: Session, user_id: int, address: DireccionUserCreate):
    """Crear dirección para un usuario"""
    db_address = DireccionUsers(
        id_usuario=user_id,
        ciudad=address.ciudad,
        direccion=address.direccion,
        codigo_postal=address.codigo_postal,
        referencia=address.referencia,
    )
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def get_addresses_by_user_id(db: Session, user_id: int):
    """Obtener la direccion de un usuario"""
    return db.query(DireccionUsers).filter(DireccionUsers.id_usuario == user_id).all()
