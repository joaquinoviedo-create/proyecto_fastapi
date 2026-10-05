from fastapi import HTTPException, Query, status
from typing import Annotated

def verify_api_token(
    token: Annotated[str, Query(description="Token de seguridad obligatorio")]
):
    if token != "nivel-intermedio-2026":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Token no válido o ausente"
        )