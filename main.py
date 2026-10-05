from fastapi import FastAPI, Depends
from routers import usuarios, productos
from dependencies import verify_api_token

# Punto de entrada principal (Consigna 5)
app = FastAPI(title="Trabajo Práctico 1 - FastAPI")

# Registro del router de usuarios (Ejercicios 1 y 2)
app.include_router(usuarios.router)

# Lógica de Bloqueo Global para productos usando el parámetro dependencies (Ejercicio 4)
app.include_router(productos.router, dependencies=[Depends(verify_api_token)])

@app.get("/")
def root():
    return {"message": "API Funcionando correctamente. Ve a /docs para probarla."}