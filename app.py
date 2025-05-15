# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/")
def home():
    return "Music Metadata API is running."

@app.route("/submit", methods=["POST"])
def submit_composition():
    data = request.json

    required_fields = [
        "title", "artist_name", "genre", "isrc_code", "composer_details"
    ]
    missing = [field for field in required_fields if not data.get(field)]

    if missing:
        return jsonify({"status": "error", "message": f"Missing fields: {', '.join(missing)}"}), 400

    # Simulate saving to DB (print to logs)
    print("Received Composition Data:")
    print(data)

    return jsonify({"status": "success", "message": "Composition submitted successfully."})

if __name__ == "__main__":
    app.run(debug=True)
