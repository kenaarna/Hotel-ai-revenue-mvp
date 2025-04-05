
# app.py (Flask Backend)
from flask import Flask, jsonify
from datetime import date, timedelta
import random

app = Flask(__name__)

# Simulated data generators
def generate_sample_bookings():
    room_types = ['Standard', 'Deluxe', 'Suite']
    bookings = []
    base_date = date.today()
    for i in range(10):
        day = base_date - timedelta(days=i)
        for _ in range(random.randint(1, 4)):
            bookings.append({
                "date": str(day),
                "room_type": random.choice(room_types),
                "price": round(random.uniform(90, 250), 2)
            })
    return bookings

def get_local_events():
    return [
        {"name": "Local Festival", "start_date": "2025-04-05", "end_date": "2025-04-06", "impact": 0.25},
        {"name": "Business Conference", "start_date": "2025-04-07", "end_date": "2025-04-08", "impact": 0.15}
    ]

def generate_forecast():
    forecast = []
    base_date = date.today()
    for i in range(5):
        d = base_date + timedelta(days=i)
        occ = random.randint(45, 99)
        forecast.append({"date": str(d), "occupancy": occ})
    return forecast

def calculate_prices():
    return {
        "Standard": {"current": 120, "suggested": 132},
        "Deluxe": {"current": 150, "suggested": 177},
        "Suite": {"current": 220, "suggested": 248},
    }

@app.route("/dashboard")
def dashboard():
    return jsonify({
        "forecast": generate_forecast(),
        "events": get_local_events(),
        "pricing": calculate_prices(),
        "bookings": generate_sample_bookings()
    })

if __name__ == '__main__':
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
