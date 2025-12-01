#!/usr/bin/env python3
"""
API Vuelos - Corregida para CORS desde navegador
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os

# Crear app FastAPI
app = FastAPI(title="API Vuelos", version="1.0.0")

# CORS ultra-permisivo para pruebas
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las URLs
    allow_credentials=True,  # Permitir credenciales
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todos los headers
)

@app.get("/")
async def root():
    """Endpoint raíz"""
    return JSONResponse(content={
        "mensaje": "API Vuelos - CORS Corregido",
        "status": "funcionando",
        "cors": "habilitado",
        "endpoints": ["/health", "/buscar-vuelos"]
    })

@app.get("/health")
async def health():
    """Health check"""
    return JSONResponse(content={
        "status": "ok",
        "cors_enabled": True,
        "message": "API funcionando con CORS habilitado"
    })

@app.post("/buscar-vuelos")
async def buscar_vuelos(data: dict):
    """Búsqueda de vuelos con CORS corregido"""
    
    # Extraer datos con valores por defecto
    origen = data.get("origen", "MAD")
    destino = data.get("destino", "BCN")
    fecha = data.get("fecha", "2025-01-15")
    
    # Datos de respuesta
    respuesta = {
        "success": True,
        "vuelos": [
            {
                "origen": origen,
                "destino": destino,
                "fecha": fecha,
                "precio": 142.80,
                "aerolinea": "Iberia",
                "duracion": "1h 15m",
                "escalas": 0
            },
            {
                "origen": origen,
                "destino": destino,
                "fecha": fecha,
                "precio": 168.50,
                "aerolinea": "Vueling",
                "duracion": "1h 20m",
                "escalas": 0
            }
        ],
        "total": 2,
        "modo": "demo_cors_fix"
    }
    
    return JSONResponse(content=respuesta)

# Handler para OPTIONS (preflight CORS)
@app.options("/buscar-vuelos")
async def options_buscar_vuelos():
    """Manejar preflight OPTIONS para CORS"""
    return JSONResponse(content={"message": "OPTIONS allowed"}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    print(f"Iniciando API con CORS en puerto {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
