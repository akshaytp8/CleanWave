import random
import numpy as np
from datetime import datetime, timedelta

# Ward names follow the 2020 Kerala Local Self Government Department election
# roster. Coordinates are illustrative markers around Chemmad, not ward centers.
TIRURANGADI_WARDS = [
    {"id": "W001", "name": "Thrikkulam Palathingal", "lat": 11.0280, "lon": 75.8970},
    {"id": "W002", "name": "Pathinarungal", "lat": 11.0280, "lon": 75.9050},
    {"id": "W003", "name": "Karayil", "lat": 11.0280, "lon": 75.9130},
    {"id": "W004", "name": "Kakkunathupara", "lat": 11.0280, "lon": 75.9210},
    {"id": "W005", "name": "Pantharangadi", "lat": 11.0360, "lon": 75.8970},
    {"id": "W006", "name": "Kariparambu", "lat": 11.0360, "lon": 75.9050},
    {"id": "W007", "name": "Manippadam", "lat": 11.0360, "lon": 75.9130},
    {"id": "W008", "name": "Chemmad North", "lat": 11.0360, "lon": 75.9210},
    {"id": "W009", "name": "Mamburam", "lat": 11.0440, "lon": 75.8970},
    {"id": "W010", "name": "Tirurangadi East", "lat": 11.0440, "lon": 75.9050},
    {"id": "W011", "name": "Soudabad", "lat": 11.0440, "lon": 75.9130},
    {"id": "W012", "name": "Kakkad East", "lat": 11.0440, "lon": 75.9210},
    {"id": "W013", "name": "Karimbil", "lat": 11.0520, "lon": 75.8970},
    {"id": "W014", "name": "Venniyoor", "lat": 11.0520, "lon": 75.9050},
    {"id": "W015", "name": "Kapprad", "lat": 11.0520, "lon": 75.9130},
    {"id": "W016", "name": "Mattil", "lat": 11.0520, "lon": 75.9210},
    {"id": "W017", "name": "Kachadi", "lat": 11.0600, "lon": 75.8970},
    {"id": "W018", "name": "Chullippara South", "lat": 11.0600, "lon": 75.9050},
    {"id": "W019", "name": "Chullippara North", "lat": 11.0600, "lon": 75.9130},
    {"id": "W020", "name": "Kundalangadu", "lat": 11.0600, "lon": 75.9210},
    {"id": "W021", "name": "Karimbil West", "lat": 11.0280, "lon": 75.9050},
    {"id": "W022", "name": "Kakkad", "lat": 11.0280, "lon": 75.9130},
    {"id": "W023", "name": "Koyilippadam", "lat": 11.0280, "lon": 75.9210},
    {"id": "W024", "name": "Melechina", "lat": 11.0360, "lon": 75.8970},
    {"id": "W025", "name": "Thazhechina", "lat": 11.0360, "lon": 75.9050},
    {"id": "W026", "name": "Cherappurathazham", "lat": 11.0360, "lon": 75.9130},
    {"id": "W027", "name": "Tirurangadi", "lat": 11.0360, "lon": 75.9210},
    {"id": "W028", "name": "Chanthappadi", "lat": 11.0440, "lon": 75.8970},
    {"id": "W029", "name": "Azad Nagar", "lat": 11.0440, "lon": 75.9050},
    {"id": "W030", "name": "C.K Nagar", "lat": 11.0440, "lon": 75.9130},
    {"id": "W031", "name": "C.K Nagar South", "lat": 11.0440, "lon": 75.9210},
    {"id": "W032", "name": "Kumbamkadavu", "lat": 11.0520, "lon": 75.8970},
    {"id": "W033", "name": "Venchali", "lat": 11.0520, "lon": 75.9050},
    {"id": "W034", "name": "Kisan Kendram", "lat": 11.0520, "lon": 75.9130},
    {"id": "W035", "name": "Kottuvalaparambu", "lat": 11.0520, "lon": 75.9210},
    {"id": "W036", "name": "Thrikkulam", "lat": 11.0600, "lon": 75.8970},
    {"id": "W037", "name": "Kottuvalakkad", "lat": 11.0600, "lon": 75.9050},
    {"id": "W038", "name": "Anithara", "lat": 11.0600, "lon": 75.9130},
    {"id": "W039", "name": "Pallippadi", "lat": 11.0600, "lon": 75.9210},
]

