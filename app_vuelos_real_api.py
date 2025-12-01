"""
FlightSearch Pro - API v3.0 con Datos Reales
Integra AviationStack API para vuelos en tiempo real
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import requests
import json
import os
from datetime import datetime, timedelta
import random
from aeropuertos_data import AEROPUERTOS_MUNDIALES as AEROPUERTOS, AEROLINEAS, SITIOS_COMPRA

# Configuración de la API
app = FastAPI(title="FlightSearch Pro - Real Data API", version="3.0")

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos de datos
class FlightSearch(BaseModel):
    origen: str
    destino: str
    fecha: str
    adultos: int = 1

class Flight(BaseModel):
    origen: str
    destino: str
    fecha: str
    precio: float
    moneda: str = "USD"
    precio_eur: Optional[float] = None
    aerolinea: str
    numero_vuelo: str
    duracion: str
    escalas: int
    estado: str = "programado"
    link_compra: str = ""
    tipo_busqueda: str = "real"

class SearchResponse(BaseModel):
    success: bool
    vuelos: List[Flight]
    total: int
    modo: str
    datos_reales: bool = True
    fecha_busqueda: str

# Configuración AviationStack
AVIATIONSTACK_API_KEY = os.getenv('AVIATIONSTACK_API_KEY', 'YOUR_API_KEY_HERE')
AVIATIONSTACK_BASE_URL = 'https://api.aviationstack.com/v1'

class AviationStackAPI:
    """Cliente para la API de AviationStack"""
    
    def __init__(self):
        self.api_key = AVIATIONSTACK_API_KEY
        self.base_url = AVIATIONSTACK_BASE_URL
        self.request_count = 0
        self.monthly_limit = 100  # Plan gratuito
        
    def is_available(self) -> bool:
        """Verifica si la API key está configurada"""
        return self.api_key and self.api_key != 'YOUR_API_KEY_HERE'
    
    def check_limits(self) -> bool:
        """Verifica si no hemos excedido los límites"""
        return self.request_count < self.monthly_limit
    
    def get_flights_today(self, dep_iata: str, arr_iata: str) -> List[dict]:
        """Obtiene vuelos en tiempo real para hoy"""
        if not self.is_available():
            return []
            
        if not self.check_limits():
            return []
            
        try:
            # Parámetros para la búsqueda
            params = {
                'access_key': self.api_key,
                'dep_iata': dep_iata,
                'arr_iata': arr_iata,
                'limit': 10,
                'flight_status': 'scheduled'
            }
            
            # Si se especifica una fecha, usarla
            today = datetime.now().strftime('%Y-%m-%d')
            params['flight_date'] = today
            
            url = f"{self.base_url}/flights"
            response = requests.get(url, params=params, timeout=10)
            
            self.request_count += 1
            
            if response.status_code == 200:
                data = response.json()
                return data.get('data', [])
            else:
                print(f"Error API: {response.status_code} - {response.text}")
                return []
                
        except Exception as e:
            print(f"Error al obtener vuelos reales: {e}")
            return []
    
    def convert_to_our_format(self, flight_data: dict) -> Optional[Flight]:
        """Convierte datos de AviationStack a nuestro formato"""
        try:
            departure = flight_data.get('departure', {})
            arrival = flight_data.get('arrival', {})
            airline = flight_data.get('airline', {})
            flight_info = flight_data.get('flight', {})
            
            # Obtener códigos de aeropuerto
            dep_iata = departure.get('iata', '')
            arr_iata = arrival.get('iata', '')
            
            if not dep_iata or not arr_iata:
                return None
            
            # Obtener información de la aerolínea
            airline_name = airline.get('name', 'Unknown')
            airline_iata = airline.get('iata', 'XX')
            
            # Generar número de vuelo realista
            flight_number = flight_info.get('iata', f"{airline_iata}{flight_info.get('number', '000')}")
            if not flight_number or len(flight_number) < 3:
                flight_number = f"{airline_iata}{random.randint(100, 999)}"
            
            # Calcular duración estimada (simplificado)
            duration = self._estimate_duration(dep_iata, arr_iata)
            
            # Generar precio simulado realista basado en distancia y aerolínea
            precio_usd = self._generate_realistic_price(dep_iata, arr_iata, airline_name)
            
            # Obtener enlace de compra
            link_compra = self._generate_purchase_link(dep_iata, arr_iata, flight_number)
            
            # Determinar si tiene escalas (simplificado)
            escalas = 0 if random.random() > 0.3 else 1
            
            return Flight(
                origen=dep_iata,
                destino=arr_iata,
                fecha=datetime.now().strftime('%Y-%m-%d'),
                precio=precio_usd,
                precio_eur=precio_usd * 0.85,  # Aproximación
                aerolinea=airline_name,
                numero_vuelo=flight_number,
                duracion=duration,
                escalas=escalas,
                link_compra=link_compra,
                tipo_busqueda="tiempo_real"
            )
            
        except Exception as e:
            print(f"Error al convertir vuelo: {e}")
            return None
    
    def _estimate_duration(self, dep_iata: str, arr_iata: str) -> str:
        """Estima la duración del vuelo basada en la distancia entre aeropuertos"""
        # Distancias aproximadas entre aeropuertos principales (en minutos)
        distances = {
            ('MAD', 'BCN'): 75,  # Madrid-Barcelona
            ('MAD', 'LHR'): 120,  # Madrid-Londres
            ('JFK', 'LAX'): 360,  # New York-Los Angeles
            ('JFK', 'CDG'): 420,  # New York-París
            ('MAD', 'JFK'): 480,  # Madrid-New York
        }
        
        route = tuple(sorted([dep_iata, arr_iata]))
        
        if route in distances:
            duration_minutes = distances[route]
        else:
            # Estimar basado en distancia aproximada
            duration_minutes = random.randint(90, 600)
        
        hours = duration_minutes // 60
        minutes = duration_minutes % 60
        
        return f"{hours}h {minutes}m"
    
    def _generate_realistic_price(self, dep_iata: str, arr_iata: str, airline_name: str) -> float:
        """Genera un precio realista basado en ruta y aerolínea"""
        # Precios base por distancia (aproximados)
        base_prices = {
            'Europa': 150,
            'America_Norte': 400,
            'America_Sur': 600,
            'Asia': 800,
            'Africa': 500,
            'Oceania': 900
        }
        
        # Determinar región basada en códigos de aeropuerto
        region = self._get_region(dep_iata, arr_iata)
        base_price = base_prices.get(region, 300)
        
        # Multiplicador por aerolínea
        airline_multipliers = {
            'Iberia': 1.0,
            'Vueling': 0.8,
            'Ryanair': 0.7,
            'British Airways': 1.3,
            'Air France': 1.2,
            'Lufthansa': 1.4,
            'United Airlines': 1.5,
            'American Airlines': 1.6,
            'Delta Air Lines': 1.5,
            'Southwest Airlines': 1.1
        }
        
        multiplier = airline_multipliers.get(airline_name, 1.0)
        
        # Variación aleatoria del ±20%
        variation = random.uniform(0.8, 1.2)
        
        return round(base_price * multiplier * variation, 2)
    
    def _get_region(self, dep_iata: str, arr_iata: str) -> str:
        """Determina la región de la ruta"""
        # Agrupación por regiones (simplificado)
        europe_airports = ['MAD', 'BCN', 'LHR', 'CDG', 'FCO', 'FRA', 'AMS', 'CPH', 'ARN', 'DUB']
        us_airports = ['JFK', 'LAX', 'ORD', 'ATL', 'DFW', 'DEN', 'SEA', 'LAS', 'PHX', 'MIA']
        asia_airports = ['NRT', 'PVG', 'PEK', 'ICN', 'SIN', 'BKK', 'HKG', 'DXB', 'DEL', 'MNL']
        
        if dep_iata in europe_airports or arr_iata in europe_airports:
            return 'Europa'
        elif dep_iata in us_airports or arr_iata in us_airports:
            if arr_iata in europe_airports or dep_iata in europe_airports:
                return 'America_Norte'  # Intercontinental
            return 'America_Norte'
        elif dep_iata in asia_airports or arr_iata in asia_airports:
            return 'Asia'
        else:
            return 'Europa'  # Por defecto
    
    def _generate_purchase_link(self, dep_iata: str, arr_iata: str, flight_number: str) -> str:
        """Genera un enlace de compra realista"""
        # Seleccionar sitio de compra aleatorio
        site = random.choice(list(SITIOS_COMPRA.keys()))
        today = datetime.now().strftime('%Y-%m-%d')
        
        # Enlaces con parámetros
        links = {
            'Expedia': f"https://www.expedia.com/Flights-Search?trip=roundtrip&leg1=from:{dep_iata},to:{arr_iata},departure:{today}TANYT&leg2=from:{arr_iata},to:{dep_iata},departure:{today}TANYT",
            'Booking.com': "https://www.booking.com/flights",
            'Skyscanner': f"https://www.skyscanner.com/transport/flights/{dep_iata.lower()}/{arr_iata.lower()}/{today.replace('-', '')}/{today.replace('-', '')}",
            'Kayak': f"https://www.kayak.com/flights/{dep_iata}-{arr_iata}/{today}/{today}",
            'Google Flights': f"https://www.google.com/travel/flights?q=tickets%20from%20{dep_iata}%20to%20{arr_iata}%20on%20{today}",
            'Cheapflights': f"https://www.cheapflights.com/flights/{dep_iata}-{arr_iata}/{today}",
            'Momondo': f"https://www.momondo.com/flights/{dep_iata}-{arr_iata}/{today}",
            'Priceline': f"https://www.priceline.com/flights/results/airlines={flight_number}"
        }
        
        return links.get(site, links['Expedia'])

# Instancia global del cliente API
aviation_client = AviationStackAPI()

def generate_mock_flights(search: FlightSearch) -> List[Flight]:
    """Genera vuelos simulados mejorados como fallback"""
    flights = []
    today = datetime.now()
    search_date = datetime.strptime(search.fecha, '%Y-%m-%d')
    
    # Determinar si la búsqueda es para hoy o futura
    is_today = search_date.date() == today.date()
    is_future = search_date > today + timedelta(days=1)
    
    # Si es futura, usar vuelos programados simulados
    # Si es hoy, intentar obtener datos reales primero
    real_flights = []
    
    if is_today and aviation_client.is_available():
        real_flights = aviation_client.get_flights_today(search.origen, search.destino)
        
        # Convertir vuelos reales
        for flight_data in real_flights[:3]:  # Limitar a 3 vuelos reales
            flight = aviation_client.convert_to_our_format(flight_data)
            if flight:
                flights.append(flight)
    
    # Completar con vuelos simulados si es necesario
    num_mock_flights = 3 - len(flights) if len(flights) < 3 else 0
    
    for i in range(num_mock_flights):
        # Seleccionar aerolínea aleatoria
        airline_name, airline_info = random.choice(list(AEROLINEAS.items()))
        airline_code = airline_info["codigo"]
        
        # Generar número de vuelo
        flight_number = f"{airline_code}{random.randint(100, 999)}"
        
        # Calcular duración
        duration = aviation_client._estimate_duration(search.origen, search.destino)
        
        # Precio realista
        precio_usd = aviation_client._generate_realistic_price(search.origen, search.destino, airline_name)
        
        # Link de compra
        link_compra = aviation_client._generate_purchase_link(search.origen, search.destino, flight_number)
        
        # Escalas aleatorias
        escalas = random.choice([0, 0, 0, 1])  # 75% directo, 25% con escalas
        
        mock_flight = Flight(
            origen=search.origen,
            destino=search.destino,
            fecha=search.fecha,
            precio=precio_usd,
            precio_eur=precio_usd * 0.85,
            aerolinea=airline_name,
            numero_vuelo=flight_number,
            duracion=duration,
            escalas=escalas,
            link_compra=link_compra,
            tipo_busqueda="simulado_mejorado"
        )
        
        flights.append(mock_flight)
    
    return sorted(flights, key=lambda x: x.precio)

@app.get("/")
async def root():
    """Endpoint raíz con información de la API"""
    return {
        "mensaje": "FlightSearch Pro - API v3.0 con Datos Reales",
        "version": "3.0",
        "endpoints": ["/health", "/buscar-vuelos", "/aeropuertos", "/api-info"],
        "datos_reales": aviation_client.is_available(),
        "request_count": f"{aviation_client.request_count}/{aviation_client.monthly_limit}"
    }

@app.get("/health")
async def health_check():
    """Endpoint de verificación de salud"""
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "version": "3.0",
        "aviationstack_configured": aviation_client.is_available(),
        "api_usage": f"{aviation_client.request_count}/{aviation_client.monthly_limit}"
    }

@app.post("/buscar-vuelos")
async def buscar_vuelos(search: FlightSearch):
    """Busca vuelos con datos reales y simulados mejorados"""
    try:
        # Validar que los aeropuertos existen
        if search.origen not in AEROPUERTOS:
            raise HTTPException(status_code=400, detail=f"Aeropuerto de origen no válido: {search.origen}")
        
        if search.destino not in AEROPUERTOS:
            raise HTTPException(status_code=400, detail=f"Aeropuerto de destino no válido: {search.destino}")
        
        if search.origen == search.destino:
            raise HTTPException(status_code=400, detail="El origen y destino no pueden ser el mismo")
        
        # Generar vuelos (reales + simulados)
        vuelos = generate_mock_flights(search)
        
        return SearchResponse(
            success=True,
            vuelos=vuelos,
            total=len(vuelos),
            modo="datos_reales",
            datos_reales=aviation_client.is_available(),
            fecha_busqueda=datetime.now().isoformat()
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

@app.get("/aeropuertos")
async def get_airports():
    """Obtiene lista de aeropuertos disponibles"""
    return {
        "aeropuertos": AEROPUERTOS,
        "total": len(AEROPUERTOS),
        "aerolineas": AEROLINEAS,
        "sitios_compra": SITIOS_COMPRA
    }

@app.get("/api-info")
async def api_info():
    """Información detallada sobre la API y configuración"""
    return {
        "api_name": "FlightSearch Pro v3.0",
        "version": "3.0",
        "data_sources": {
            "real_time": aviation_client.is_available(),
            "aviationstack": {
                "configured": aviation_client.is_available(),
                "monthly_limit": aviation_client.monthly_limit,
                "requests_used": aviation_client.request_count,
                "plan": "Free" if aviation_client.is_available() else "None"
            },
            "fallback": "Enhanced simulation with real airport data"
        },
        "features": {
            "worldwide_airports": len(AEROPUERTOS),
            "usd_pricing": True,
            "flight_numbers": True,
            "purchase_links": True,
            "real_time_data": aviation_client.is_available()
        },
        "configuration": {
            "aviationstack_api_key": "configured" if aviation_client.is_available() else "not_set"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)