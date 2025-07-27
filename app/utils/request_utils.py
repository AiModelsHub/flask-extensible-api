import random
from app.core.config import Config

def random_lat_lng():
    lat1 = random.uniform(43.4, 43.9)
    lat2 = random.uniform(lat1, 44.0)

    lng1 = random.uniform(1.1, 1.75)
    lng2 = random.uniform(lng1, 1.8)
    
    return [[lat1, lng1], [lat2, lng2]]

def build_headers():
    return {
        "Host": "maps.googleapis.com",
        "Content-Type": "application/json+protobuf",
        "X-Goog-Maps-API-Salt": Config.GOOGLE_MAPS_API_SALT,
        "X-Goog-Maps-API-Signature": Config.GOOGLE_MAPS_API_SIGNATURE,
        "X-Goog-Maps-Client-Id": Config.GOOGLE_MAPS_CLIENT_ID,
        "X-Goog-Gmp-Client-Signals": Config.GOOGLE_MAPS_GMP_CLIENT_SIGNALS,
        "X-Goog-Maps-Session-Id": Config.GOOGLE_MAPS_SESSION_ID,
        "X-User-Agent": "grpc-web-javascript/0.1",
        "Origin": "https://www.google.com",
        "Referer": "https://www.google.com/"
    }

def build_data():
    return [
        random_lat_lng(),
        8, None, "en-US", 2, None, 0, 0, None, None, 289, 1,
        "https://www.google.com/maps/embed", 1
    ]
