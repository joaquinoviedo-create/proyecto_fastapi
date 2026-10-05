from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Annotated
from dependencies import verify_api_token

# ESTA ES LA VARIABLE QUE UVICORN NO ENCUENTRA:
router = APIRouter(prefix="/products", tags=["Productos"])

db_productos = []

class Producto(BaseModel):
    nombre: str
    precio: float

@router.post("/")
def agregar_producto(
    producto: Producto, 
    token_verificado: Annotated[None, Depends(verify_api_token)]
):
    db_productos.append(producto.model_dump())
    return {"message": "Producto agregado", "producto": producto}

@router.get("/")
def listar_productos():
    return db_productos