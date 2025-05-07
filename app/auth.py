"""Verificación de token"""

import json
import os
import urllib.request
from fastapi import HTTPException, status, Header
from firebase_admin import credentials, auth, initialize_app

# firebase_credentials_path = os.getenv("FIREBASE_CREDENTIALS_PATH")

firebase_url = os.getenv("FIREBASE_CREDENTIALS_PATH")

if firebase_url:
    with urllib.request.urlopen(firebase_url) as response:
        cred_data = json.load(response)
    cred = credentials.Certificate(cred_data)
    initialize_app(cred)
else:
    print("⚠️ No Firebase credentials found.")

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
