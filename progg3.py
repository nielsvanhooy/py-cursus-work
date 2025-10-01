# app.py
from flask import Flask, request, jsonify, make_response
from urllib3.poolmanager import key_fn_by_scheme

app = Flask(__name__)
import csv


countries = []
    # {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    # {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    # {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
# id,name,capital,area
# 1,Thailand,Bangkok,513120
# 2,Australia,Canberra,7617930
# 3,Egypt,Cairo,1010408

@app.get("/nextid")
def _find_next_id():
    list_ids=[]
    with open('countries.csv','r',newline='') as csvfile:
        fieldnames=("id","name","capital","area")
        countries = csv.DictReader(csvfile, delimiter=',',fieldnames=fieldnames)
        for (column) in countries:
            list_ids.append(column["id"])
        if len(list_ids) == 0:
            current_id=0
            maak_kop = "ja"
        elif len(list_ids) == 1:
            current_id=0
            maak_kop = "nee"
        else:
            current_id=int(max(list_ids[1:]))
            maak_kop = "nee"
        next_id = current_id + 1
        return next_id,maak_kop

@app.get("/countries")
def get_countries():
    countries=[]
    with open('countries.csv', newline='') as csvfile:
        content = csv.DictReader(csvfile)
        # reader = dict
        # next(reader)
        for row in content:
            countries.append(row)
    return jsonify(countries)

@app.post("/countries")
def add_country():
    if not request.is_json:
        return make_response(jsonify({"error": "Request must be JSON"}), 415)

    data = request.get_json()

    required_fields = {"name", "capital", "area"}
    if not required_fields.issubset(data):
        return make_response(jsonify({"error": f"Missing fields: {required_fields - data.keys()}"}), 400)

    next_id,maak_kop = _find_next_id()
    country = {
        "id": next_id,
        "name": data["name"],
        "capital": data["capital"],
        "area": data["area"]
    }

    with open('countries.csv', 'a', newline='') as csvfile:
        fieldnames=country.keys()
        file = csv.DictWriter(csvfile, fieldnames=fieldnames )
        if maak_kop == "ja":
            file.writeheader()
        file.writerow(country)
    return make_response(jsonify(country), 201)

@app.delete("/countries/delete/<int:id>")
def delete_country(id):
    with open("countries.csv", "r") as csvfile:
        lines = csv.DictReader(csvfile, delimiter=",")
        cities=list(lines)
        kopregel=(cities[0].keys())

    with open("countries.csv", "w") as csvfile:
        fieldnames=kopregel
        newfile = csv.DictWriter(csvfile, fieldnames=kopregel )
        newfile.writeheader()
        for line in cities:
            if (int(list(line.values())[0])) != id:
                newfile.writerow(line)

    return make_response("", 204)


if __name__ == "__main__":
    app.run(debug=True)