from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample data for fresh water areas and heat hotspots
data = [
    {
        "lat": 34.0522,
        "lng": -118.2437,
        "type": "fresh_water",
        "description": "Los Angeles River"
    },
    {
        "lat": 34.0523,
        "lng": -118.2585,
        "type": "heat",
        "description": "Downtown Heat Zone"
    },
    {
        "lat": 34.0525,
        "lng": -118.2332,
        "type": "fresh_water",
        "description": "Griffith Park Lake"
    },
    {
        "lat": 34.0491,
        "lng": -118.2583,
        "type": "heat",
        "description": "High Temperature Area"
    }
]

@app.route("/")
def index():
    return render_template("map.html")

@app.route("/data")
def get_data():
    return jsonify(data)

@app.route("/submit", methods=["POST"])
def submit_data():
    new_entry = request.json
    data.append(new_entry)
    return jsonify({"message": "Data submitted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
