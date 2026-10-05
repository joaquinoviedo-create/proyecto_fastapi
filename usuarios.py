from fastapi import APIRouter, HTTPException, Path, Query, status
from pydantic import BaseModel, Field
from typing import Annotated

# ESTA ES LA VARIABLE QUE LE FALTA A MAIN:
router = APIRouter(prefix="/users", tags=["Usuarios"])

db_usuarios = []

class Usuario(BaseModel):
    id: int
    username: str = Field(..., min_length=5)
    edad: int = Field(..., ge=18)

@router.post("/", status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: Annotated[Usuario, "Esquema de usuario"]):
    for u in db_usuarios:
        if u["id"] == usuario.id or u["username"] == usuario.username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="El usuario ya existe"
            )
    db_usuarios.append(usuario.model_dump())
    return {"message": "Usuario registrado con éxito", "user": usuario}

@router.get("/{user_id}")
def buscar_usuario(
    user_id: Annotated[int, Path(gt=0, description="El ID debe ser mayor a 0")],
    categoria: Annotated[str, Query(min_length=3)] = "general"
):
    for u in db_usuarios:
        if u["id"] == user_id:
            return {"usuario": u, "categoria_buscada": categoria}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")