import csv
import json
from flask import current_app
import os
import math

SPECIALTY_MAP = {}
HOSPITALS = []
DATA_LOADED = False

# City coordinates mapping (latitude, longitude)
CITY_COORDINATES = {
    "new delhi": (28.7041, 77.1025),
    "delhi": (28.7041, 77.1025),
    "rishikesh": (30.0893, 78.2679),
    "dehradun": (30.3165, 78.0322),
    "haridwar": (29.9457, 78.1642),
    "lucknow": (26.8467, 80.9462),
    "gurgaon": (28.4595, 77.0266),
    "bhopal": (23.1815, 79.9864),
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946),
    "hyderabad": (17.3850, 78.4867),
    "kolkata": (22.5726, 88.3639),
    "chennai": (13.0827, 80.2707),
    "pune": (18.5204, 73.8567),
    "ahmedabad": (23.0225, 72.5714),
    "jaipur": (26.9124, 75.7873),
    "surat": (21.1702, 72.8311),
    "chandigarh": (30.7333, 76.7794),
    "indore": (22.7196, 75.8577),
    "visakhapatnam": (17.6869, 83.2185),
    "nagpur": (21.1458, 79.0882),
    "kochi": (9.9312, 76.2673),
    "noida": (28.5355, 77.3910),
    "thane": (19.2183, 72.9781),
    "nashik": (19.9975, 73.7898),
    "aurangabad": (19.8762, 75.3433),
    "vadodara": (22.3072, 73.1812),
    "ghaziabad": (28.6692, 77.4538),
    "ludhiana": (30.9010, 75.8573),
    "agra": (27.1767, 78.0081),
    "jabalpur": (23.1815, 79.9864),
    "ranchi": (23.3441, 85.3096),
    "srinagar": (34.0837, 74.7973),
    "coimbatore": (11.0026, 76.9124),
    "allahabad": (25.4358, 81.8463),
    "varanasi": (25.3176, 82.9739),
    "amritsar": (31.6340, 74.8723),
    "guwahati": (26.1445, 91.7362),
    "mysore": (12.2958, 76.6394),
    "madurai": (9.9252, 78.1198),
    "erode": (11.3919, 79.1159),
    "rajkot": (22.3039, 70.8022),
    "thrissur": (10.5276, 76.2144),
    "thiruvananthapuram": (8.5241, 76.9366),
    "meerut": (28.9845, 77.7064),
    "faridabad": (28.4089, 77.3178),
    "durgapur": (23.7957, 87.3140),
    "asansol": (23.6889, 86.9709),
    "salem": (11.6643, 78.1460),
    "tiruppur": (11.1085, 77.3411),
    "jamshedpur": (22.8046, 86.1827),
    "kota": (25.2138, 75.8648),
    "udaipur": (24.5854, 73.7125),
    "jodhpur": (26.2389, 73.0243),
    "bikaner": (28.0229, 71.8325),
    "ajmer": (26.4499, 74.6399),
    "bareilly": (28.3670, 79.4304),
    "moradabad": (28.8385, 77.7597),
    "aligarh": (27.8974, 77.8942),
    "mathura": (27.4924, 77.6737),
    "gwalior": (26.2389, 78.1784),
    "ujjain": (23.1815, 75.7733),
    "ratlam": (23.3308, 75.0541),
    "khandwa": (21.8333, 76.3667),
    "bhind": (26.5283, 78.7722),
    "morena": (26.5033, 78.3856),
    "davangere": (14.4667, 75.9167),
    "hassan": (13.9991, 75.9478),
    "tumkur": (13.2176, 77.1146),
    "belgaum": (15.8497, 74.5097),
    "bijapur": (16.8303, 75.7305),
    "bagalkot": (16.1667, 75.6667),
    "hubli": (15.3647, 75.1240),
    "berhampur": (19.3150, 84.7941),
    "balasore": (21.4938, 86.9270),
    "sambalpur": (21.5657, 84.0242),
    "rourkela": (22.2604, 84.8536),
    "chhindwara": (22.0615, 78.9934),
    "seoni": (22.6667, 79.1500),
    "mandla": (22.5667, 80.6333),
    "hosangabad": (21.8333, 77.7500),
    "burhanpur": (21.3060, 76.2261),
    "khargone": (21.8107, 75.5181),
    "nanded": (19.1383, 76.3185),
    "parbhani": (19.2683, 76.7674),
    "latur": (18.4088, 76.5158),
    "beed": (19.2556, 75.7597),
    "jalna": (19.8367, 75.8761),
    "washim": (20.1067, 76.3250),
    "vikarabad": (17.3424, 77.2542),
    "jolly grant": (30.1928, 78.2345),
}


