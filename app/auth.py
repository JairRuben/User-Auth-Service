"""Verificación de token"""

import os
from fastapi import HTTPException, status, Header
import firebase_admin
from firebase_admin import credentials, auth


firebase_credentials_path = os.getenv("FIREBASE_CREDENTIALS_PATH")

if firebase_credentials_path and os.path.exists(firebase_credentials_path):
    cred = credentials.Certificate(firebase_credentials_path)
    firebase_admin.initialize_app(cred)
else:
    print("⚠️ Firebase credentials not found, skipping Firebase initialization.")
    firebase_admin.initialize_app()


def verify_token(authorization: str = Header(...)):
    """Verificar Token FIREBASE"""
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing",
        )

    try:

        if not authorization.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Authorization header format. Expected 'Bearer <token>'",
            )

        token = authorization.replace("Bearer ", "").strip()
        decoded_token = auth.verify_id_token(token)
        return decoded_token

    except Exception as e:
        print(f"Token verification error: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        ) from e
