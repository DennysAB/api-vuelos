from fastapi import FastAPI
import os

app = FastAPI(title="API Vuelos")

@app.get("/health")
def health():
    return {"status": "ok", "timestamp": "2025-11-29"}

@app.get("/")
def root():
    return {
        "mensaje": "API Búsqueda de Vuelos",
        "endpoints": ["/health", "/buscar-vuelos"]
    }

@app.post("/buscar-vuelos")
def buscar_vuelos():
    return {
        "vuelos": [
            {
                "precio": 142.80,
                "origen": "MAD",
                "destino": "BCN",
                "aerolinea": "Iberia"
            }
        ],
        "total": 1,
        "modo": "demo"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
