Table of Contents

*   [REST APIs and Web Services](#rest-apis-and-web-services)
    *   [HTTP Methods](#http-methods)
    *   [Status Codes](#status-codes)
    *   [API Endpoints](#api-endpoints)
*   [REST and Python: Consuming APIs](#rest-and-python-consuming-apis)
    *   [GET](#get)
    *   [POST](#post)
    *   [PUT](#put)
    *   [PATCH](#patch)
    *   [DELETE](#delete)
*   [REST and Python: Building APIs](#rest-and-python-building-apis)
    *   [Identify Resources](#identify-resources)
    *   [Define Your Endpoints](#define-your-endpoints)
    *   [Pick Your Data Interchange Format](#pick-your-data-interchange-format)
    *   [Design Success Responses](#design-success-responses)
    *   [Design Error Responses](#design-error-responses)
*   [REST and Python: Tools of the Trade](#rest-and-python-tools-of-the-trade)
    *   [Flask](#flask)
    *   [Litestar Framework](#litestar-framework)



## REST APIs and Web Services[](#rest-apis-and-web-services "Permanent link")

What is a REST API.
an application programming interface (API) that follows the design principles of the REST architectural style


A **REST web service** is any web service that adheres to REST architecture constraints. These web services expose their data to the outside world through an API. REST APIs provide access to web service data through public web URLs.


### HTTP Methods[](#http-methods "Permanent link")

REST APIs listen for [HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) like `GET`, `POST`, and `DELETE` to know which operations to perform on the web service’s resources. A **resource** is any data available in the web service that can be accessed and manipulated with **HTTP requests** to the REST API. The HTTP method tells the API which action to perform on the resource.

While there are many HTTP methods, the five methods listed below are the most commonly used with REST APIs:

| HTTP method | Description |
| --- | --- |
| `GET` | Retrieve an existing resource. |
| `POST` | Create a new resource. |
| `PUT` | Update an existing resource. |
| `PATCH` | Partially update an existing resource. |
| `DELETE` | Delete a resource. |

A REST API client application can use these five HTTP methods to manage the state of resources in the web service.

### Status Codes[](#status-codes "Permanent link")

Once a REST API receives and processes an HTTP request, it will return an **HTTP response**. 
Included in this response is an **HTTP status code**. 
This code provides information about the results of the request. 

An application sending requests to the API can check the status code and perform actions based on the result. 
These actions could include handling errors or displaying a success message to a user.

Below is a list of the most common status codes returned by REST APIs:

| Code | Meaning | Description |
| --- | --- | --- |
| `200` | OK  | The requested action was successful. |
| `201` | Created | A new resource was created. |
| `202` | Accepted | The request was received, but no modification has been made yet. |
| `204` | No Content | The request was successful, but the response has no content. |
| `400` | Bad Request | The request was malformed. |
| `401` | Unauthorized | The client is not authorized to perform the requested action. |
| `404` | Not Found | The requested resource was not found. |
| `415` | Unsupported Media Type | The request data format is not supported by the server. |
| `422` | Unprocessable Entity | The request data was properly formatted but contained invalid or missing data. |
| `500` | Internal Server Error | The server threw an error when processing the request. |

These ten status codes represent only a small subset of the available [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). Status codes are numbered based on the category of the result:

| Code range | Category |
| --- | --- |
| `2xx` | Successful operation |
| `3xx` | Redirection |
| `4xx` | Client error |
| `5xx` | Server error |

HTTP status codes come in handy when working with REST APIs as you’ll often need to perform different logic based on the results of the request.

### API Endpoints[](#api-endpoints "Permanent link")

A REST API exposes a set of public URLs that client applications use to access the resources of a web service. These URLs, in the context of an API, are called **endpoints**.

To help clarify this, take a look at the table below. 
In this table, you’ll see API endpoints for a hypothetical [CRM](https://en.wikipedia.org/wiki/Customer_relationship_management) system. 

These endpoints are for a customer resource that represents potential `customers` in the system:

| HTTP method | API endpoint | Description |
| --- | --- | --- |
| `GET` | `/customers` | Get a list of customers. |
| `GET` | `/customers/<customer_id>` | Get a single customer. |
| `POST` | `/customers` | Create a new customer. |
| `PUT` | `/customers/<customer_id>` | Update a customer. |
| `PATCH` | `/customers/<customer_id>` | Partially update a customer. |
| `DELETE` | `/customers/<customer_id>` | Delete a customer. |

Each of the endpoints above performs a different action based on the HTTP method.

**Note:** The base URL for the endpoints has been omitted for brevity. 
In reality, you’ll need the full URL path to access an API endpoint:

`https://api.example.com/customers`

This is the full URL you’d use to access this endpoint. The base URL is everything besides `/customers`.

You’ll note that some endpoints have `<customer_id>` at the end. This notation means you need to append a numeric `customer_id` to the URL to tell the REST API which `customer` you’d like to work with.

The endpoints listed above represent only one resource in the system. Production-ready REST APIs often have tens or even hundreds of different endpoints to manage the resources in the web service.


## REST and Python: Consuming APIs[](#rest-and-python-consuming-apis "Permanent link")

To write code that interacts with REST APIs, most Python developers turn to [`requests`](https://realpython.com/python-requests/) to send HTTP requests. This library abstracts away the complexities of making HTTP requests. It’s one of the few projects worth treating as if it’s part of the standard library.

To start using `requests`, you need to install it first. You can use [`pip`](https://realpython.com/what-is-pip/) to install it:

Shell

```bash
python -m pip install requests
```
or if working in a virtual environment: activate it first. 
(make sure you are in the correct directory that has a .venv folder)

```bash
source venv/bin/activate
```

Now that you’ve got `requests` installed, you can start sending HTTP requests.

### GET[](#get "Permanent link")

`GET` is one of the most common HTTP methods you’ll use when working with REST APIs. This method allows you to retrieve resources from a given API. `GET` is a **read-only** operation, so you shouldn’t use it to modify an existing resource.

To test out `GET` and the other methods in this section, you’ll use a service called [JSONPlaceholder](https://jsonplaceholder.typicode.com/). This free service provides fake API endpoints that send back responses that `requests` can process.

Python

```python
import requests 
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.json())

{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
```

This code calls `requests.get()` to send a `GET` request to `/todos/1`, which responds with the `todo` item with the ID `1`. Then you can call [`.json()`](https://docs.python-requests.org/en/master/user/quickstart/#json-response-content) on the `response` object to view the data that came back from the API.

The response data is formatted as [JSON](https://www.json.org/json-en.html), a key-value store similar to a [Python dictionary](https://realpython.com/python-dicts/). It’s a very popular data format and the de facto interchange format for most REST APIs.

Beyond viewing the JSON data from the API, you can also view other things about the `response`:

Python

```python
import requests 
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.json())

print(response.status_code)  
print(response.headers["Content-Type"])

```
Here, you access `response.status_code` to see the HTTP status code. You can also view the response’s [HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) with `response.headers`. 
This dictionary contains metadata about the response, such as the `Content-Type` of the response.

### POST[](#post "Permanent link")

Now, take a look at how you use `requests` to `POST` data to a REST API to create a new resource. 
You’ll use JSONPlaceholder again, but this time you’ll include JSON data in the request. 
Here’s the data that you’ll send:

JSON

```javascript
{"userId": 1, "title": "Buy milk", "completed": false }
```

This JSON contains information for a new `todo` item. 
Back in your IDE. run the following code to create the new `todo`:

Python
```python
import requests

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}

response = requests.post(api_url, json=todo)
print(response.json())
print(response.status_code)

```

Here, you call `requests.post()` to create a new `todo` in the system.

First, you create a dictionary containing the data for your `todo`. 
Then you pass this dictionary to the `json` keyword argument of `requests.post()`. 
When you do this, `requests.post()` automatically sets the request’s HTTP header `Content-Type` to `application/json`. 
It also serializes `todo` into a JSON string, which it appends to the body of the request.

If you don’t use the `json` keyword argument to supply the JSON data, 
then you need to set `Content-Type` accordingly and serialize the JSON manually.

Here’s an equivalent version to the previous code:
when using stuff like stackoverflow. you would usually the equivelant like below.

Python

```python
import requests
import json


api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers =  {"Content-Type":"application/json"}


response = requests.post(api_url, data=json.dumps(todo), headers=headers)
print(response.json())
print(response.status_code)

```

`
In this code, you add a `headers` dictionary that contains a single header `Content-Type` set to `application/json`. 
This tells the REST API that you’re sending JSON data with the request.

You then call `requests.post()`, but instead of passing `todo` to the `json` argument, you first call `json.dumps(todo)` to serialize it. 
After it’s serialized, you pass it to the `data` keyword argument. The `data` argument tells `requests` what data to include in the request. 
You also pass the `headers` dictionary to `requests.post()` to set the HTTP headers manually.

When you call `requests.post()` like this, it has the same effect as the previous code but gives you more control over the request.

**Note:** [`json.dumps()`](https://docs.python.org/3/library/json.html#json.dumps) comes from the [`json`](https://docs.python.org/3/library/json.html) package in the standard library. This package provides useful methods for working with [JSON in Python](https://realpython.com/python-json/).

Once the API responds, you call `response.json()` to view the JSON. The JSON includes a generated `id` for the new `todo`. The `201` status code tells you that a new resource was created.


### PUT[](#put "Permanent link")

Beyond `GET` and `POST`, `requests` provides support for all the other HTTP methods you would use with a REST API. 
The following code sends a `PUT` request to update an existing `todo` with new data. 
Any data sent with a `PUT` request will completely replace the existing values of the `todo`.

You’ll use the same JSONPlaceholder endpoint you used with `GET` and `POST`, but this time you’ll append `10` to the end of the URL. 
This tells the REST API which `todo` you’d like to update:

Python

```python
import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10" 
response = requests.get(api_url) 
print(response.json())
# now look closely at the output
# lets make a PUT request to update the todo
todo = {"userId": 1, "title": "Wash car", "completed": True}

response = requests.put(api_url, json=todo)
print(response.json())
print(response.status_code)
```


Here, you first call `requests.get()` to view the contents of the existing `todo`. 
Next, you call `requests.put()` with new JSON data to replace the existing to-do’s values. 
You can see the new values when you call `response.json()`. 
Successful `PUT` requests will always return `200` instead of `201` because you aren’t creating a new resource but just updating an existing one.

### PATCH[](#patch "Permanent link")

Next up, you’ll use `requests.patch()` to modify the value of a specific field on an existing `todo`. 
`PATCH` differs from `PUT` in that it doesn’t completely replace the existing resource. 
It only modifies the values set in the JSON sent with the request.

You’ll use the same `todo` from the last example to try out `requests.patch()`. 
Here are the current values:

Python

```python
{'userId': 1, 'title': 'Wash car', 'completed': True, 'id': 10}
```

Now you can update the `title` with a new value:

Python

```python
import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10" 
todo = {"title": "Mow lawn"}
response = requests.patch(api_url, json=todo)
print(response.json())
print(response.status_code)

```


When you call `response.json()`, you can see that `title` was updated to `Mow lawn`.

### DELETE[](#delete "Permanent link")

Last but not least, if you want to completely remove a resource, then you use `DELETE`. 
Here’s the code to remove a `todo`:

Python

```python
import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
print(response.json())
print(response.status_code)

```


You call `requests.delete()` with an API URL that contains the ID for the `todo` you would like to remove. This sends a `DELETE` request to the REST API, which then removes the matching resource. After deleting the resource, the API sends back an empty JSON object indicating that the resource has been deleted.

The `requests` library is an awesome tool for working with REST APIs and an indispensable part of your Python tool belt. In the next section, you’ll change gears and consider what it takes to build a REST API.

## REST and Python: Building APIs[](#rest-and-python-building-apis "Permanent link")

REST API design is a huge topic with many layers. As with most things in technology, there’s a wide range of opinions on the best approach to building APIs. In this section, you’ll look at some recommended steps to follow as you build an API.

### Identify Resources[](#identify-resources "Permanent link")

The first step you’ll take as you build a REST API is to identify the resources the API will manage. It’s common to describe these resources as plural nouns, like `customers`, `events`, or `transactions`. As you identify different resources in your web service, you’ll build out a list of nouns that describe the different data users can manage in the API.

As you do this, make sure to consider any nested resources. For example, `customers` may have `sales`, or `events` may contain `guests`. Establishing these resource hierarchies will help when you define API endpoints.


### Define Your Endpoints[](#define-your-endpoints "Permanent link")

Once you’ve identified the resources in your web service, you’ll want to use these to define the API endpoints. Here are some example endpoints for a `transactions` resource you might find in an API for a payment processing service:

| HTTP method | API endpoint | Description |
| --- | --- | --- |
| `GET` | `/transactions` | Get a list of transactions. |
| `GET` | `/transactions/<transaction_id>` | Get a single transaction. |
| `POST` | `/transactions` | Create a new transaction. |
| `PUT` | `/transactions/<transaction_id>` | Update a transaction. |
| `PATCH` | `/transactions/<transaction_id>` | Partially update a transaction. |
| `DELETE` | `/transactions/<transaction_id>` | Delete a transaction. |

These six endpoints cover all the operations that you’ll need to create, read, update, and delete `transactions` in the web service. 
Each resource in your web service would have a similar list of endpoints based on what actions a user can perform with the API.

**Note:** An endpoint shouldn’t contain verbs. 
Instead, you should select the appropriate HTTP methods to convey the endpoint’s action. 
For example, the endpoint below contains an unneeded verb:

HTTP

`GET /getTransactions`

Here, `get` is included in the endpoint when it isn’t needed. The HTTP method `GET` already provides the semantic meaning for the endpoint by indicating the action. You can remove `get` from the endpoint:

HTTP

`GET /transactions`

This endpoint contains only a plural noun, and the HTTP method `GET` communicates the action.

Now take a look at an example of endpoints for a nested resource. Here, you’ll see endpoints for `guests` that are nested under `events` resources:

| HTTP method | API endpoint | Description |
| --- | --- | --- |
| `GET` | `/events/<event_id>/guests` | Get a list of guests. |
| `GET` | `/events/<event_id>/guests/<guest_id>` | Get a single guest. |
| `POST` | `/events/<event_id>/guests` | Create a new guest. |
| `PUT` | `/events/<event_id>/guests/<guest_id>` | Update a guest. |
| `PATCH` | `/events/<event_id>/guests/<guest_id>` | Partially update a guest. |
| `DELETE` | `/events/<event_id>/guests/<guest_id>` | Delete a guest. |

With these endpoints, you can manage `guests` for a specific event in the system.

This isn’t the only way to define an endpoint for nested resources. Some people prefer to use [query strings](https://en.wikipedia.org/wiki/Query_string) to access a nested resource. A query string allows you to send additional parameters with your HTTP request. In the following endpoint, you append a query string to get `guests` for a specific `event_id`:

HTTP

`GET /guests?event_id=23`

This endpoint will filter out any `guests` that don’t reference the given `event_id`. As with many things in API design, you need to decide which method fits your web service best.

**Note:** It’s very unlikely that your REST API will stay the same throughout the life of your web service. Resources will change, and you’ll need to update your endpoints to reflect these changes. This is where **API versioning** comes in. API versioning allows you to modify your API without fear of breaking existing integrations.

There’s a wide range of versioning strategies. Selecting the right option depends on the requirements of your API. Below are some of the most popular options for API versioning:

*   [URI versioning](https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design#uri-versioning)
*   [HTTP header versioning](https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design#header-versioning)
*   [Query string versioning](https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design#query-string-versioning)
*   [Media type versioning](https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design#media-type-versioning)

No matter what strategy you select, versioning your API is an important step to ensuring it can adapt to changing requirements while supporting existing users.

Now that you’ve covered endpoints, in the next section you’ll look at some options for formatting data in your REST API.

### Pick Your Data Interchange Format[](#pick-your-data-interchange-format "Permanent link")

Two popular options for formatting web service data are [XML](https://en.wikipedia.org/wiki/XML) and JSON. Traditionally, XML was very popular with [SOAP](https://en.wikipedia.org/wiki/SOAP) APIs, but JSON is more popular with REST APIs. To compare the two, take a look at an example `book` resource formatted as XML and JSON.

Here’s the book formatted as XML:

XML

`<?xml version="1.0" encoding="UTF-8" ?> <book>     <title>Python Basics</title>     <page_count>635</page_count>     <pub_date>2021-03-16</pub_date>     <authors>         <author>             <name>David Amos</name>         </author>         <author>             <name>Joanna Jablonski</name>         </author>         <author>             <name>Dan Bader</name>         </author>         <author>             <name>Fletcher Heisler</name>         </author>     </authors>     <isbn13>978-1775093329</isbn13>     <genre>Education</genre> </book>`

XML uses a series of **elements** to encode data. Each element has an opening and closing tag, with the data in between. Elements can be nested inside other elements. You can see this above, where several `<author>` tags are nested inside of `<authors>`.

Now, take a look at the same `book` in JSON:

JSON

`{     "title": "Python Basics",     "page_count": 635,     "pub_date": "2021-03-16",     "authors": [         {"name": "David Amos"},         {"name": "Joanna Jablonski"},         {"name": "Dan Bader"},         {"name": "Fletcher Heisler"}     ],     "isbn13": "978-1775093329",     "genre": "Education" }`

JSON stores data in key-value pairs similar to a Python dictionary. Like XML, JSON supports nesting data to any level, so you can model complex data.

Neither JSON nor XML is inherently better than the other, but there’s a preference for JSON among REST API developers. This is especially true when you pair a REST API with a front-end framework like [React](https://reactjs.org/) or [Vue](https://vuejs.org/).


### Design Success Responses[](#design-success-responses "Permanent link")

Once you’ve picked a data format, the next step is to decide how you’ll respond to HTTP requests. All responses from your REST API should have a similar format and include the proper HTTP status code.

In this section, you’ll look at some example HTTP responses for a hypothetical API that manages an inventory of `cars`. These examples will give you a sense of how you should format your API responses. To make things clear, you’ll look at raw HTTP requests and responses instead of using an HTTP library like `requests`.

To start things off, take a look at a `GET` request to `/cars`, which returns a list of `cars`:

HTTP

`GET /cars HTTP/1.1 Host: api.example.com`

This HTTP request is made up of four parts:

1.  **`GET`** is the HTTP method type.
2.  **`/cars`** is the API endpoint.
3.  **`HTTP/1.1`** is the HTTP version.
4.  **`Host: api.example.com`** is the API host.

These four parts are all you need to send a `GET` request to `/cars`. Now take a look at the response. This API uses JSON as the data interchange format:

HTTP

`HTTP/1.1 200 OK Content-Type: application/json ...  [     {         "id": 1,         "make": "GMC",         "model": "1500 Club Coupe",         "year": 1998,         "vin": "1D7RV1GTXAS806941",         "color": "Red"     },     {         "id": 2,         "make": "Lamborghini",         "model":"Gallardo",         "year":2006,         "vin":"JN1BY1PR0FM736887",         "color":"Mauve"     },     {         "id": 3,         "make": "Chevrolet",         "model":"Monte Carlo",         "year":1996,         "vin":"1G4HP54K714224234",         "color":"Violet"     } ]`

The API returns a response that contains a list of `cars`. You know that the response was successful because of the `200 OK` status code. The response also has a `Content-Type` header set to `application/json`. This tells the user to parse the response as JSON.

**Note:** When you’re working with a real API, you’re going to see more HTTP headers than this. These headers differ between APIs, so they’ve been excluded in these examples.

It’s important to always set the correct `Content-Type` header on your response. If you send JSON, then set `Content-Type` to `application/json`. If XML, then set it to `application/xml`. This header tells the user how they should parse the data.

You also want to include an appropriate status code in your response. For any successful `GET` request, you should return `200 OK`. This tells the user that their request was processed as expected.

Take a look at another `GET` request, this time for a single car:

HTTP

`GET /cars/1 HTTP/1.1 Host: api.example.com`

This HTTP request queries the API for car `1`. Here’s the response:

HTTP

`HTTP/1.1 200 OK Content-Type: application/json  {     "id": 1,     "make": "GMC",     "model": "1500 Club Coupe",     "year": 1998,     "vin": "1D7RV1GTXAS806941",     "color": "Red" },`

This response contains a single JSON object with the car’s data. Since it’s a single object, it doesn’t need to be wrapped in a list. Like the last response, this also has a `200 OK` status code.

**Note:** A `GET` request should never modify an existing resource. If the request contains data, then this data should be ignored and the API should return the resource unchanged.

Next up, check out a `POST` request to add a new car:

HTTP

`POST /cars HTTP/1.1 Host: api.example.com Content-Type: application/json  {     "make": "Nissan",     "model": "240SX",     "year": 1994,     "vin": "1N6AD0CU5AC961553",     "color": "Violet" }`

This `POST` request includes JSON for the new car in the request. It sets the `Content-Type` header to `application/json` so the API knows the content type of the request. The API will create a new car from the JSON.

Here’s the response:

HTTP

`HTTP/1.1 201 Created Content-Type: application/json  {     "id": 4,     "make": "Nissan",     "model": "240SX",     "year": 1994,     "vin": "1N6AD0CU5AC961553",     "color": "Violet" }`

This response has a `201 Created` status code to tell the user that a new resource was created. Make sure to use `201 Created` instead of `200 OK` for all successful `POST` requests.

This response also includes a copy of the new car with an `id` generated by the API. It’s important to send back an `id` in the response so that the user can modify the resource again.

**Note:** It’s important to always send back a copy of a resource when a user creates it with `POST` or modifies it with `PUT` or `PATCH`. This way, the user can see the changes that they’ve made.

Now take a look at a `PUT` request:

HTTP

`PUT /cars/4 HTTP/1.1 Host: api.example.com Content-Type: application/json  {     "make": "Buick",     "model": "Lucerne",     "year": 2006,     "vin": "4T1BF3EK8AU335094",     "color":"Maroon" }`

This request uses the `id` from the previous request to update the car with all new data. As a reminder, `PUT` updates all fields on the resource with new data. Here’s the response:

HTTP

`HTTP/1.1 200 OK Content-Type: application/json  {     "id": 4,     "make": "Buick",    "model": "Lucerne",    "year": 2006,    "vin": "4T1BF3EK8AU335094",    "color":"Maroon" }`

The response includes a copy of the `car` with the new data. Again, you always want to send back the full resource for a `PUT` request. The same applies to a `PATCH` request:

HTTP

`PATCH /cars/4 HTTP/1.1 Host: api.example.com Content-Type: application/json  {     "vin": "VNKKTUD32FA050307",     "color": "Green" }`

`PATCH` requests only update a part of a resource. In the request above, the `vin` and `color` fields will be updated with new values. Here’s the response:

HTTP

`HTTP/1.1 200 OK Content-Type: application/json  {     "id": 4,     "make": "Buick",     "model": "Lucerne",     "year": 2006,     "vin": "VNKKTUD32FA050307",    "color": "Green" }`

The response contains a full copy of the `car`. As you can see, only the `vin` and `color` fields have been updated.

Finally, take a look at how your REST API should respond when it receives a `DELETE` request. Here’s a `DELETE` request to remove a `car`:

HTTP

`DELETE /cars/4 HTTP/1.1`

This `DELETE` request tells the API to remove the `car` with the ID `4`. Here’s the response:

HTTP

`HTTP/1.1 204 No Content`

This response only includes the status code `204 No Content`. This status code tells a user that the operation was successful, but no content was returned in the response. This makes sense since the `car` has been deleted. There’s no reason to send a copy of it back in the response.

The responses above work well when everything goes as planned, but what happens if there’s a problem with the request? In the next section, you’ll look at how your REST API should respond when errors occur.


### Design Error Responses[](#design-error-responses "Permanent link")

There’s always a chance that requests to your REST API could fail. It’s a good idea to define what an error response will look like. These responses should include a description of what error occurred along with the appropriate status code. In this section, you’ll look at a few examples.

To start, take a look at a request for a resource that doesn’t exist in the API:

HTTP

`GET /motorcycles HTTP/1.1 Host: api.example.com`

Here, the user sends a `GET` request to `/motorcycles`, which doesn’t exist. The API sends back the following response:

HTTP

`HTTP/1.1 404 Not Found Content-Type: application/json ...  {     "error": "The requested resource was not found." }`

This response includes a `404 Not Found` status code. Along with this, the response contains a JSON object with a descriptive error message. Providing a descriptive error message gives the user more context for the error.

Now take a look at the error response when the user sends an invalid request:

HTTP

`POST /cars HTTP/1.1 Host: api.example.com Content-Type: application/json  {     "make": "Nissan",     "year": 1994,     "color": "Violet"`

This `POST` request contains JSON, but it isn’t formatted correctly. It’s missing a closing curly brace (`}`) at the end. The API won’t be able to process this data. The error response tells the user about the issue:

HTTP

`HTTP/1.1 400 Bad Request Content-Type: application/json  {     "error": "This request was not properly formatted. Please send again." }`

This response includes a descriptive error message along with the `400 Bad Request` status code, telling the user they need to fix the request.

There are several other ways that the request can be wrong even if it’s formatted properly. In this next example, the user sends a `POST` request but includes an unsupported media type:

HTTP

`POST /cars HTTP/1.1 Host: api.example.com Content-Type: application/xml  <?xml version="1.0" encoding="UTF-8" ?> <car>     <make>Nissan</make>     <model>240SX</model>     <year>1994</year>     <vin>1N6AD0CU5AC961553</vin>     <color>Violet</color> </car>`

In this request, the user sends XML, but the API only supports JSON. The API responds with this:

HTTP

`HTTP/1.1 415 Unsupported Media Type Content-Type: application/json  {     "error": "The application/xml mediatype is not supported." }`

This response includes the `415 Unsupported Media Type` status code to indicate that the `POST` request included a data format that isn’t supported by the API. This error code makes sense for data that’s in the wrong format, but what about data that’s invalid even with the correct format?

In this next example, the user sends a `POST` request but includes `car` data that doesn’t match fields of the other data:

HTTP

`POST /cars HTTP/1.1 Host: api.example.com Content-Type: application/json  {     "make": "Nissan",     "model": "240SX",     "topSpeed": 120    "warrantyLength": 10 }`

In this request, the user adds `topSpeed` and `warrantyLength` fields to the JSON. These fields aren’t supported by the API, so it responds with an error message:

HTTP

`HTTP/1.1 422 Unprocessable Entity Content-Type: application/json  {     "error": "Request had invalid or missing data." }`

This response includes the `422 Unprocessable Entity` status code. This status code indicates that there weren’t any issues with the request, but the data was invalid. A REST API needs to validate incoming data. If the user sends data with the request, then the API should validate the data and inform the user of any errors.

Responding to requests, both successful and erroneous, is one of the most important jobs of a REST API. If your API is intuitive and provides accurate responses, then it’ll be easier for users to build applications around your web service. Luckily, some great Python web frameworks abstract away the complexities of processing HTTP requests and returning responses. You’ll look at three popular options in the next section.



## REST and Python: Tools of the Trade[](#rest-and-python-tools-of-the-trade "Permanent link")

In this section, you’ll look at 2 popular frameworks for building REST APIs in Python. 
Each framework has pros and cons, so you’ll have to evaluate which works best for your needs. 

To this end, in the next sections, you’ll look at a REST API in each framework. 
All the examples will be for a similar API that manages a collection of countries.

Each country will have the following fields:

*   **`name`** is the name of the country.
*   **`capital`** is the capital of the country.
*   **`area`** is the area of the country in square kilometers.

The fields `name`, `capital`, and `area` store data about a specific country somewhere in the world.

Most of the time, data sent from a REST API comes from a database. [Connecting to a database](https://realpython.com/flask-connexion-rest-api-part-2/) is beyond the scope for now. we will store our stuff into a csv if needed
For the examples below, you’ll store your data in a Python list. and later change it to a csv file. in the future we will use sqlite

**Note:** It’s advised that you create individual folders for each of the examples to separate the source files.

To keep things consistent, you’ll use `countries` as your main endpoint for all three frameworks. You’ll also use JSON as your data format for all three frameworks.

Now that you’ve got the background for the API, you can move on to the next section, where you’ll look at the REST API in **Flask**.

### Flask[](#flask "Permanent link")

[Flask](https://realpython.com/introduction-to-flask-part-1-setting-up-a-static-site/) is a Python microframework used to build web applications and REST APIs. 
I find Flask the easiest framework to use given youre experience level.


Flask provides a solid backbone for your applications while leaving many design choices up to you. Flask’s main job is to handle HTTP requests and route them to the appropriate function in the application.

**Note:** The code in this section uses the new [Flask 2](https://palletsprojects.com/blog/flask-2-0-released/) syntax. If you’re running an older version of Flask, then use [`@app.route("/countries")`](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Flask.route) instead of [`@app.get("/countries")`](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Flask.get) and [`@app.post("/countries")`](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Flask.post).

To handle `POST` requests in older versions of [Flask](https://flask.palletsprojects.com/en/1.1.x/), you’ll also need to add the `methods` parameter to `@app.route()`:

Python

`@app.route("/countries", methods=["POST"])`

This route handles `POST` requests to `/countries` in Flask 1.

Below is an example Flask application for the REST API:

Python

```python
# app.py
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1 if countries else 1

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.post("/countries")
def add_country():
    if not request.is_json:
        return make_response(jsonify({"error": "Request must be JSON"}), 415)

    data = request.get_json()

    required_fields = {"name", "capital", "area"}
    if not required_fields.issubset(data):
        return make_response(jsonify({"error": f"Missing fields: {required_fields - data.keys()}"}), 400)

    country = {
        "id": _find_next_id(),
        "name": data["name"],
        "capital": data["capital"],
        "area": data["area"]
    }
    countries.append(country)
    return make_response(jsonify(country), 201)

if __name__ == "__main__":
    app.run(debug=True)


# you can get the respone by using curl in the cli:
# curl -X GET http://127.0.0.1:5000/countries
# 
# or if it runs on localhost:

# curl -X GET http://localhost:5000/countries
```
This application defines the API endpoint `/countries` to manage the list of countries. It handles two different kinds of requests:

1.  **`GET /countries`** returns the list of `countries`.
2.  **`POST /countries`** adds a new `country` to the list.

**Note:** This Flask application includes functions to handle only two types of requests to the API endpoint, `/countries`. In a full REST API, you’d want to expand this to include functions for all the required operations.

You can try out this application by installing `flask` with `pip`:

Shell

`$ python -m pip install flask`

Once `flask` is installed, save the code in a file called `app.py`. Then run it from vscode or pycharm

you will get output like this
Shell

```bash
$ flask run * Serving Flask app "app.py" (lazy loading) 
* Environment: development 
* Debug mode: on 
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
```
This starts up a server running the application. Open up your browser and go to `http://127.0.0.1:5000/countries` or `http://localhost:5000/countries`, 
and you’ll see the following response:

JSON

`[     {         "area": 513120,         "capital": "Bangkok",         "id": 1,         "name": "Thailand"     },     {         "area": 7617930,         "capital": "Canberra",         "id": 2,         "name": "Australia"     },     {         "area": 1010408,         "capital": "Cairo",         "id": 3,         "name": "Egypt"     } ]`

This JSON response contains the three `countries` defined at the start of `app.py`. Take a look at the following code to see how this works:

Python

```python
@app.get("/countries") 
def get_countries():     
    return jsonify(countries)
```

This code uses `@app.get()`, a Flask route [decorator](https://realpython.com/primer-on-python-decorators/), to connect `GET` requests to a function in the application. When you access `/countries`, Flask calls the decorated function to handle the HTTP request and [return](https://realpython.com/python-return-statement/) a response.

In the code above, `get_countries()` takes `countries`, which is a [Python list](https://realpython.com/python-lists-tuples/), and converts it to JSON with `jsonify()`. This JSON is returned in the response.

**Note:** Most of the time, you can just return a Python dictionary from a Flask function. Flask will automatically convert any Python dictionary to JSON. You can see this in action with the function below:

Python

```python
@app.get("/country") 
def get_country():     
    return countries[1]
```

In this code, you return the second dictionary from `countries`. Flask will convert this dictionary to JSON. Here’s what you’ll see when you request `/country`:

JSON

`{     "area": 7617930,     "capital": "Canberra",     "id": 2,     "name": "Australia" }`

This is the JSON version of the dictionary you returned from `get_country()`.

In `get_countries()`, you need to use `jsonify()` because you’re returning a list of dictionaries and not just a single dictionary. Flask doesn’t automatically convert lists to JSON.

Now take a look at `add_country()`. This function handles `POST` requests to `/countries` and allows you to add a new country to the list. It uses the Flask [`request`](https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object) object to get information about the current HTTP request:

Python

```python
@app.post("/countries") 
def add_country():     
    if request.is_json:         
        country = request.get_json()         
        country["id"] = _find_next_id()         
        countries.append(country)         
        return country, 201     
    return {"error": "Request must be JSON"}, 415

```
This function performs the following operations:

1.  Using [`request.is_json`](https://flask.palletsprojects.com/en/1.1.x/api/?highlight=is_json#flask.Request.is_json) to check that the request is JSON
2.  Creating a new `country` instance with `request.get_json()`
3.  Finding the next `id` and setting it on the `country`
4.  Appending the new `country` to `countries`
5.  Returning the `country` in the response along with a `201 Created` status code
6.  Returning an error message and `415 Unsupported Media Type` status code if the request wasn’t JSON

`add_country()` also calls `_find_next_id()` to determine the `id` for the new `country`:

Python

```python
def _find_next_id():     
return max(country["id"] for country in countries) + 1   
```

This helper function uses a [generator expression](https://realpython.com/introduction-to-python-generators/) to select all the country IDs and then calls [`max()`](https://realpython.com/python-min-and-max/) on them to get the largest value. It increments this value by `1` to get the next ID to use.

You can try out this endpoint in the shell using the command-line tool [curl](https://curl.se/), which allows you to send HTTP requests from the command line. Here, you’ll add a new `country` to the list of `countries`:

Shell

`$ curl -i http://127.0.0.1:5000/countries \ -X POST \ -H 'Content-Type: application/json' \ -d '{"name":"Germany", "capital": "Berlin", "area": 357022}'  HTTP/1.0 201 CREATED Content-Type: application/json ...  {     "area": 357022,     "capital": "Berlin",     "id": 4,     "name": "Germany" }`

This curl command has some options that are helpful to know:

*   **`-X`** sets the HTTP method for the request.
*   **`-H`** adds an HTTP header to the request.
*   **`-d`** defines the request data.

With these options set, curl sends JSON data in a `POST` request with the `Content-Type` header set to `application/json`. The REST API returns `201 CREATED` along with the JSON for the new `country` you added.

**Note:** In this example, `add_country()` doesn’t contain any validation to confirm that the JSON in the request matches the format of `countries`. Check out [flask-expects-json](https://pypi.org/project/flask-expects-json/) if you’d like to validate the format of JSON in Flask.

You can use curl to send a `GET` request to `/countries` to confirm that the new `country` was added. If you don’t use `-X` in your curl command, then it sends a `GET` request by default:

Shell

`$ curl -i http://127.0.0.1:5000/countries  HTTP/1.0 200 OK Content-Type: application/json ...  [     {         "area": 513120,         "capital": "Bangkok",         "id": 1,         "name": "Thailand"     },     {         "area": 7617930,         "capital": "Canberra",         "id": 2,         "name": "Australia"     },     {         "area": 1010408,         "capital": "Cairo",         "id": 3,         "name": "Egypt"     },     {         "area": 357022,         "capital": "Berlin",         "id": 4,         "name": "Germany"     } ]`

This returns the full list of countries in the system, with the newest country at the bottom.

This is just a sampling of what Flask can do. This application could be expanded to include endpoints for all the other HTTP methods. Flask also has a large ecosystem of extensions that provide additional functionality for REST APIs, such as [database integrations](https://realpython.com/flask-connexion-rest-api/), [authentication](https://realpython.com/flask-google-login/), and background processing.



### Litestar Framework[](#litestar-framework "Permanent link")

Another popular option for building REST APIs (and the ones i use professionaly) is [Litestar Framework](https://litestar.dev/).

Litestar is a modern, fast, and flexible web framework for building APIs in Python. It’s designed to be easy to use while providing powerful features for building RESTful services.
Litestar is built on top of [Starlette](https://www.starlette.io/) and [Pydantic](https://docs.pydantic.dev/latest/), which makes it fast and efficient. It also has a simple and intuitive API that makes it easy to get started.
I mostly use it because it is native Async and it is very fast, however. for where we are now in the course, it may be a bit too advanced.

below is mostly for demonstration purposes as we will continue with flask for the rest of the course. (until we go into async and more advanced topics)

```python
from litestar import Litestar, get, post, Request, Response
from pydantic import BaseModel
from typing import List
import uvicorn

class Country(BaseModel):
    name: str
    capital: str
    area: int

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1 if countries else 1

@get("/countries")
async def get_countries() -> List[dict]:
    return countries

@post("/countries")
async def add_country(request: Request) -> Response:
    data = await request.json()
    required_fields = {"name", "capital", "area"}
    if not required_fields.issubset(data):
        return Response(
            {"error": f"Missing fields: {required_fields - data.keys()}"},
            status_code=400
        )

    country = {
        "id": _find_next_id(),
        "name": data["name"],
        "capital": data["capital"],
        "area": data["area"]
    }
    countries.append(country)

    return Response(country, status_code=201)

app = Litestar(route_handlers=[get_countries, add_country])

# --- 👇 Run the server from this file in vs code or pycharm ---
if __name__ == "__main__":
    uvicorn.run("prog:app", host="127.0.0.1", port=5000, reload=True)

```

we will need to install the following packages to run this code:

```bash
pip install litestar uvicorn pydantic
```

Sure! Here is the explanation formatted as a complete Markdown file:

---

````markdown
# 🇹🇭 Simple Country API with Litestar and Uvicorn

This project defines a basic REST API to manage country data using **[Litestar](https://www.litestar.dev)**. The server is started using **Uvicorn** directly from the same Python file.

---

## 📁 File: `prog.py`

### 🔧 Imports

```python
from litestar import Litestar, get, post, Request, Response
from pydantic import BaseModel
from typing import List
import uvicorn
````

* `Litestar`, `get`, `post`, `Request`, `Response`: Core components from the Litestar web framework.
* `BaseModel`: From Pydantic, used to define data models with validation.
* `List`: For type hinting a list of dictionaries.
* `uvicorn`: The ASGI server to run the app.

---

### 📦 Data Model

```python
class Country(BaseModel):
    name: str
    capital: str
    area: int
```

Defines the schema for a country with three fields: `name`, `capital`, and `area`.

---

### 🌍 In-Memory Data Store

```python
countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]
```

A simple list of dictionaries representing country records.

---

### 🔢 ID Generation Helper

```python
def _find_next_id():
    return max(country["id"] for country in countries) + 1 if countries else 1
```

Returns the next available unique ID for a new country entry.

---

### 📥 `GET /countries` Endpoint

```python
@get("/countries", sync_to_thread=False)
def get_countries() -> List[dict]:
    return countries
```

* Returns a list of all country entries.
* `sync_to_thread=False` is used to indicate that this synchronous function is safe and non-blocking.

---

### ➕ `POST /countries` Endpoint

```python
@post("/countries")
async def add_country(request: Request) -> Response:
    data = await request.json()
    required_fields = {"name", "capital", "area"}
    if not required_fields.issubset(data):
        return Response(
            {"error": f"Missing fields: {required_fields - data.keys()}"},
            status_code=400
        )

    country = {
        "id": _find_next_id(),
        "name": data["name"],
        "capital": data["capital"],
        "area": data["area"]
    }
    countries.append(country)

    return Response(country, status_code=201)
```

* Accepts a JSON body with required fields.
* Validates field presence.
* Adds the new country to the list and returns it with HTTP 201 Created.

---

### 🚀 Create and Run the Litestar App

```python
app = Litestar(route_handlers=[get_countries, add_country])
```

Creates the Litestar app with the registered route handlers.

```python
if __name__ == "__main__":
    uvicorn.run("prog:app", host="127.0.0.1", port=8000, reload=True)
```

* Launches the server on `http://127.0.0.1:8000`.
* `reload=True` enables hot-reloading for development.

---

## 🧪 Example Usage

### 🔍 Get All Countries

```bash
curl -X GET http://127.0.0.1:8000/countries
```

### ➕ Add a Country

```bash
curl -X POST http://127.0.0.1:8000/countries \
     -H "Content-Type: application/json" \
     -d '{"name": "Japan", "capital": "Tokyo", "area": 377975}'
```

---




