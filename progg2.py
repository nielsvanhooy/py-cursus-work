import csv
import os
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

CSV_FILE = "countries.csv"
FIELDNAMES = ["id", "name", "capital", "area"]

def initialize_csv():
    """Create CSV file with headers if it doesn't exist"""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            writer.writeheader()

def load_countries():
    """Load all countries from CSV file"""
    initialize_csv()
    try:
        with open(CSV_FILE, newline="", encoding='utf-8') as csvfile:
            return list(csv.DictReader(csvfile))
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading countries: {e}")
        return []

def save_all_countries(countries):
    """Save all countries to CSV file"""
    try:
        with open(CSV_FILE, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(countries)
    except Exception as e:
        print(f"Error saving countries: {e}")
        raise

def save_country(country):
    """Append a single country to CSV file"""
    try:
        with open(CSV_FILE, "a", newline="", encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            writer.writerow(country)
    except Exception as e:
        print(f"Error saving country: {e}")
        raise

def _find_next_id(countries):
    """Find the next available ID"""
    if not countries:
        return 1
    try:
        return max(int(c["id"]) for c in countries if c["id"].isdigit()) + 1
    except (ValueError, KeyError):
        return 1

def validate_country_data(data):
    """Validate country data"""
    required_fields = {"name", "capital", "area"}

    if not isinstance(data, dict):
        return False, "Invalid data format"

    missing_fields = required_fields - set(data.keys())
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"

    # Validate data types and values
    if not isinstance(data["name"], str) or not data["name"].strip():
        return False, "Name must be a non-empty string"

    if not isinstance(data["capital"], str) or not data["capital"].strip():
        return False, "Capital must be a non-empty string"

    try:
        area = float(data["area"])
        if area <= 0:
            return False, "Area must be a positive number"
    except (ValueError, TypeError):
        return False, "Area must be a valid number"

    return True, None

@app.route("/")
def home():
    """Home endpoint with API information"""
    return jsonify({
        "message": "Countries API",
        "endpoints": {
            "GET /countries": "Get all countries",
            "POST /countries": "Add a new country",
            "DELETE /countries/<id>": "Delete a country by ID",
            "GET /countries/search?capital=<name>": "Search countries by capital"
        }
    })

@app.route("/countries", methods=["GET"])
def get_countries():
    """Get all countries"""
    try:
        countries = load_countries()
        return jsonify(countries)
    except Exception:
        return make_response(jsonify({"error": "Failed to load countries"}), 500)

@app.route("/countries", methods=["POST"])
def add_country():
    """Add a new country"""
    if not request.is_json:
        return make_response(jsonify({"error": "Request must be JSON"}), 415)

    data = request.get_json()

    # Validate input data
    is_valid, error_msg = validate_country_data(data)
    if not is_valid:
        return make_response(jsonify({"error": error_msg}), 400)

    try:
        countries = load_countries()

        # Check if country already exists
        existing_country = any(
            c["name"].lower() == data["name"].lower()
            for c in countries
        )
        if existing_country:
            return make_response(jsonify({"error": "Country already exists"}), 409)

        new_country = {
            "id": str(_find_next_id(countries)),
            "name": data["name"].strip(),
            "capital": data["capital"].strip(),
            "area": str(float(data["area"]))  # Normalize the area value
        }

        save_country(new_country)
        return make_response(jsonify(new_country), 201)

    except Exception:
        return make_response(jsonify({"error": "Failed to add country"}), 500)

@app.route("/countries/<int:country_id>", methods=["DELETE"])
def delete_country(country_id):
    """Delete a country by ID"""
    try:
        countries = load_countries()
        original_count = len(countries)

        filtered_countries = [c for c in countries if int(c["id"]) != country_id]

        if len(filtered_countries) == original_count:
            return make_response(jsonify({"error": "Country not found"}), 404)

        save_all_countries(filtered_countries)
        return make_response("", 204)

    except Exception:
        return make_response(jsonify({"error": "Failed to delete country"}), 500)

@app.route("/countries/<int:country_id>", methods=["GET"])
def get_country(country_id):
    """Get a specific country by ID"""
    try:
        countries = load_countries()
        country = next((c for c in countries if int(c["id"]) == country_id), None)

        if not country:
            return make_response(jsonify({"error": "Country not found"}), 404)

        return jsonify(country)

    except Exception:
        return make_response(jsonify({"error": "Failed to get country"}), 500)

@app.route("/countries/<int:country_id>", methods=["PUT"])
def update_country(country_id):
    """Update a country by ID"""
    if not request.is_json:
        return make_response(jsonify({"error": "Request must be JSON"}), 415)

    data = request.get_json()

    # Validate input data
    is_valid, error_msg = validate_country_data(data)
    if not is_valid:
        return make_response(jsonify({"error": error_msg}), 400)

    try:
        countries = load_countries()
        country_index = next(
            (i for i, c in enumerate(countries) if int(c["id"]) == country_id),
            None
        )

        if country_index is None:
            return make_response(jsonify({"error": "Country not found"}), 404)

        # Check if name conflicts with another country
        existing_country = any(
            c["name"].lower() == data["name"].lower() and int(c["id"]) != country_id
            for c in countries
        )
        if existing_country:
            return make_response(jsonify({"error": "Country name already exists"}), 409)

        # Update the country
        countries[country_index] = {
            "id": str(country_id),
            "name": data["name"].strip(),
            "capital": data["capital"].strip(),
            "area": str(float(data["area"]))
        }

        save_all_countries(countries)
        return jsonify(countries[country_index])

    except Exception:
        return make_response(jsonify({"error": "Failed to update country"}), 500)

@app.route("/countries/search", methods=["GET"])
def search_by_capital():
    """Search countries by capital city"""
    capital = request.args.get("capital", "").strip()

    if not capital:
        return make_response(jsonify({"error": "Capital parameter is required"}), 400)

    try:
        countries = load_countries()
        matches = [
            c for c in countries
            if c["capital"].lower() == capital.lower()
        ]

        if not matches:
            return make_response(jsonify({"error": "No country found with that capital"}), 404)

        return jsonify(matches)

    except Exception:
        return make_response(jsonify({"error": "Failed to search countries"}), 500)

@app.route("/countries/search/name", methods=["GET"])
def search_by_name():
    """Search countries by name (partial match)"""
    name = request.args.get("name", "").strip()

    if not name:
        return make_response(jsonify({"error": "Name parameter is required"}), 400)

    try:
        countries = load_countries()
        matches = [
            c for c in countries
            if name.lower() in c["name"].lower()
        ]

        if not matches:
            return make_response(jsonify({"error": "No countries found matching that name"}), 404)

        return jsonify(matches)

    except Exception:
        return make_response(jsonify({"error": "Failed to search countries"}), 500)

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return make_response(jsonify({"error": "Endpoint not found"}), 404)

@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors"""
    return make_response(jsonify({"error": "Method not allowed"}), 405)

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return make_response(jsonify({"error": "Internal server error"}), 500)

if __name__ == "__main__":
    # Initialize CSV file on startup
    initialize_csv()

    # Run the app
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )