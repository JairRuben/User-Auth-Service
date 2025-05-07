"""Archivo para el manejo de validación en usuarios"""

from fastapi import APIRouter, Depends, HTTPException, Header
from requests import Session

from app import auth, crud
from app.auth import verify_token
from app.database import SessionLocal
from app.schemas import UserCreate, UserOut


router = APIRouter()


@router.get("/protected")
def protected_route(user_data=Depends(verify_token)):
    """Verificación de Token Enviado"""
    return {"message": "Acceso autorizado", "user": user_data}


def get_db():
    """Dependencia para obtener la sesión sincrónica"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/me", response_model=UserOut)
def get_or_create_user(
    db: Session = Depends(get_db),
    authorization: str = Header(...),
):
    """Crea automáticamente un usuario si no existe, o lo devuelve si ya existe"""

    user_data = auth.verify_token(authorization)

    email = user_data["email"]
    name = user_data.get("name", "No name")
    photo = user_data.get("picture", "")
    phone = user_data.get("phone", "")
    uuid = user_data.get("uid")
    provider_sign_in = user_data["firebase"].get("sign_in_provider", "unknown")

    if not email or not uuid:
        raise HTTPException(status_code=400, detail="Datos del token incompletos")

    existing_user = crud.get_user_by_email(db, email)
    if existing_user:
        return existing_user

    name_parts = name.split(" ")

    if len(name_parts) == 4:
        nombre_usuario = " ".join(name_parts[:2]).title()
        apellido_usuario = " ".join(name_parts[2:]).title()
    else:
        nombre_usuario = name_parts[0]
        apellido_usuario = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""

    user_create = UserCreate(
        nombre_usuario=nombre_usuario,
        apellido_usuario=apellido_usuario,
        email_usuario=email,
        foto_usuario=photo,
        telefono_usuario=phone,
        uuid_usuario=uuid,
        tipo_login=provider_sign_in,
    )

    new_user = crud.create_user(db, user_create)
    return new_user