def calculate_distance(city1: str, city2: str) -> float:
    """Calculate distance between two cities using Haversine formula (in km)"""
    coords1 = CITY_COORDINATES.get(city1.lower())
    coords2 = CITY_COORDINATES.get(city2.lower())
    
    if not coords1 or not coords2:
        return 0.0
    
    lat1, lon1 = coords1
    lat2, lon2 = coords2
    
    # Haversine formula
    R = 6371  # Earth's radius in kilometers
    
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dlon / 2) * math.sin(dlon / 2)
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    
    return round(distance, 1)


def load_specialty_map():
    global SPECIALTY_MAP, DATA_LOADED

    try:
        path = current_app.config.get("DISEASE_SPECIALTY_MAP")
        
        if not path or not os.path.exists(path):
            print(f"Warning: Disease specialty map not found at {path}")
            SPECIALTY_MAP = {}
            return

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

            # convert list → dictionary
            SPECIALTY_MAP = {
                item["disease"].lower(): item["specialty"].lower()
                for item in data
            }

    except Exception as e:
        print(f"Error loading specialty map: {e}")
        SPECIALTY_MAP = {}


def load_hospitals():
    global HOSPITALS, DATA_LOADED

    try:
        path = current_app.config.get("HOSPITALS_CSV")
        
        if not path or not os.path.exists(path):
            print(f"Warning: Hospital list not found at {path}")
            HOSPITALS = []
            return

        with open(path, "r", encoding="utf-8") as f:

            reader = csv.DictReader(f)

            hospitals = []

            for row in reader:
                hospital_type = row.get("type", "").lower()
                
                # Assign realistic ratings based on hospital type
                if hospital_type == "government":
                    rating = round(3.8 + (hash(row.get("name", "")) % 20) / 100, 1)
                else:  # Private
                    rating = round(4.2 + (hash(row.get("name", "")) % 30) / 100, 1)
                
                # Clamp rating between 1-5
                rating = min(5.0, max(1.0, rating))

                hospitals.append({
                    "name": row.get("name", ""),
                    "city": row.get("city", "").lower(),
                    "type": row.get("type", ""),
                    "phone": row.get("phone", ""),
                    "address": f"{row.get('city', '')}, {row.get('type', '')} Hospital",
                    "specialties": [
                        s.strip().lower()
                        for s in row.get("specialties", "").split("|")
                        if s.strip()
                    ],
                    "rating": rating
                })

            HOSPITALS = hospitals
            DATA_LOADED = True

    except Exception as e:
        print(f"Error loading hospitals: {e}")
        HOSPITALS = []


def find_hospitals_for_disease(disease: str, city: str):
    global DATA_LOADED
    
    # Load data if not already loaded
    if not DATA_LOADED:
        load_specialty_map()
        load_hospitals()

    if not disease or not city:
        return []

    disease = disease.lower()
    city = city.lower()

    specialty = SPECIALTY_MAP.get(disease)

    # Filter by city
    city_hospitals = [h for h in HOSPITALS if h["city"] == city]

    if not city_hospitals:
        result = HOSPITALS[:5]
    elif not specialty:
        result = city_hospitals[:5]
    else:
        # Filter by specialty
        filtered = [
            h for h in city_hospitals
            if specialty in h["specialties"]
        ]
        result = filtered[:5] if filtered else city_hospitals[:5]

    # Add distance information to each hospital
    for hospital in result:
        hospital["distance"] = calculate_distance(city, hospital["city"])

    return result