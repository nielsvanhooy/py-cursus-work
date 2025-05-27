### 📄 `solutions.md`

```markdown
# ✅ Solutions — Countries API

---

## Exercise 1: Use CSV as a Data Source

### 1. `countries.csv`

```csv
id,name,capital,area
1,Thailand,Bangkok,513120
2,Australia,Canberra,7617930
3,Egypt,Cairo,1010408
````

### 2. Updated `app.py`

```python
import csv
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)
CSV_FILE = "countries.csv"

def load_countries():
    with open(CSV_FILE, newline="") as csvfile:
        return list(csv.DictReader(csvfile))

def save_country(country):
    with open(CSV_FILE, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["id", "name", "capital", "area"])
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
    country = {
        "id": str(_find_next_id(countries)),
        "name": data["name"],
        "capital": data["capital"],
        "area": str(data["area"])
    }
    save_country(country)
    return make_response(jsonify(country), 201)
```

---

## Exercise 2: Implement DELETE Endpoint

### Add this to the same `app.py`

```python
@app.delete("/countries/<int:country_id>")
def delete_country(country_id):
    countries = load_countries()
    filtered = [c for c in countries if int(c["id"]) != country_id]

    if len(filtered) == len(countries):
        return make_response(jsonify({"error": "Country not found"}), 404)

    with open(CSV_FILE, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["id", "name", "capital", "area"])
        writer.writeheader()
        writer.writerows(filtered)

    return "", 204
```

---

## Exercise 3: Search for Countries by Capital

### Add this route to `app.py`

```python
@app.get("/countries/search")
def search_by_capital():
    capital = request.args.get("capital", "").lower()
    countries = load_countries()
    matches = [c for c in countries if c["capital"].lower() == capital]

    if not matches:
        return make_response(jsonify({"error": "No country found"}), 404)

    return jsonify(matches)
```