# 🧪 Flask Exercises — Countries API

These exercises build progressively on each other. Start with the code in `from the course material (22-working-with-rest-and-api's) provided earlier.

---

# how to contact my endpoints from the cli for these exercises:

Sure! Here’s a neat **curl instructions guide** you can share with your users for all the endpoints in your Flask app:

---

# Using `curl` to interact with the Countries API

### Base URL (assuming local dev server):

```
http://127.0.0.1:5000
```

---

## 1. Get all countries

**Request:**

```bash
curl http://127.0.0.1:5000/countries
```

**Description:**
Retrieve a list of all countries.

---

## 2. Add a new country

**Request:**

```bash
curl -X POST http://127.0.0.1:5000/countries \
  -H "Content-Type: application/json" \
  -d '{"name": "France", "capital": "Paris", "area": 551695}'
```

**Description:**
Add a new country by sending a JSON object with `name`, `capital`, and `area`.

---

## 3. Delete a country by ID

**Request:**

```bash
curl -X DELETE http://127.0.0.1:5000/countries/<id>
```

**Example: Delete country with ID 2**

```bash
curl -X DELETE http://127.0.0.1:5000/countries/2
```

**Description:**
Deletes the country with the given ID.

---

## 4. Search countries by capital city

**Request:**

```bash
curl "http://127.0.0.1:5000/countries/search?capital=Bangkok"
```

**Description:**
Search for countries where the capital matches the query parameter (case insensitive).

---

# Notes

* Replace `127.0.0.1:5000` with your server’s address if different.
* When adding a country, the JSON must include all fields: `name`, `capital`, `area`.
* Deleting a non-existent country ID returns an error.
* The search endpoint returns all countries with an exact match of the capital city.

---



==================================



## Exercise 1: Use CSV as a Data Source

### Goal

Replace the in-memory list `countries` with a CSV file that is used to load and store country data.

### Steps

1. Create a file named `countries.csv` with the following contents:

```csv
id,name,capital,area
1,Thailand,Bangkok,513120
2,Australia,Canberra,7617930
3,Egypt,Cairo,1010408
````

2. At the start of your Flask app, write a function to load countries from the CSV into a list of dictionaries.

3. When a new country is added via `POST /countries`, append it to the CSV file as well.

> Hint: You can use Python’s built-in `csv` module to read/write.

---

## Exercise 2: Implement DELETE Endpoint



### Goal

Create a new endpoint:

```
DELETE /countries/<int:id>
```

This endpoint should remove a country with the given ID.

Bonus objective here. see if you can also implement a `PUT`/`PATCH` route to update existing countries.

### Steps

1. Read the data from the CSV file.
2. Remove the matching country by ID.
3. Write the updated list back to the CSV file.
4. Return a 204 No Content status if successful.
5. If the ID is not found, return a 404 error.

---

## Exercise 3: Search for Countries

### Goal

Add support for querying countries based on capital name.

### Endpoint

```
GET /countries/search?capital=Cairo
```

### Steps

1. Add a new route `/countries/search` that accepts a `capital` query parameter.
2. Filter the list of countries (loaded from CSV) where the capital matches the query (case-insensitive).
3. Return the matched country or a 404 error if none is found.

HINT:
a search param in an url is denoted by a `?` followed by the key-value pair, e.g., `?router=lala1234`.
---

Good luck, and don’t forget to test your code using `curl` or Postman! (if you have that knowledge)

````








