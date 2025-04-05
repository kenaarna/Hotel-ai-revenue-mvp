from flask import Flask, jsonify
from datetime import date, timedelta
import random
import os

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
        {"name": "Local Festival", "start_date": "2025-04-05", "end_date": "2025-04-06"},
        {"name": "Business Conference", "start_date": "2025-04-07", "end_date": "2025-04-08"}
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
        "Standard": {"current": 120, "suggested": 135},
        "Deluxe": {"current": 150, "suggested": 175},
        "Suite": {"current": 220, "suggested": 240}
    }

@app.route("/dashboard")
def dashboard():
    return jsonify({
        "forecast": generate_forecast(),
        "events": get_local_events(),
        "pricing": calculate_prices(),
        "bookings": generate_sample_bookings()
    })

# New API endpoints
@app.route("/api/forecast")
def api_forecast():
    return jsonify(generate_forecast())

@app.route("/api/events")
def api_events():
    return jsonify(get_local_events())

@app.route("/api/bookings")
def api_bookings():
    return jsonify(generate_sample_bookings())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

    
