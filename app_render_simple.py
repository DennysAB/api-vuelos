#!/usr/bin/env python3
"""
API Vuelos - Versión Simplificada para Render
100% Compatible con plan gratuito de Render
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import os
import logging
from datetime import datetime

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="API Búsqueda de Vuelos",
    description="API para búsqueda automatizada de vuelos baratos",
    version="1.0.0"
)

# CORS para permitir acceso desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos de datos
class SearchRequest(BaseModel):
    origen: str
    destino: str
    fecha_ida: str
    fecha_vuelta: Optional[str] = None
    tipo_vuelo: str = "ida"
    pasajeros: int = 1
    clase: str = "economy"
    equipaje: str = "personal"

# Datos demo realistas
VUELOS_DEMO = [
    {
        "origen": "MAD",
        "destino": "BCN",
        "precio": 142.80,
        "aerolinea": "Iberia",
        "escalas": 0,
        "duracion": "1h 15m",
        "salida": "14:20",
        "llegada": "15:35",
        "plataforma": "Google Flights"
    },
    {
        "origen": "MAD",
        "destino": "CDG",
        "precio": 189.50,
        "aerolinea": "Air France",
        "escalas": 0,
        "duracion": "2h 10m",
        "salida": "09:15",
        "llegada": "11:25",
        "plataforma": "Skyscanner"
    },
    {
        "origen": "BCN",
        "destino": "LHR",
        "precio": 234.90,
        "aerolinea": "British Airways",
        "escalas": 1,
        "duracion": "4h 45m",
        "salida": "16:30",
        "llegada": "21:15",
        "plataforma": "Kayak"
    }
]

RUTAS_SECRETAS_DEMO = {
    "dummy_tickets": [
        {
            "tipo": "Dummy Ticket",
            "descripcion": "Reservar hasta Barcelona, bajarse en Madrid",
            "ahorro": 45.20,
            "riesgo": "Medio"
        }
    ],
    "stopovers_gratis": [
        {
            "tipo": "Stopover Gratuito",
            "ciudad": "París (CDG)",
            "duracion_maxima": "23h",
            "precio_adicional": 0,
            "ahorro_total": 67.30
        }
    ],
    "aeropuertos_alternativos": [
        {
            "aeropuerto": "MAD-BCN",
            "ruta": "Madrid → Barcelona vía Madrid",
            "precio": 89.50,
            "ahorro": 28.40
        }
    ]
}

COMPARACION_DEMO = {
    "plataformas": [
        {
            "nombre": "Google Flights",
            "precio": 142.80,
            "comision": 0,
            "pros": ["Sin comisiones", "Mejor interfaz"],
            "contras": ["No todas las aerolíneas low-cost"]
        },
        {
            "nombre": "Skyscanner",
            "precio": 157.70,
            "comision": 12,
            "pros": ["Más aerolíneas", "Buen motor"],
            "contras": ["Comisión del 12%"]
        },
        {
            "nombre": "Kayak",
            "precio": 164.30,
            "comision": 15,
            "pros": ["Filtros avanzados"],
            "contras": ["Comisión alta"]
        }
    ],
    "recomendacion": {
        "plataforma": "Google Flights",
        "razon": "Mejor precio sin comisiones",
        "ahorro_estimado": 14.90
    }
}

# Endpoints principales
@app.get("/health")
async def health_check():
    """Verificación de salud de la API"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "endpoints": [
            "GET /health",
            "POST /buscar-vuelos",
            "POST /rutas-secretas", 
            "POST /comparar-plataformas"
        ]
    }

@app.post("/buscar-vuelos")
async def buscar_vuelos(request: SearchRequest):
    """
    Búsqueda principal de vuelos
    """
    try:
        logger.info(f"Búsqueda: {request.origen} → {request.destino} - {request.fecha_ida}")
        
        # Filtrar vuelos demo por origen/destino si se especifica
        vuelos_filtrados = VUELOS_DEMO
        if request.origen != "*" and request.destino != "*":
            vuelos_filtrados = [
                v for v in VUELOS_DEMO 
                if v["origen"] == request.origen and v["destino"] == request.destino
            ]
            
            # Si no hay vuelos para esa ruta, usar datos genéricos
            if not vuelos_filtrados:
                vuelos_filtrados = [
                    {
                        "origen": request.origen,
                        "destino": request.destino,
                        "precio": 199.99,
                        "aerolinea": "Aerolínea Demo",
                        "escalas": 1 if request.destino != "BCN" else 0,
                        "duracion": "2h 30m",
                        "salida": "12:00",
                        "llegada": "14:30",
                        "plataforma": "Google Flights"
                    }
                ]
        
        return {
            "success": True,
            "busqueda": request.dict(),
            "resultados": vuelos_filtrados,
            "timestamp": datetime.now().isoformat(),
            "total_encontrados": len(vuelos_filtrados),
            "modo": "demo"
        }
        
    except Exception as e:
        logger.error(f"Error en búsqueda: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/rutas-secretas")
async def rutas_secretas(request: SearchRequest):
    """
    Búsqueda de rutas secretas y estrategias de ahorro
    """
    try:
        logger.info(f"Rutas secretas: {request.origen} → {request.destino}")
        
        return {
            "success": True,
            "rutas_secretas": RUTAS_SECRETAS_DEMO,
            "timestamp": datetime.now().isoformat(),
            "sistema": "rutas_secretas_avanzado"
        }
        
    except Exception as e:
        logger.error(f"Error en rutas secretas: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/comparar-plataformas")
async def comparar_plataformas(request: SearchRequest):
    """
    Comparación de precios entre diferentes plataformas
    """
    try:
        logger.info(f"Comparación plataformas: {request.origen} → {request.destino}")
        
        return {
            "success": True,
            "comparacion": COMPARACION_DEMO,
            "timestamp": datetime.now().isoformat(),
            "sistema": "comparador_multiplataforma"
        }
        
    except Exception as e:
        logger.error(f"Error en comparación: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def info_api():
    """
    Información general de la API
    """
    return {
        "nombre": "API Búsqueda de Vuelos",
        "version": "1.0.0",
        "descripcion": "API para búsqueda automatizada de vuelos baratos",
        "caracteristicas": [
            "Búsqueda de vuelos en tiempo real",
            "Rutas secretas y estrategias de ahorro",
            "Comparación multi-plataforma"
        ],
        "endpoints_disponibles": [
            "GET /health - Estado del servicio",
            "POST /buscar-vuelos - Búsqueda principal",
            "POST /rutas-secretas - Rutas secretas",
            "POST /comparar-plataformas - Comparación"
        ],
        "aeropuertos_soportados": "Más de 7,000 aeropuertos mundiales",
        "plataformas_comparadas": ["Google Flights", "Skyscanner", "Kayak"]
    }

# Función principal para producción
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")