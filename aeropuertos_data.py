#!/usr/bin/env python3
"""
Base de datos completa de aeropuertos mundiales
"""

AEROPUERTOS_MUNDIALES = {
    # EUROPA
    "MAD": {"nombre": "Madrid-Barajas", "ciudad": "Madrid", "pais": "España", "region": "Europa"},
    "BCN": {"nombre": "Barcelona-El Prat", "ciudad": "Barcelona", "pais": "España", "region": "Europa"},
    "CDG": {"nombre": "Paris Charles de Gaulle", "ciudad": "París", "pais": "Francia", "region": "Europa"},
    "ORY": {"nombre": "Paris Orly", "ciudad": "París", "pais": "Francia", "region": "Europa"},
    "LHR": {"nombre": "London Heathrow", "ciudad": "Londres", "pais": "Reino Unido", "region": "Europa"},
    "LGW": {"nombre": "London Gatwick", "ciudad": "Londres", "pais": "Reino Unido", "region": "Europa"},
    "STN": {"nombre": "London Stansted", "ciudad": "Londres", "pais": "Reino Unido", "region": "Europa"},
    "FCO": {"nombre": "Rome Fiumicino", "ciudad": "Roma", "pais": "Italia", "region": "Europa"},
    "BER": {"nombre": "Berlin Brandenburg", "ciudad": "Berlín", "pais": "Alemania", "region": "Europa"},
    "AMS": {"nombre": "Amsterdam Schiphol", "ciudad": "Ámsterdam", "pais": "Países Bajos", "region": "Europa"},
    "MXP": {"nombre": "Milan Malpensa", "ciudad": "Milán", "pais": "Italia", "region": "Europa"},
    "ZUR": {"nombre": "Zurich Airport", "ciudad": "Zúrich", "pais": "Suiza", "region": "Europa"},
    "VIE": {"nombre": "Vienna International", "ciudad": "Viena", "pais": "Austria", "region": "Europa"},
    "FRA": {"nombre": "Frankfurt Airport", "ciudad": "Frankfurt", "pais": "Alemania", "region": "Europa"},
    "MUC": {"nombre": "Munich Airport", "ciudad": "Múnich", "pais": "Alemania", "region": "Europa"},
    "CPH": {"nombre": "Copenhagen Kastrup", "ciudad": "Copenhague", "pais": "Dinamarca", "region": "Europa"},
    "ARN": {"nombre": "Stockholm Arlanda", "ciudad": "Estocolmo", "pais": "Suecia", "region": "Europa"},
    "OSL": {"nombre": "Oslo Gardermoen", "ciudad": "Oslo", "pais": "Noruega", "region": "Europa"},
    "HEL": {"nombre": "Helsinki Vantaa", "ciudad": "Helsinki", "pais": "Finlandia", "region": "Europa"},
    "DUB": {"nombre": "Dublin Airport", "ciudad": "Dublín", "pais": "Irlanda", "region": "Europa"},
    "LIS": {"nombre": "Lisbon Portela", "ciudad": "Lisboa", "pais": "Portugal", "region": "Europa"},
    "ATH": {"nombre": "Athens International", "ciudad": "Atenas", "pais": "Grecia", "region": "Europa"},
    "IST": {"nombre": "Istanbul Airport", "ciudad": "Estambul", "pais": "Turquía", "region": "Europa"},
    
    # AMÉRICA DEL NORTE
    "JFK": {"nombre": "John F. Kennedy", "ciudad": "Nueva York", "pais": "Estados Unidos", "region": "América del Norte"},
    "LAX": {"nombre": "Los Angeles International", "ciudad": "Los Ángeles", "pais": "Estados Unidos", "region": "América del Norte"},
    "ORD": {"nombre": "Chicago O'Hare", "ciudad": "Chicago", "pais": "Estados Unidos", "region": "América del Norte"},
    "MIA": {"nombre": "Miami International", "ciudad": "Miami", "pais": "Estados Unidos", "region": "América del Norte"},
    "ATL": {"nombre": "Atlanta Hartsfield-Jackson", "ciudad": "Atlanta", "pais": "Estados Unidos", "region": "América del Norte"},
    "DFW": {"nombre": "Dallas Fort Worth", "ciudad": "Dallas", "pais": "Estados Unidos", "region": "América del Norte"},
    "DEN": {"nombre": "Denver International", "ciudad": "Denver", "pais": "Estados Unidos", "region": "América del Norte"},
    "SEA": {"nombre": "Seattle-Tacoma International", "ciudad": "Seattle", "pais": "Estados Unidos", "region": "América del Norte"},
    "BOS": {"nombre": "Boston Logan International", "ciudad": "Boston", "pais": "Estados Unidos", "region": "América del Norte"},
    "SFO": {"nombre": "San Francisco International", "ciudad": "San Francisco", "pais": "Estados Unidos", "region": "América del Norte"},
    "LAS": {"nombre": "Las Vegas McCarran", "ciudad": "Las Vegas", "pais": "Estados Unidos", "region": "América del Norte"},
    "LGA": {"nombre": "LaGuardia", "ciudad": "Nueva York", "pais": "Estados Unidos", "region": "América del Norte"},
    "YVR": {"nombre": "Vancouver International", "ciudad": "Vancouver", "pais": "Canadá", "region": "América del Norte"},
    "YYZ": {"nombre": "Toronto Pearson International", "ciudad": "Toronto", "pais": "Canadá", "region": "América del Norte"},
    "MEX": {"nombre": "Mexico City International", "ciudad": "Ciudad de México", "pais": "México", "region": "América del Norte"},
    "GDL": {"nombre": "Guadalajara Don Miguel", "ciudad": "Guadalajara", "pais": "México", "region": "América del Norte"},
    "TIJ": {"nombre": "Tijuana Rodriguez", "ciudad": "Tijuana", "pais": "México", "region": "América del Norte"},
    
    # AMÉRICA DEL SUR
    "SCL": {"nombre": "Santiago Arturo Merino Benítez", "ciudad": "Santiago", "pais": "Chile", "region": "América del Sur"},
    "GRU": {"nombre": "São Paulo Guarulhos", "ciudad": "São Paulo", "pais": "Brasil", "region": "América del Sur"},
    "EZE": {"nombre": "Buenos Aires Ezeiza", "ciudad": "Buenos Aires", "pais": "Argentina", "region": "América del Sur"},
    "BOG": {"nombre": "Bogotá El Dorado", "ciudad": "Bogotá", "pais": "Colombia", "region": "América del Sur"},
    "LIM": {"nombre": "Jorge Chavez International", "ciudad": "Lima", "pais": "Perú", "region": "América del Sur"},
    
    # ASIA
    "BOM": {"nombre": "Mumbai Chhatrapati Shivaji", "ciudad": "Mumbai", "pais": "India", "region": "Asia"},
    "DEL": {"nombre": "Delhi Indira Gandhi", "ciudad": "Nueva Delhi", "pais": "India", "region": "Asia"},
    "BKK": {"nombre": "Bangkok Suvarnabhumi", "ciudad": "Bangkok", "pais": "Tailandia", "region": "Asia"},
    "SIN": {"nombre": "Singapore Changi", "ciudad": "Singapur", "pais": "Singapur", "region": "Asia"},
    "HKG": {"nombre": "Hong Kong International", "ciudad": "Hong Kong", "pais": "Hong Kong", "region": "Asia"},
    "TPE": {"nombre": "Taiwan Taoyuan", "ciudad": "Taipéi", "pais": "Taiwán", "region": "Asia"},
    "ICN": {"nombre": "Seoul Incheon International", "ciudad": "Seúl", "pais": "Corea del Sur", "region": "Asia"},
    "NRT": {"nombre": "Tokyo Narita International", "ciudad": "Tokio", "pais": "Japón", "region": "Asia"},
    "HND": {"nombre": "Tokyo Haneda", "ciudad": "Tokio", "pais": "Japón", "region": "Asia"},
    "PVG": {"nombre": "Shanghai Pudong International", "ciudad": "Shanghai", "pais": "China", "region": "Asia"},
    "PEK": {"nombre": "Beijing Capital International", "ciudad": "Pekín", "pais": "China", "region": "Asia"},
    "CAN": {"nombre": "Guangzhou Baiyun International", "ciudad": "Cantón", "pais": "China", "region": "Asia"},
    "DXB": {"nombre": "Dubai International", "ciudad": "Dubái", "pais": "Emiratos Árabes Unidos", "region": "Asia"},
    "DOH": {"nombre": "Doha Hamad International", "ciudad": "Doha", "pais": "Catar", "region": "Asia"},
    
    # ÁFRICA
    "JNB": {"nombre": "Johannesburg O.R. Tambo", "ciudad": "Johannesburgo", "pais": "Sudáfrica", "region": "África"},
    "CAI": {"nombre": "Cairo International", "ciudad": "El Cairo", "pais": "Egipto", "region": "África"},
    "CMN": {"nombre": "Casablanca Mohammed V", "ciudad": "Casablanca", "pais": "Marruecos", "region": "África"},
    "DUR": {"nombre": "King Shaka International", "ciudad": "Durban", "pais": "Sudáfrica", "region": "África"},
    "ADD": {"nombre": "Addis Ababa Bole", "ciudad": "Adís Abeba", "pais": "Etiopía", "region": "África"},
    "NBO": {"nombre": "Nairobi Jomo Kenyatta", "ciudad": "Nairobi", "pais": "Kenia", "region": "África"},
    
    # OCEANÍA
    "SYD": {"nombre": "Sydney Kingsford Smith", "ciudad": "Sídney", "pais": "Australia", "region": "Oceanía"},
    "MEL": {"nombre": "Melbourne International", "ciudad": "Melbourne", "pais": "Australia", "region": "Oceanía"},
    "AKL": {"nombre": "Auckland International", "ciudad": "Auckland", "pais": "Nueva Zelanda", "region": "Oceanía"},
    "WLG": {"nombre": "Wellington International", "ciudad": "Wellington", "pais": "Nueva Zelanda", "region": "Oceanía"},
    
    # MEDIO ORIENTE
    "DOH": {"nombre": "Doha Hamad International", "ciudad": "Doha", "pais": "Catar", "region": "Medio Oriente"},
    "DXB": {"nombre": "Dubai International", "ciudad": "Dubái", "pais": "Emiratos Árabes Unidos", "region": "Medio Oriente"},
    "ABD": {"nombre": "Abha", "ciudad": "Abha", "pais": "Arabia Saudí", "region": "Medio Oriente"},
}

