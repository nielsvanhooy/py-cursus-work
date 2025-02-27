## Introduction to Python Dictionaries

Python dictionaries are one of the most important and useful data structures in the language. 
They allow you to store and retrieve data using key-value pairs instead of indices. 
This makes dictionaries incredibly versatile for a wide range of programming tasks, 
especially when it comes to data processing and analysis.

## What is a Python Dictionary?

A Python dictionary is an unordered collection of items where each item is stored as a key-value pair. 
Dictionaries are optimized for retrieving data when you know the key. 
Unlike sequences such as lists or tuples which are indexed by a range of numbers, 
dictionaries are indexed by keys, which can be any immutable type like strings, numbers, or tuples.

### Key Features of Dictionaries

* **Key-Value Pairs**: Each item in a dictionary consists of a key and its corresponding value
* **Mutable**: Dictionaries can be modified after creation
* **Dynamic**: They can grow and shrink as needed
* **Versatile**: Values can be of any data type (including other dictionaries)
* **Fast Access**: Retrieving values by key is very efficient

## Creating Python Dictionaries

There are several ways to create a dictionary in Python:

## Syntax

```python
{
    `key`: `value`,
}
```

- the key has to be an immutable type:  string, number, or tuple
- values can be any data type: string, number, list, dictionary, etc.

### Using Curly Braces

The most common method is to enclose comma-separated key-value pairs in curly braces:

```python
# Empty dictionary
empty_dict = {}

# Dictionary with items
student = {
    'name': 'John Doe',
    'age': 21,
    'courses': ['Math', 'Physics', 'Programming']
}
```

### Using the dict() Constructor

You can also create dictionaries using the built-in `dict()` function:

```python
# Empty dictionary
empty_dict = dict()

# Dictionary from keyword arguments
person = dict(name='Alice', age=25, city='New York')

# Dictionary from a list of tuples
items = dict([('apple', 4.5), ('banana', 3.2), ('orange', 2.0)])
```

---

## Accessing Dictionary Elements

There are multiple ways to access elements in a dictionary:

### Using Keys

The most straightforward way is to use the key inside square brackets:

```python
student = {'name': 'John', 'age': 21, 'courses': ['Math', 'Physics']}

# Access value by key
print(student['name'])  # Output: John
print(student['courses'])  # Output: ['Math', 'Physics']
```

### Using the get() Method

The get method is preferred. because you can give a default back if not found.
The `get()` method is safer as it doesn't raise a KeyError if the key doesn't exist:

```python
# Access with get()
print(student.get('name'))  # Output: John
print(student.get('grade'))  # Output: None (key doesn't exist)
print(student.get('grade', 'N/A'))  # Output: N/A (custom default value)
```

## Modifying Dictionaries

Dictionaries are mutable, meaning you can change their content without changing their identity.

### Adding or Updating Items

You can add new key-value pairs or update existing ones:

```python
student = {'name': 'John', 'age': 21}

# Add a new key-value pair
student['courses'] = ['Math', 'Physics']

# Update an existing key
student['age'] = 22

print(student)
# Output: {'name': 'John', 'age': 22, 'courses': ['Math', 'Physics']}
```

### Using the update() Method

The `update()` method lets you add multiple key-value pairs at once:

```python
student = {'name': 'John', 'age': 21}

# Add/update multiple items at once
student.update({'age': 22, 'city': 'New York', 'grade': 'A'})

print(student)
# Output: {'name': 'John', 'age': 22, 'city': 'New York', 'grade': 'A'}
```

## Removing Items

There are several ways to remove items from a dictionary:

### Using the pop() Method

The `pop()` method removes an item with the specified key and returns the value:

```python
student = {'name': 'John', 'age': 21, 'city': 'New York'}

# Remove and return a value
age = student.pop('age')
print(age)  # Output: 21
print(student)  # Output: {'name': 'John', 'city': 'New York'}
```

### Using the popitem() Method

The `popitem()` method removes and returns the last inserted key-value pair as a tuple:

```python
student = {'name': 'John', 'age': 21, 'city': 'New York'}

# Remove the last inserted item
last_item = student.popitem()
print(last_item)  # Output: ('city', 'New York')
print(student)  # Output: {'name': 'John', 'age': 21}
```

### Using the del Keyword

The `del` keyword removes an item with a specific key:

```python
student = {'name': 'John', 'age': 21, 'city': 'New York'}

# Delete a specific key
del student['city']
print(student)  # Output: {'name': 'John', 'age': 21}

# Delete the entire dictionary
del student
# print(student)  # This would raise an error as student no longer exists
```

### Using the clear() Method

The `clear()` method removes all items from the dictionary:

```python
student = {'name': 'John', 'age': 21}

# Remove all items
student.clear()
print(student)  # Output: {}
```

---

## Dictionary Methods

Python dictionaries come with many useful built-in methods:

### keys(), values(), and items()

These methods return view objects that provide views on the dictionary's keys, values, and key-value pairs:

```python
student = {'name': 'John', 'age': 21, 'city': 'New York'}

# Get all keys
keys = student.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'city'])

# Get all values
values = student.values()
print(values)  # Output: dict_values(['John', 21, 'New York'])

# Get all key-value pairs
items = student.items()
print(items)  # Output: dict_items([('name', 'John'), ('age', 21), ('city', 'New York')])
```

### copy()

The `copy()` method returns a shallow copy of the dictionary:

```python
original = {'name': 'John', 'age': 21, 'courses': ['Math', 'Physics']}

# Create a copy
copied = original.copy()

# Modify the original
original['name'] = 'Jane'
original['courses'].append('Chemistry')

print(original)  # Output: {'name': 'Jane', 'age': 21, 'courses': ['Math', 'Physics', 'Chemistry']}
print(copied)    # Output: {'name': 'John', 'age': 21, 'courses': ['Math', 'Physics', 'Chemistry']}
```