KERALA_FIXED_HOLIDAYS = {
    (1, 26),  # Republic Day
    (4, 14),  # Vishu
    (8, 15),  # Independence Day
    (10, 2),  # Gandhi Jayanti
    (12, 25),  # Christmas
}

def generate_collection_points():
    points = []
    for ward in TIRURANGADI_WARDS:
        for i in range(3):
            lat_offset = random.uniform(-0.01, 0.01)
            lon_offset = random.uniform(-0.01, 0.01)
            points.append({
                "name": f"{ward['name']} Point {i+1}",
                "ward_id": ward["id"],
                "ward_name": ward["name"],
                "latitude": ward["lat"] + lat_offset,
                "longitude": ward["lon"] + lon_offset,
                "max_capacity_liters": random.choice([300, 500, 750, 1000]),
                "current_fill_level": round(random.uniform(10, 95), 1),
            })
    return points

def generate_waste_history(days=180):
    history = []
    base_date = datetime.now() - timedelta(days=days)
    for day in range(days):
        current_date = base_date + timedelta(days=day)
        is_holiday = int((current_date.month, current_date.day) in KERALA_FIXED_HOLIDAYS)
        day_of_week = current_date.weekday()
        for ward in TIRURANGADI_WARDS:
            base_volume = random.uniform(2000, 3000)
            if day_of_week >= 5:
                base_volume *= 1.2
            if is_holiday:
                base_volume *= 1.4
            month = current_date.month
            if month in [8, 9]:
                base_volume *= 1.3
            noise = np.random.normal(0, 200)
            volume = max(200, base_volume + noise)
            history.append({
                "ward_id": ward["id"],
                "ward_name": ward["name"],
                "recorded_date": current_date,
                "actual_volume_kg": round(volume, 2),
                "temperature_celsius": round(random.uniform(22, 38), 1),
                "humidity_pct": round(random.uniform(30, 90), 1),
                "is_holiday": is_holiday,
            })
    return history

def generate_citizens(count=100):
    first_names = ["Amit", "Priya", "Rahul", "Sunita", "Vikram", "Anjali", "Rohit", "Kavya",
                   "Deepak", "Neha", "Sanjay", "Pooja", "Arun", "Meena", "Rajesh", "Divya"]
    last_names = ["Sharma", "Gupta", "Singh", "Kumar", "Verma", "Agarwal", "Yadav", "Joshi"]
    citizens = []
    for i in range(count):
        ward = random.choice(TIRURANGADI_WARDS)
        points = random.randint(0, 2500)
        tier = "Bronze"
        if points >= 2000:
            tier = "Platinum"
        elif points >= 1000:
            tier = "Gold"
        elif points >= 500:
            tier = "Silver"
        citizens.append({
            "name": f"{random.choice(first_names)} {random.choice(last_names)}",
            "ward_id": ward["id"],
            "ward_name": ward["name"],
            "total_points": points,
            "tier": tier,
        })
    return citizens

def generate_waste_classifications():
    classifications = []
    points = generate_collection_points()
    for point in points:
        organic = random.uniform(20, 60)
        plastic = random.uniform(10, 30)
        paper = random.uniform(5, 20)
        metal = random.uniform(2, 10)
        glass = random.uniform(2, 8)
        hazardous = random.uniform(1, 5)
        total = organic + plastic + paper + metal + glass + hazardous
        classifications.append({
            "ward_id": point["ward_id"],
            "organic_pct": round(organic/total*100, 2),
            "plastic_pct": round(plastic/total*100, 2),
            "paper_pct": round(paper/total*100, 2),
            "metal_pct": round(metal/total*100, 2),
            "glass_pct": round(glass/total*100, 2),
            "hazardous_pct": round(hazardous/total*100, 2),
            "total_volume_liters": round(random.uniform(50, 450), 1),
            "confidence_score": round(random.uniform(0.75, 0.98), 3),
        })
    return classifications
