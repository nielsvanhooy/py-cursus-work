import csv
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)
CSV_FILE = "countries.csv"

FIELDNAMES = ["id", "name", "capital", "area"]

def load_countries():
    with open(CSV_FILE, newline="") as csvfile:
        return list(csv.DictReader(csvfile))

def save_all_countries(countries):
    with open(CSV_FILE, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(countries)

def save_country(country):
    with open(CSV_FILE, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writerow(country)

def _find_next_id(countries):
    return max(int(c["id"]) for c in countries) + 1 if countries else 1

@app.get("/countries")
def get_countries():
    return jsonify(load_countries())

@app.post("/countries")
def add_country():
    if not request.is_json:
        return make_response(jsonify({"error": "Request must be JSON"}), 415)

    data = request.get_json()
    required_fields = {"name", "capital", "area"}

    if not required_fields.issubset(data):
        return make_response(jsonify({"error": f"Missing fields: {required_fields - data.keys()}"}), 400)

    countries = load_countries()
    new_country = {
        "id": str(_find_next_id(countries)),
        "name": data["name"],
        "capital": data["capital"],
        "area": str(data["area"])
    }

    save_country(new_country)
    return make_response(jsonify(new_country), 201)

@app.delete("/countries/<int:country_id>")
def delete_country(country_id):
    countries = load_countries()
    filtered = [c for c in countries if int(c["id"]) != country_id]

    if len(filtered) == len(countries):
        return make_response(jsonify({"error": "Country not found"}), 404)

    save_all_countries(filtered)
    return "", 204

@app.get("/countries/search")
def search_by_capital():
    capital = request.args.get("capital", "").lower()
    countries = load_countries()
    matches = [c for c in countries if c["capital"].lower() == capital]

    if not matches:
        return make_response(jsonify({"error": "No country found"}), 404)

    return jsonify(matches)

if __name__ == "__main__":
    app.run(debug=True)