Note that with shallow copies, nested mutable objects like lists are still references to the same objects.

### setdefault()

The `setdefault()` method returns the value of the specified key. If the key doesn't exist, it inserts the key with the specified value:

```python
student = {'name': 'John', 'age': 21}

# Get value if key exists, otherwise set default
email = student.setdefault('email', 'john@example.com')
print(email)  # Output: john@example.com
print(student)  # Output: {'name': 'John', 'age': 21, 'email': 'john@example.com'}

# Key already exists, so original value is returned
name = student.setdefault('name', 'Jane')
print(name)  # Output: John (not Jane)
```

## Nested Dictionaries

Dictionaries can contain other dictionaries, creating nested structures:

```python
# Nested dictionary representing a student database
students = {
    '1001': {
        'name': 'John Doe',
        'age': 21,
        'courses': ['Math', 'Physics']
    },
    '1002': {
        'name': 'Jane Smith',
        'age': 20,
        'courses': ['Chemistry', 'Biology']
    }
}

# Accessing values in nested dictionaries
print(students['1001']['name'])  # Output: John Doe
print(students['1002']['courses'][0])  # Output: Chemistry

# Adding a new student
students['1003'] = {
    'name': 'Bob Johnson',
    'age': 22,
    'courses': ['Computer Science', 'Statistics']
}
```

---

## Common Dictionary Operations

### Checking if a Key Exists

You can use the `in` operator to check if a key exists in a dictionary:

```python
student = {'name': 'John', 'age': 21}

# Check if a key exists
print('name' in student)  # Output: True
print('grade' in student)  # Output: False
```

### Iterating Through a Dictionary

There are several ways to iterate through a dictionary:

```python
student = {'name': 'John', 'age': 21, 'city': 'New York'}

# Iterate through keys (default)
for key in student:
    print(key, student[key])

# Iterate through keys explicitly
for key in student.keys():
    print(key)

# Iterate through values
for value in student.values():
    print(value)

# Iterate through key-value pairs
for key, value in student.items():
    print(key, ":", value)
```

### Finding the Length of a Dictionary

The `len()` function returns the number of key-value pairs in a dictionary:

```python
student = {'name': 'John', 'age': 21, 'city': 'New York'}
print(len(student))  # Output: 3
```

## Dictionary as Function Arguments

Dictionaries can be unpacked and used as function arguments using the double asterisk (`**`) operator:

```python
def display_person(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Dictionary to unpack
person = {'name': 'John', 'age': 21, 'city': 'New York'}

# Unpack the dictionary as keyword arguments
display_person(**person)
# Output: Name: John, Age: 21, City: New York
```

## Advanced Dictionary Techniques

### Merging Dictionaries

In Python 3.5+, you can use the unpacking operator to merge dictionaries:

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge dictionaries (later values override earlier ones)
merged = {**dict1, **dict2}
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}
```

In Python 3.9+, you can use the pipe operator:

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge with the pipe operator
merged = dict1 | dict2
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}
```

### OrderedDict and Dictionary Order

Since Python 3.7, regular dictionaries maintain insertion order by default. Before that, you could use `OrderedDict` from the `collections` module:

```python
from collections import OrderedDict

# Create an ordered dictionary
ordered = OrderedDict([('apple', 4.5), ('banana', 3.2), ('orange', 2.0)])

# Regular dictionaries also maintain order in Python 3.7+
regular = {'apple': 4.5, 'banana': 3.2, 'orange': 2.0}
```

### defaultdict for Default Values

The `defaultdict` from the `collections` module automatically provides default values for nonexistent keys:

```python
from collections import defaultdict

# Create a defaultdict that defaults to 0
fruit_count = defaultdict(int)

fruits = ['apple', 'banana', 'orange', 'apple', 'apple', 'banana']

# Count occurrences
for fruit in fruits:
    fruit_count[fruit] += 1

print(fruit_count)
# Output: defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'orange': 1})
```

### Counter for Frequency Counting

The `Counter` class is a specialized dictionary for counting hashable objects:

```python
from collections import Counter

# Count occurrences in a list
fruits = ['apple', 'banana', 'orange', 'apple', 'apple', 'banana']
fruit_counter = Counter(fruits)

print(fruit_counter)
# Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Most common elements
print(fruit_counter.most_common(2))
# Output: [('apple', 3), ('banana', 2)]
```

## Real-World Applications of Dictionaries

### Data Processing

Dictionaries are excellent for processing and analyzing data:

```python
# Sales data by quarter
sales_data = {
    'Q1': {'jan': 100, 'feb': 110, 'mar': 125},
    'Q2': {'apr': 130, 'may': 115, 'jun': 135},
    'Q3': {'jul': 140, 'aug': 145, 'sep': 155},
    'Q4': {'oct': 160, 'nov': 165, 'dec': 170}
}

# Calculate total annual sales
annual_sales = sum(
    month_sales
    for quarter in sales_data.values()
    for month_sales in quarter.values()
)
print(f"Annual sales: ${annual_sales}")
```

### Configuration and Settings

Dictionaries are perfect for storing configuration settings:

```python
# Application configuration
config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'user': 'admin',
        'password': 'secret'
    },
    'api': {
        'endpoint': 'https://api.example.com',
        'timeout': 30,
        'retry_limit': 3
    },
    'logging': {
        'level': 'INFO',
        'file': 'app.log'
    }
}

# Access configuration settings
db_host = config['database']['host']
api_timeout = config['api']['timeout']
```