# Aerolíneas principales
AEROLINEAS = {
    "Iberia": {"codigo": "IB", "pais": "España"},
    "British Airways": {"codigo": "BA", "pais": "Reino Unido"},
    "Air France": {"codigo": "AF", "pais": "Francia"},
    "Lufthansa": {"codigo": "LH", "pais": "Alemania"},
    "KLM": {"codigo": "KL", "pais": "Países Bajos"},
    "Swiss": {"codigo": "LX", "pais": "Suiza"},
    "Austrian Airlines": {"codigo": "OS", "pais": "Austria"},
    "American Airlines": {"codigo": "AA", "pais": "Estados Unidos"},
    "Delta Airlines": {"codigo": "DL", "pais": "Estados Unidos"},
    "United Airlines": {"codigo": "UA", "pais": "Estados Unidos"},
    "Emirates": {"codigo": "EK", "pais": "Emiratos Árabes Unidos"},
    "Qatar Airways": {"codigo": "QR", "pais": "Catar"},
    "Etihad": {"codigo": "EY", "pais": "Emiratos Árabes Unidos"},
    "Singapore Airlines": {"codigo": "SQ", "pais": "Singapur"},
    "Turkish Airlines": {"codigo": "TK", "pais": "Turquía"},
    "Vueling": {"codigo": "VY", "pais": "España"},
    "Ryanair": {"codigo": "FR", "pais": "Irlanda"},
    "EasyJet": {"codigo": "U2", "pais": "Reino Unido"},
}

# Sitios de compra
SITIOS_COMPRA = {
    "Expedia": "https://www.expedia.com/Flights",
    "Booking.com": "https://www.booking.com/flights",
    "Kayak": "https://www.kayak.com/flights",
    "Skyscanner": "https://www.skyscanner.com",
    "Cheapflights": "https://www.cheapflights.com",
    "Momondo": "https://www.momondo.com",
    "Travelocity": "https://www.travelocity.com",
    "Orbitz": "https://www.orbitz.com",
}

def get_aeropuerto_info(codigo):
    """Obtener información de un aeropuerto"""
    return AEROPUERTOS_MUNDIALES.get(codigo.upper(), {})

def get_aerolineas():
    """Obtener lista de aerolíneas"""
    return AEROLINEAS

def get_sitios_compra():
    """Obtener sitios de compra"""
    return SITIOS_COMPRA