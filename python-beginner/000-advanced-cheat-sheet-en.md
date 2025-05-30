# Python Advanced Topics

## Table of Contents
- [Functional Programming in Python](#functional-programming-in-python)
- [Design Patterns in Python](#design-patterns-in-python)
- [Concurrency Models](#concurrency-models)
- [Web Development Essentials](#web-development-essentials)
- [Data Science Ecosystem](#data-science-ecosystem)
- [Database Interaction](#database-interaction)
- [Decorators Deep Dive](#decorators-deep-dive)
- [Memory Management](#memory-management)
- [Python C Extensions](#python-c-extensions)
- [Network Programming](#network-programming)
- [GUI Development](#gui-development)
- [Security Best Practices](#security-best-practices)
- [Python Internals](#python-internals)
- [Project Structure and Organization](#project-structure-and-organization)
- [Documentation Best Practices](#documentation-best-practices)

## Functional Programming in Python

### First-Class and Higher-Order Functions
```python
# Functions as first-class objects
def greet(name):
    return f"Hello, {name}!"

# Assign function to variable
greeting_function = greet
result = greeting_function("Alice")  # "Hello, Alice!"

# Function as argument (higher-order function)
def apply_function(func, value):
    return func(value)

result = apply_function(len, "hello")  # 5

# Function returning function
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))  # 10
print(triple(5))  # 15
```

### Map, Filter, and Reduce
```python
# map: apply function to each item in iterable
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]

# Using list comprehension (often more readable)
squared = [x**2 for x in numbers]

# filter: keep items that pass a test
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# Using list comprehension
even_numbers = [x for x in numbers if x % 2 == 0]

# reduce: apply function cumulatively to items
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)  # 1*2*3*4*5 = 120
sum_all = reduce(lambda x, y: x + y, numbers)  # 1+2+3+4+5 = 15
```

### Partial Functions
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

# Create new functions with partially applied arguments
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(4))  # 16
print(cube(4))    # 64

# Practical example: preconfigured function
import json
load_json_as_dict = partial(json.loads, object_hook=dict)
```

### Function Composition
```python
# Manual composition
def compose(f, g):
    return lambda x: f(g(x))

# Example
def add_one(x): return x + 1
def multiply_by_two(x): return x * 2

add_then_multiply = compose(multiply_by_two, add_one)
multiply_then_add = compose(add_one, multiply_by_two)

print(add_then_multiply(3))  # (3+1)*2 = 8
print(multiply_then_add(3))  # (3*2)+1 = 7

# Multiple function composition
def compose(*functions):
    def compose_two(f, g):
        return lambda x: f(g(x))
    return reduce(compose_two, functions, lambda x: x)

# Example
def square(x): return x * x
pipeline = compose(square, multiply_by_two, add_one)
print(pipeline(3))  # square(multiply_by_two(add_one(3))) = square(multiply_by_two(4)) = square(8) = 64
```

### Immutability and Frozen Data Structures
```python
# Immutable built-in types: int, float, str, tuple, frozenset

# Creating immutable versions of mutable structures
from types import MappingProxyType
original_dict = {'a': 1, 'b': 2}
read_only_dict = MappingProxyType(original_dict)
# read_only_dict['c'] = 3  # TypeError: 'mappingproxy' object does not support item assignment

# However, the original dict can still be modified
original_dict['c'] = 3
print(read_only_dict)  # Shows {'a': 1, 'b': 2, 'c': 3}

# Frozen set - immutable version of set
frozen = frozenset([1, 2, 3])
# frozen.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'

# For custom objects, use @property with no setter
class ImmutablePoint:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
    @property
    def x(self):
        return self._x
        
    @property
    def y(self):
        return self._y
```

## Design Patterns in Python

### Singleton
```python
# Method 1: Using a decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Logger:
    def __init__(self):
        self.logs = []
    
    def log(self, message):
        self.logs.append(message)

# Method 2: Using a metaclass
class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self):
        self.connection = "Connected"
```

### Factory
```python
# Simple Factory
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Usage
animal = AnimalFactory.create_animal("dog")
print(animal.speak())  # "Woof!"
```

### Observer
```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def register_observer(self, observer):
        self._observers.append(observer)
    
    def unregister_observer(self, observer):
        self._observers.remove(observer)
    
    def notify_observers(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(*args, **kwargs)

class Observer:
    def update(self, *args, **kwargs):
        pass

# Example implementation
class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0
    
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.notify_observers(value)

class TemperatureDisplay(Observer):
    def update(self, temperature):
        print(f"Temperature changed to {temperature}°C")

# Usage
station = WeatherStation()
display = TemperatureDisplay()
station.register_observer(display)
station.temperature = 25  # Triggers notification
```

### Strategy
```python
from abc import ABC, abstractmethod

# Strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, expiry, cvv):
        self.card_number = card_number
        self.expiry = expiry
        self.cvv = cvv
    
    def pay(self, amount):
        print(f"Paying ${amount} with credit card {self.card_number}")
        return True

class PayPalPayment(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def pay(self, amount):
        print(f"Paying ${amount} with PayPal account {self.email}")
        return True

# Context
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None
    
    def add_item(self, item, price):
        self.items.append((item, price))
    
    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy
    
    def calculate_total(self):
        return sum(price for _, price in self.items)
    
    def checkout(self):
        if not self.payment_strategy:
            raise Exception("Payment strategy not set")
        
        total = self.calculate_total()
        return self.payment_strategy.pay(total)

# Usage
cart = ShoppingCart()
cart.add_item("Book", 20)
cart.add_item("Laptop", 1000)

# Use credit card
cart.set_payment_strategy(CreditCardPayment("1234-5678-9012-3456", "12/25", "123"))
cart.checkout()

# Use PayPal
cart.set_payment_strategy(PayPalPayment("user@example.com", "password"))
cart.checkout()
```

## Concurrency Models

### Threading
```python
import threading
import time

def task(name, delay):
    print(f"Task {name} started")
    time.sleep(delay)  # Simulate work
    print(f"Task {name} completed")

# Create and start threads
threads = []
for i in range(3):
    t = threading.Thread(target=task, args=(i, 1))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All tasks completed")

# Using a thread pool
from concurrent.futures import ThreadPoolExecutor

def worker(num):
    print(f"Worker {num} starting")
    time.sleep(1)
    return f"Worker {num} result"

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(worker, i) for i in range(5)]
    
    for future in futures:
        print(future.result())
```

### Multiprocessing
```python
import multiprocessing as mp
import time

def cpu_bound_task(number):
    """A CPU-bound task (good for multiprocessing)"""
    return sum(i * i for i in range(number))

# Create and start processes
if __name__ == "__main__":  # Required for Windows
    numbers = [10**7, 10**7, 10**7]
    
    # Sequential
    start = time.time()
    results = [cpu_bound_task(n) for n in numbers]
    print(f"Sequential: {time.time() - start:.2f} seconds")
    
    # Parallel
    start = time.time()
    with mp.Pool(processes=3) as pool:
        results = pool.map(cpu_bound_task, numbers)
    print(f"Parallel: {time.time() - start:.2f} seconds")

# Process Pool Executor
from concurrent.futures import ProcessPoolExecutor

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(cpu_bound_task, numbers))
```

### Asynchronous Programming with asyncio
```python
import asyncio
import time

async def async_task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)  # Non-blocking sleep
    print(f"Task {name} completed")
    return f"Result from task {name}"

async def main():
    # Run tasks sequentially
    start = time.time()
    for i in range(3):
        await async_task(i, 1)
    print(f"Sequential: {time.time() - start:.2f} seconds")
    
    # Run tasks concurrently
    start = time.time()
    tasks = [async_task(i, 1) for i in range(3)]
    results = await asyncio.gather(*tasks)
    print(f"Concurrent: {time.time() - start:.2f} seconds")
    print(f"Results: {results}")
    
    # Wait for first task to complete
    start = time.time()
    done, pending = await asyncio.wait(
        [async_task(i, i) for i in range(1, 4)],
        return_when=asyncio.FIRST_COMPLETED
    )
    print(f"First task completed in {time.time() - start:.2f} seconds")
    
    # Cancel pending tasks
    for task in pending:
        task.cancel()

# Run the event loop
asyncio.run(main())
```

### Thread Safety and Synchronization
```python
import threading
import time

# Using locks
counter = 0
counter_lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100000):
        with counter_lock:  # Acquire and release lock
            counter += 1

threads = [threading.Thread(target=increment_counter) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Counter: {counter}")  # Should be 500000

# Using RLock (reentrant lock)
rlock = threading.RLock()

def recursive_function(depth):
    with rlock:  # Can acquire the same lock multiple times
        if depth > 0:
            recursive_function(depth - 1)

# Using Semaphore to limit concurrent access
semaphore = threading.Semaphore(3)  # Max 3 threads at once

def limited_concurrency_task(num):
    with semaphore:
        print(f"Task {num} started")
        time.sleep(1)
        print(f"Task {num} completed")

# Start more threads than the semaphore allows
threads = [threading.Thread(target=limited_concurrency_task, args=(i,)) for i in range(10)]
for t in threads:
    t.start()
```

## Web Development Essentials

### Making HTTP Requests
```python
import requests

# Basic GET request
response = requests.get("https://api.example.com/data")
data = response.json()
print(f"Status code: {response.status_code}")
print(f"Content: {data}")

# POST request with JSON data
response = requests.post(
    "https://api.example.com/create",
    json={"name": "John", "age": 30}
)

# Request with parameters
params = {"q": "python", "page": 1}
response = requests.get("https://api.example.com/search", params=params)

# Request with headers
headers = {"Authorization": "Bearer token123"}
response = requests.get("https://api.example.com/protected", headers=headers)

# File upload
files = {"file": open("document.pdf", "rb")}
response = requests.post("https://api.example.com/upload", files=files)

# Session for multiple requests (preserves cookies)
session = requests.Session()
session.get("https://api.example.com/login")
response = session.get("https://api.example.com/dashboard")  # Has cookies from login

# Timeouts
try:
    response = requests.get("https://api.example.com/slow", timeout=5)
except requests.Timeout:
    print("Request timed out")
```

### Flask Web Application
```python
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simple route
@app.route('/')
def home():
    return "Hello, World!"

# Route with variable
@app.route('/user/<username>')
def show_user(username):
    return f"User: {username}"

# Route with type specification
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post ID: {post_id}"

# Route with multiple methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Process login
        return f"Logged in as {username}"
    else:
        return render_template('login.html')

# JSON API endpoint
@app.route('/api/data')
def get_data():
    data = {"name": "John", "age": 30}
    return jsonify(data)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### FastAPI Web Application
```python
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(..., title="The ID of the item"),
    q: Optional[str] = Query(None, max_length=50)
):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id < 1:
        raise HTTPException(status_code=400, detail="Item ID must be positive")
    return {"item_id": item_id, **item.dict()}

# Run with: uvicorn main:app --reload
```

## Data Science Ecosystem

### NumPy Basics
```python
import numpy as np

# Creating arrays
a = np.array([1, 2, 3, 4, 5])
b = np.zeros((3, 3))
c = np.ones((2, 2))
d = np.eye(3)  # 3x3 identity matrix
e = np.arange(10)  # 0-9
f = np.linspace(0, 1, 5)  # 5 equally spaced points between 0 and 1

# Array operations
print(a + 2)  # Element-wise addition
print(a * 2)  # Element-wise multiplication
print(a @ a)  # Matrix multiplication (Python 3.5+)
print(np.dot(a, a))  # Dot product

# Slicing
print(a[1:3])  # Elements at index 1 and 2
print(a[a > 2])  # Boolean indexing

# Reshaping
g = np.arange(12).reshape(3, 4)  # 3x4 matrix
h = g.T  # Transpose

# Statistical functions
print(np.mean(a))
print(np.median(a))
print(np.std(a))
print(np.min(a))
print(np.max(a))
```

### Pandas Basics
```python
import pandas as pd
import numpy as np

# Creating DataFrames
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': ['a', 'b', 'c', 'd', 'e']
})

# Reading data
# df = pd.read_csv('data.csv')
# df = pd.read_excel('data.xlsx')
# df = pd.read_json('data.json')

# Basic operations
print(df.head())  # First 5 rows
print(df.describe())  # Statistical summary
print(df.info())  # DataFrame info

# Indexing and selection
print(df['A'])  # Select column
print(df[['A', 'B']])  # Select multiple columns
print(df.loc[1])  # Select row by label
print(df.iloc[1])  # Select row by position
print(df.loc[1:3, 'A':'B'])  # Select rows and columns by label
print(df.iloc[1:3, 0:2])  # Select rows and columns by position

# Filtering
print(df[df['A'] > 2])  # Rows where A > 2
print(df[(df['A'] > 2) & (df['B'] < 40)])  # Combining conditions

# Missing data
df2 = df.copy()
df2.loc[1, 'A'] = np.nan
print(df2.isna())  # Check for NaN
print(df2.dropna())  # Drop rows with NaN
print(df2.fillna(0))  # Fill NaN with 0

# Grouping and aggregation
df3 = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B', 'C'],
    'Value': [10, 20, 30, 40, 50]
})
print(df3.groupby('Category').sum())
print(df3.groupby('Category').agg(['sum', 'mean', 'count']))

# Pivoting
df4 = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'Product': ['A', 'B', 'A', 'B'],
    'Sales': [100, 200, 150, 250]
})
pivot = df4.pivot_table(index='Date', columns='Product', values='Sales')
print(pivot)
```

### Matplotlib Basics
```python
import matplotlib.pyplot as plt
import numpy as np

# Basic line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)')
plt.title('Sin Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()

# Multiple plots
plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.title('Sin and Cos Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(x, np.sin(x))
ax1.set_title('Sin Wave')
ax2.plot(x, np.cos(x))
ax2.set_title('Cos Wave')
plt.tight_layout()
plt.show()

# Bar plot
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]
plt.figure(figsize=(8, 5))
plt.bar(categories, values)
plt.title('Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

# Scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.7)
plt.title('Scatter Plot')
plt.colorbar()
plt.show()
```

## Database Interaction

### SQLite with sqlite3
```python
import sqlite3

# Connect to database (creates file if doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER
)
''')

# Insert data
cursor.execute('''
INSERT INTO users (name, email, age)
VALUES (?, ?, ?)
''', ('Alice', 'alice@example.com', 30))

# Insert multiple rows
users = [
    ('Bob', 'bob@example.com', 25),
    ('Charlie', 'charlie@example.com', 35)
]
cursor.executemany('INSERT INTO users (name, email, age) VALUES (?, ?, ?)', users)

# Commit changes
conn.commit()

# Query data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Using named placeholders
cursor.execute('''
SELECT * FROM users WHERE age > :min_age
''', {'min_age': 25})
rows = cursor.fetchall()

# Using row factory for named columns
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute('SELECT * FROM users')
for row in cursor.fetchall():
    print(f"Name: {row['name']}, Email: {row['email']}")

# Close connection
conn.close()
```

### SQLAlchemy ORM
```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create engine and base
engine = create_engine('sqlite:///orm_example.db')
Base = declarative_base()

# Define models
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    age = Column(Integer)
    
    posts = relationship('Post', back_populates='author')
    
    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    author = relationship('User', back_populates='posts')
    
    def __repr__(self):
        return f"<Post(title='{self.title}')>"

# Create tables
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Add data
alice = User(name='Alice', email='alice@example.com', age=30)
session.add(alice)
session.add_all([
    User(name='Bob', email='bob@example.com', age=25),
    User(name='Charlie', email='charlie@example.com', age=35)
])
session.commit()

# Add related data
alice = session.query(User).filter_by(name='Alice').first()
post = Post(title='First Post', content='Hello, world!', author=alice)
session.add(post)
session.commit()

# Query data
users = session.query(User).all()
for user in users:
    print(user)

# Filter queries
young_users = session.query(User).filter(User.age < 30).all()
for user in young_users:
    print(f"{user.name} is {user.age} years old")

# Join queries
for user, post in session.query(User, Post).filter(User.id == Post.user_id).all():
    print(f"{user.name} wrote: {post.title}")

# Update data
alice = session.query(User).filter_by(name='Alice').first()
alice.age = 31
session.commit()

# Delete data
post = session.query(Post).first()
session.delete(post)
session.commit()

# Close session
session.close()
```

## Decorators Deep Dive

### Creating Decorators
```python
# Basic decorator
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@simple_decorator
def say_hello(name):
    print(f"Hello, {name}!")
    return f"Hello, {name}!"

# Decorator with arguments
def repeat(n=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(n=3)
def say_hi(name):
    print(f"Hi, {name}!")
    return f"Hi, {name}!"

# Preserving function metadata
from functools import wraps

def preserved_metadata(func):
    @wraps(func)  # Preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@preserved_metadata
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

print(add.__name__)  # 'add' (not 'wrapper')
print(add.__doc__)   # Original docstring preserved
```

### Class Decorators
```python
# Decorating a class
def add_greeting(cls):
    cls.greeting = "Hello!"
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Creating a decorator class
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call count: {self.count}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

# Class decorator with arguments
class Repeat:
    def __init__(self, n=1):
        self.n = n
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.n):
                result = func(*args, **kwargs)
            return result
        return wrapper

@Repeat(n=3)
def say_hi():
    print("Hi!")
```

### Practical Decorator Examples
```python
import time
import functools
import logging

# Timing decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds to run")
        return result
    return wrapper

# Cache/memoize results
def memoize(func):
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key that can be used as a dictionary key
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

# Retry decorator
def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    print(f"Attempt {attempts} failed with error: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
        return wrapper
    return decorator

# Logging decorator
def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__} returned {result}")
            return result
        except Exception as e:
            logging.error(f"{func.__name__} raised {e}")
            raise
    return wrapper

# Authentication decorator
def require_auth(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.is_authenticated:
            raise PermissionError("Authentication required")
        return func(user, *args, **kwargs)
    return wrapper
```