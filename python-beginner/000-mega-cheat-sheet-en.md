# Python Cheat Sheet

## Table of Contents
- [Data Types](#data-types)
- [Variables](#variables)
- [Operators](#operators)
- [Control Flow](#control-flow)
- [Data Structures](#data-structures)
- [Functions](#functions)
- [File Operations](#file-operations)
- [Modules and Packages](#modules-and-packages)
- [Exception Handling](#exception-handling)
- [Classes and OOP](#classes-and-oop)
- [Working with Paths (pathlib)](#working-with-paths-pathlib)
- [Common Built-in Functions](#common-built-in-functions)
- [String Formatting](#string-formatting)
- [Generators and Iterators](#generators-and-iterators)
- [Standard Library Highlights](#standard-library-highlights)
- [Virtual Environments](#virtual-environments)
- [Type Hints](#type-hints)
- [Async Programming](#async-programming)
- [Debugging and Logging](#debugging-and-logging)
- [Testing](#testing)
- [Performance Tips](#performance-tips)
- [Best Practices and Common Gotchas](#best-practices-and-common-gotchas)

## Data Types

### Basic Types
- **int**: Integer numbers (`1`, `42`, `-7`)
- **float**: Floating-point numbers (`3.14`, `-0.001`, `2e3`)
- **bool**: Boolean values (`True`, `False`)
- **str**: Strings (`"hello"`, `'world'`, `"""multi-line"""`)
- **NoneType**: The `None` value (represents absence of value)
- **complex**: Complex numbers (`3+4j`)

### Type Conversion
```python
# Converting between types
int("42")       # 42
float(42)       # 42.0
str(42)         # "42"
bool(0)         # False (0, "", [], {}, None are False)
bool(42)        # True (any non-zero/empty value)
```

### Checking Types
```python
type(42)        # <class 'int'>
isinstance(42, int)  # True
```

## Variables

### Variable Assignment
```python
x = 5           # Basic assignment
x, y = 5, 10    # Multiple assignment
x += 1          # Augmented assignment (x = x + 1)
```

### Variable Naming Rules
- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Case-sensitive
- Cannot use Python keywords (if, else, for, etc.)

### Constants
```python
# Convention: Constants use ALL_CAPS
PI = 3.14159
MAX_SIZE = 100
```

## Operators

### Arithmetic Operators
```python
a + b    # Addition
a - b    # Subtraction
a * b    # Multiplication
a / b    # Division (returns float)
a // b   # Floor division (integer division)
a % b    # Modulus (remainder)
a ** b   # Exponentiation (a to the power of b)
```

### Comparison Operators
```python
a == b   # Equal to
a != b   # Not equal to
a > b    # Greater than
a < b    # Less than
a >= b   # Greater than or equal to
a <= b   # Less than or equal to
```

### Logical Operators
```python
a and b  # True if both a and b are True
a or b   # True if either a or b is True
not a    # Inverts the boolean value of a
```

### Identity Operators
```python
a is b      # True if a and b refer to the same object
a is not b  # True if a and b do not refer to the same object
```

### Membership Operators
```python
a in b      # True if a is a member of b (list, tuple, string, etc.)
a not in b  # True if a is not a member of b
```

### Bitwise Operators
```python
a & b    # Bitwise AND
a | b    # Bitwise OR
a ^ b    # Bitwise XOR
~a       # Bitwise NOT
a << b   # Left shift
a >> b   # Right shift
```

## Control Flow

### Conditional Statements
```python
# if statement
if condition:
    # code to execute if condition is True
elif another_condition:
    # code to execute if another_condition is True
else:
    # code to execute if all conditions are False

# Ternary operator (conditional expression)
value = x if condition else y
```

### Loops
```python
# for loop
for item in iterable:
    # code to execute for each item
    
    if condition:
        continue  # Skip to next iteration
    if condition:
        break     # Exit the loop
else:
    # Executes after loop completes normally (not via break)

# for loop with range
for i in range(start, stop, step):
    # code to execute

# while loop
while condition:
    # code to execute while condition is True
    
    if condition:
        continue  # Skip to next iteration
    if condition:
        break     # Exit the loop
else:
    # Executes after loop completes normally (not via break)
```

### Match Statement (Python 3.10+)
```python
match value:
    case pattern1:
        # code for pattern1
    case pattern2:
        # code for pattern2
    case _:
        # default case
```

## Data Structures

### Lists
```python
# Creating lists
my_list = [1, 2, 3, 4, 5]
empty_list = []
list_from_iterable = list("hello")  # ['h', 'e', 'l', 'l', 'o']

# Accessing elements
first_item = my_list[0]       # First item (1)
last_item = my_list[-1]       # Last item (5)
subset = my_list[1:3]         # Slicing [2, 3]

# Common operations
my_list.append(6)             # Add to end
my_list.insert(0, 0)          # Insert at position
my_list.extend([7, 8, 9])     # Add multiple items
my_list.remove(3)             # Remove first occurrence
popped_item = my_list.pop()   # Remove and return last item
popped_item = my_list.pop(0)  # Remove and return item at index
my_list.index(4)              # Find index of value
3 in my_list                  # Check if value exists (True/False)
len(my_list)                  # Get length
my_list.sort()                # Sort in place
sorted_list = sorted(my_list) # Return sorted copy
my_list.reverse()             # Reverse in place
my_list.count(2)              # Count occurrences
my_list.clear()               # Remove all items

# List comprehensions
[x**2 for x in range(10)]                 # Create list of squares
[x for x in range(10) if x % 2 == 0]      # Even numbers only
```

### Tuples
```python
# Creating tuples
my_tuple = (1, 2, 3, 4, 5)
empty_tuple = ()
single_item_tuple = (1,)  # Comma is necessary
tuple_from_iterable = tuple("hello")

# Accessing elements (same as lists)
first_item = my_tuple[0]
subset = my_tuple[1:3]

# Common operations
len(my_tuple)           # Get length
my_tuple.count(2)       # Count occurrences
my_tuple.index(4)       # Find index of value
3 in my_tuple           # Check if value exists

# Tuples are immutable (cannot be changed after creation)
```

### Dictionaries
```python
# Creating dictionaries
my_dict = {"key1": "value1", "key2": "value2"}
empty_dict = {}
dict_with_constructor = dict(key1="value1", key2="value2")

# Accessing elements
value = my_dict["key1"]                  # Raises KeyError if key doesn't exist
value = my_dict.get("key1", "default")   # Returns default if key doesn't exist

# Common operations
my_dict["key3"] = "value3"             # Add or update key-value pair
del my_dict["key1"]                    # Delete key-value pair
popped_value = my_dict.pop("key2")     # Remove and return value
"key1" in my_dict                      # Check if key exists
my_dict.keys()                         # View of all keys
my_dict.values()                       # View of all values
my_dict.items()                        # View of all (key, value) pairs
my_dict.update({"key4": "value4"})     # Add multiple key-value pairs
my_dict.clear()                        # Remove all items

# Dictionary comprehensions
{x: x**2 for x in range(5)}           # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Sets
```python
# Creating sets
my_set = {1, 2, 3, 4, 5}
empty_set = set()  # Not {} which creates empty dict
set_from_iterable = set("hello")  # {'h', 'e', 'l', 'o'}

# Common operations
my_set.add(6)                   # Add element
my_set.remove(3)                # Remove element (raises KeyError if not present)
my_set.discard(3)               # Remove element if present
popped_item = my_set.pop()      # Remove and return arbitrary element
my_set.clear()                  # Remove all elements
3 in my_set                     # Check if element exists
len(my_set)                     # Get number of elements

# Set operations
a.union(b)             # Elements in a or b (a | b)
a.intersection(b)      # Elements in both a and b (a & b)
a.difference(b)        # Elements in a but not in b (a - b)
a.symmetric_difference(b)  # Elements in a or b but not both (a ^ b)
a.issubset(b)          # True if all elements of a are in b
a.issuperset(b)        # True if all elements of b are in a
a.isdisjoint(b)        # True if a and b have no elements in common

# Set comprehensions
{x**2 for x in range(10)}
```

## Functions

### Defining and Calling Functions
```python
# Basic function
def function_name(param1, param2):
    """Docstring describing the function."""
    # Function body
    return result

# Calling a function
result = function_name(arg1, arg2)

# Function with default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Functions with variable number of arguments
def func(*args, **kwargs):
    # args is a tuple of positional arguments
    # kwargs is a dictionary of keyword arguments
    pass
```

### Lambda Functions
```python
# Anonymous function
square = lambda x: x**2

# Used with built-in functions
sorted(items, key=lambda x: x[1])
map(lambda x: x**2, numbers)
filter(lambda x: x > 0, numbers)
```

### Function Decorators
```python
# Decorator function
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper

# Using a decorator
@my_decorator
def my_function():
    pass
```

## File Operations

### Opening and Closing Files
```python
# Basic file opening (always use with statement for auto-closing)
with open('filename.txt', 'mode') as file:
    # File operations here
    pass
```

### File Modes
- `'r'`: Read (default) - open for reading
- `'w'`: Write - open for writing, truncate file first
- `'a'`: Append - open for writing, append to end of file
- `'x'`: Exclusive creation - fail if file already exists
- `'b'`: Binary mode (added to other modes)
- `'t'`: Text mode (default, added to other modes)
- `'+'`: Update mode - open for updating (reading and writing)

### Reading Files
```python
# Read entire file as string
with open('file.txt', 'r') as file:
    content = file.read()

# Read line by line
with open('file.txt', 'r') as file:
    for line in file:
        # Process line
        pass

# Read all lines into a list
with open('file.txt', 'r') as file:
    lines = file.readlines()

# Read specific number of bytes
with open('file.txt', 'r') as file:
    chunk = file.read(1024)  # Read 1024 bytes
```

### Writing Files
```python
# Write string to file
with open('file.txt', 'w') as file:
    file.write('Hello, World!')

# Write multiple lines
with open('file.txt', 'w') as file:
    file.writelines(['Line 1\n', 'Line 2\n'])
```

### Working with Binary Files
```python
# Read binary data
with open('file.bin', 'rb') as file:
    binary_data = file.read()

# Write binary data
with open('file.bin', 'wb') as file:
    file.write(binary_data)
```

## Working with Paths (pathlib)

### Creating Path Objects
```python
from pathlib import Path

# Current directory
current_dir = Path.cwd()

# Home directory
home_dir = Path.home()

# Specific path
path = Path('/usr/local/bin')
path = Path('relative/path')
path = Path('file.txt')

# Combine paths
new_path = Path('directory') / 'file.txt'
```

### Path Information
```python
# Path parts
path.name          # 'file.txt' (filename with extension)
path.stem          # 'file' (filename without extension)
path.suffix        # '.txt' (file extension)
path.parent        # Path object representing parent directory
path.parents       # Iterator of all parents

# Path properties
path.exists()      # True if path exists
path.is_file()     # True if path is a file
path.is_dir()      # True if path is a directory
path.is_absolute() # True if path is absolute
path.absolute()    # Returns absolute path
```

### Path Operations
```python
# Creating directories
Path('new_dir').mkdir()                    # Create single directory
Path('nested/dirs').mkdir(parents=True)    # Create parent dirs too
Path('temp_dir').mkdir(exist_ok=True)      # Don't error if exists

# Listing directory contents
for item in Path('.').iterdir():           # List all items
    print(item)

# Finding files with glob patterns
for file in Path('.').glob('*.py'):        # All .py files in current dir
    print(file)

for file in Path('.').rglob('*.py'):       # Recursive search
    print(file)

# File operations
path = Path('file.txt')
if path.exists():
    path.unlink()          # Delete file
    
old_path = Path('old.txt')
new_path = Path('new.txt')
old_path.rename(new_path)  # Rename/move file

# Reading/writing with pathlib
content = path.read_text()                  # Read text file
path.write_text('Hello, World!')            # Write text file
binary_data = path.read_bytes()             # Read binary file
path.write_bytes(binary_data)               # Write binary file
```

## Modules and Packages

### Importing Modules
```python
# Basic import
import module_name

# Import with alias
import module_name as alias

# Import specific items
from module_name import function_name, ClassName

# Import all items (not recommended)
from module_name import *
```

### Creating Modules
```python
# In mymodule.py
def my_function():
    return "Hello from my_function"

class MyClass:
    pass

# Using the module
import mymodule
mymodule.my_function()
```

### Creating Packages
```
mypackage/
│
├── __init__.py
├── module1.py
└── module2.py
```

## Exception Handling

### Basic Try-Except
```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle specific exception
    print("Cannot divide by zero")
except (TypeError, ValueError) as e:
    # Handle multiple exceptions and get error message
    print(f"Error: {e}")
except Exception as e:
    # Handle any other exception
    print(f"Unexpected error: {e}")
else:
    # Executes if no exception occurred
    print("No exceptions!")
finally:
    # Always executes
    print("Cleanup code")
```

### Raising Exceptions
```python
raise ValueError("Invalid value")

# Re-raising exception
try:
    # Some code
    pass
except ValueError:
    # Do something
    raise  # Re-raise the caught exception
```

### Custom Exceptions
```python
class MyCustomError(Exception):
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        super().__init__(self.message)

# Using custom exception
raise MyCustomError("Something went wrong", code=500)
```

### Context Managers
```python
# Using a context manager (with statement)
with open('file.txt', 'r') as file:
    content = file.read()
# File automatically closed

# Creating a context manager
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    # Setup code
    try:
        yield  # Value yielded is assigned to variable in with statement
    finally:
        # Cleanup code
```

## Classes and OOP

### Defining Classes
```python
class ClassName:
    """Class docstring."""
    
    # Class variable (shared by all instances)
    class_variable = "I'm shared"
    
    # Constructor (initialization)
    def __init__(self, param1, param2):
        # Instance variables (unique to each instance)
        self.param1 = param1
        self.param2 = param2
        self._private_var = 42  # Convention for private (not enforced)
    
    # Instance method
    def method_name(self, param):
        return param + self.param1
    
    # Static method (doesn't use instance)
    @staticmethod
    def static_method(param):
        return param * 2
    
    # Class method (uses class, not instance)
    @classmethod
    def class_method(cls, param):
        return cls(param, "default")
    
    # Property (getter)
    @property
    def property_name(self):
        return self._private_var
    
    # Property setter
    @property_name.setter
    def property_name(self, value):
        self._private_var = value
```

### Inheritance
```python
class ParentClass:
    def __init__(self, param):
        self.param = param
    
    def method(self):
        return "Parent method"

class ChildClass(ParentClass):
    def __init__(self, param, other_param):
        # Call parent class constructor
        super().__init__(param)
        self.other_param = other_param
    
    # Override parent method
    def method(self):
        # Call parent method
        parent_result = super().method()
        return f"{parent_result} extended in child"
```

### Multiple Inheritance
```python
class A:
    def method(self):
        return "A"

class B:
    def method(self):
        return "B"

class C(A, B):  # Method resolution order: C -> A -> B
    pass
```

### Magic Methods
```python
class MyClass:
    def __str__(self):
        # String representation for str()
        return "String representation"
    
    def __repr__(self):
        # Representation for repr()
        return "MyClass()"
    
    def __len__(self):
        # For len()
        return 42
    
    def __call__(self, *args):
        # Makes object callable like a function
        return sum(args)
    
    def __getitem__(self, key):
        # For indexing: obj[key]
        return f"Value for {key}"
    
    def __eq__(self, other):
        # For equality: obj == other
        return True
```

## Standard Library Highlights

### collections
```python
from collections import defaultdict, Counter, namedtuple, deque, OrderedDict

# defaultdict - dictionary with default values for missing keys
word_count = defaultdict(int)
for word in ['apple', 'banana', 'apple', 'orange']:
    word_count[word] += 1  # No KeyError for new keys

# Counter - count occurrences of elements
counter = Counter(['apple', 'banana', 'apple', 'orange'])
counter['apple']  # 2
counter.most_common(2)  # [('apple', 2), ('banana', 1)]

# namedtuple - tuple with named fields
Person = namedtuple('Person', ['name', 'age', 'city'])
alice = Person('Alice', 30, 'New York')
alice.name  # 'Alice'
alice[0]    # 'Alice'

# deque - double-ended queue with fast append/pop from both ends
queue = deque(['a', 'b', 'c'])
queue.append('d')         # Add to right: ['a', 'b', 'c', 'd']
queue.appendleft('z')     # Add to left: ['z', 'a', 'b', 'c', 'd']
queue.pop()               # Remove from right: 'd'
queue.popleft()           # Remove from left: 'z'

# OrderedDict - dictionary that remembers insertion order (pre-Python 3.7)
od = OrderedDict([('first', 1), ('second', 2)])
```

### datetime
```python
from datetime import datetime, date, time, timedelta

# Create date/time objects
now = datetime.now()           # Current local datetime
today = date.today()           # Current local date
specific_date = date(2023, 12, 31)
specific_time = time(13, 30, 15)  # 1:30:15 PM
specific_dt = datetime(2023, 12, 31, 13, 30, 15)

# Formatting and parsing
formatted = now.strftime("%Y-%m-%d %H:%M:%S")  # Format to string
parsed = datetime.strptime("2023-12-31", "%Y-%m-%d")  # Parse from string

# Time spans and arithmetic
delta = timedelta(days=7, hours=3)
next_week = now + delta
days_diff = (date(2023, 12, 31) - date(2023, 1, 1)).days  # 364
```

a more modern way to work with dates. and a whole lot easier.
because datetime is a bit of a pain to work with.
[Whenever](https://github.com/ariebovenberg/whenever)


### re (Regular Expressions)
```python
import re

text = "The quick brown fox jumped over the lazy dog"

# Search for a pattern
match = re.search(r"brown", text)  # Returns Match object or None
if match:
    print(match.group())  # 'brown'
    print(match.start())  # 10 (start position)
    print(match.end())    # 15 (end position)

# Find all occurrences
matches = re.findall(r"\w+", text)  # ['The', 'quick', 'brown', ...]

# Substitute text
new_text = re.sub(r"fox", "cat", text)  # Replace fox with cat

# Split string
parts = re.split(r"\s+", text)  # Split on whitespace

# Common patterns
# \d - digit, \w - word char, \s - whitespace, [a-z] - char class
# + - 1 or more, * - 0 or more, ? - 0 or 1, {n} - exactly n times
# ^ - start of string, $ - end of string

# Compile for better performance when used multiple times
pattern = re.compile(r"\d+")
matches = pattern.findall("123 abc 456")
```

### json
```python
import json

# Python object to JSON string
data = {'name': 'Alice', 'age': 30, 'is_student': False}
json_str = json.dumps(data, indent=2)  # Pretty-printed with indentation

# JSON string to Python object
python_obj = json.loads(json_str)

# Reading/writing JSON files
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

with open('data.json', 'r') as f:
    loaded_data = json.load(f)
```

### csv
```python
import csv

# Reading CSV
with open('data.csv', 'r', newline='') as file:
    # Basic reader
    reader = csv.reader(file)
    for row in reader:
        print(row)  # row is a list
    
    # Dict reader
    file.seek(0)  # Go back to start of file
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        print(row['column_name'])  # Access by column name

# Writing CSV
with open('output.csv', 'w', newline='') as file:
    # Basic writer
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])  # Write header
    writer.writerow(['Alice', 30])    # Write data
    
    # Dict writer
    dict_writer = csv.DictWriter(file, fieldnames=['Name', 'Age'])
    dict_writer.writeheader()
    dict_writer.writerow({'Name': 'Bob', 'Age': 25})
```

### os and os.path
```python
import os

# File and directory operations
os.getcwd()              # Get current working directory
os.chdir('/path/to/dir') # Change directory
os.listdir('.')          # List directory contents
os.mkdir('new_dir')      # Create directory
os.makedirs('a/b/c')     # Create nested directories
os.remove('file.txt')    # Delete file
os.rmdir('empty_dir')    # Delete empty directory
os.rename('old.txt', 'new.txt')  # Rename file or directory

# Path operations with os.path
os.path.join('dir', 'subdir', 'file.txt')  # Joins paths correctly for platform
os.path.exists('file.txt')       # Check if file/directory exists
os.path.isfile('file.txt')       # Check if path is a file
os.path.isdir('dir')             # Check if path is a directory
os.path.abspath('file.txt')      # Get absolute path
os.path.basename('/a/b/c.txt')   # 'c.txt' (filename)
os.path.dirname('/a/b/c.txt')    # '/a/b' (directory)
os.path.splitext('file.txt')     # ('file', '.txt') (split extension)
```

### random
```python
import random

# Random numbers
random.random()       # Float between 0 and 1
random.randint(1, 10)  # Integer between 1 and 10 (inclusive)
random.uniform(1, 10)  # Float between 1 and 10
random.gauss(0, 1)     # Gaussian distribution (mean=0, std=1)

# Sequence operations
random.choice(['a', 'b', 'c'])         # Random element
random.sample(['a', 'b', 'c', 'd'], 2)  # 2 unique random elements
items = ['a', 'b', 'c']
random.shuffle(items)                  # Shuffle in-place

# Setting a seed for reproducibility
random.seed(42)
```

## Common Built-in Functions

```python
# Data type conversion
int(), float(), str(), bool(), list(), dict(), set(), tuple()

# Math
abs(x)           # Absolute value
max(iterable)    # Maximum value
min(iterable)    # Minimum value
round(x, ndigits=0)  # Round to ndigits
sum(iterable)    # Sum of all elements
pow(x, y)        # x raised to power y (x**y)
divmod(x, y)     # Returns (x//y, x%y) tuple

# Iteration
range(start, stop, step)  # Sequence generator
enumerate(iterable)       # Return (index, value) pairs
zip(iter1, iter2)         # Combine iterables
map(function, iterable)   # Apply function to all items
filter(function, iterable)  # Filter items by function
sorted(iterable, key=None, reverse=False)  # Return sorted list
reversed(sequence)        # Return reversed iterator
all(iterable)             # True if all elements are truthy
any(iterable)             # True if any element is truthy

# Object information
len(obj)         # Number of items
type(obj)        # Type of object
id(obj)          # Unique identifier
dir(obj)         # List of attributes
help(obj)        # Interactive help
isinstance(obj, class)  # Check if object is instance of class
issubclass(cls, class)  # Check if class is subclass
hasattr(obj, name)      # Check if object has attribute
getattr(obj, name, default)  # Get attribute, with optional default
```

## String Formatting

### F-strings (Python 3.6+)
```python
name = "World"
age = 42
# Basic f-string
greeting = f"Hello, {name}! You are {age} years old."

# Expressions in f-strings
result = f"2 + 2 = {2 + 2}"

# Formatting specifiers
pi = 3.14159
formatted = f"Pi is approximately {pi:.2f}"  # "Pi is approximately 3.14"

# Padding and alignment
left_aligned = f"{name:<10}"  # Left align, width 10
right_aligned = f"{name:>10}"  # Right align, width 10
center_aligned = f"{name:^10}"  # Center align, width 10

# Thousands separator
large_number = 1000000
formatted = f"{large_number:,}"  # "1,000,000"

# Binary, octal, hex representation
number = 42
binary = f"{number:b}"    # "101010"
octal = f"{number:o}"     # "52"
hex_lower = f"{number:x}"  # "2a"
hex_upper = f"{number:X}"  # "2A"

# Debugging with f-strings (Python 3.8+)
debug = f"{name=}, {age=}"  # "name='World', age=42"
```

### str.format() Method
```python
# Basic formatting
"Hello, {}!".format(name)

# Positional arguments
"{0} is {1} years old".format(name, age)

# Named arguments
"{name} is {age} years old".format(name="Alice", age=30)

# Formatting specifiers (similar to f-strings)
"Pi is approximately {:.2f}".format(3.14159)
```

### %-formatting (older style)
```python
# Basic substitution
"Hello, %s!" % name

# Multiple substitutions
"%s is %d years old" % (name, age)

# Named substitutions
"%(name)s is %(age)d years old" % {"name": "Alice", "age": 30}

# Common specifiers:
# %s - string, %d - integer, %f - float, %x - hex, %o - octal
```

### Common String Methods
```python
s = "Hello, World!"

# Case manipulation
s.upper()           # "HELLO, WORLD!"
s.lower()           # "hello, world!"
s.capitalize()      # "Hello, world!"
s.title()           # "Hello, World!"
s.swapcase()        # "hELLO, wORLD!"

# Searching
s.find("World")     # 7 (index of first occurrence, -1 if not found)
s.index("World")    # 7 (like find but raises ValueError if not found)
s.count("l")        # 3 (count occurrences)
s.startswith("Hello")  # True
s.endswith("!")     # True

# Validation
s.isalpha()         # False (checks if all characters are alphabetic)
s.isdigit()         # False (checks if all characters are digits)
s.isalnum()         # False (checks if all characters are alphanumeric)
s.islower()         # False (checks if all characters are lowercase)
s.isupper()         # False (checks if all characters are uppercase)
s.isspace()         # False (checks if all characters are whitespace)

# Transformation
s.strip()           # Remove whitespace from beginning and end
s.lstrip()          # Remove whitespace from beginning
s.rstrip()          # Remove whitespace from end
s.replace("World", "Python")  # "Hello, Python!"
",".join(["a", "b", "c"])     # "a,b,c"
"a,b,c".split(",")            # ["a", "b", "c"]
"  a  b  ".split()            # ["a", "b"] (splits on whitespace)
```

## Virtual Environments

### Creating Virtual Environments
```python
# Create a virtual environment using venv
python -m venv myenv

# Activate the virtual environment
# On Windows:
myenv\Scripts\activate
# On macOS/Linux:
source myenv/bin/activate

# Deactivate the virtual environment
deactivate
```

### Managing Packages with pip
```bash
# Install a package
pip install package_name

# Install specific version
pip install package_name==1.2.3

# Install with version constraints
pip install "package_name>=1.2.3,<2.0.0"

# Upgrade a package
pip install --upgrade package_name

# Uninstall a package
pip uninstall package_name

# List installed packages
pip list

# Show details about a package
pip show package_name

# Freeze current environment
pip freeze > requirements.txt

# Install from requirements file
pip install -r requirements.txt
```

### Managing Virtual Environments with Poetry
```bash
# Install Poetry
pip install poetry

# Create a new project
poetry new my-project

# Initialize existing project
poetry init

# Add dependencies
poetry add requests
poetry add pytest --dev  # Development dependency

# Install dependencies
poetry install

# Update dependencies
poetry update

# Activate the virtual environment
poetry shell

# Run a command in the environment
poetry run python script.py
```

## Type Hints

### Basic Type Annotations (Python 3.5+)
```python
# Variable annotations
name: str = "Alice"
age: int = 30
is_student: bool = False
height: float = 1.75
values: list[int] = [1, 2, 3]  # Python 3.9+ syntax
values: List[int] = [1, 2, 3]  # Pre-Python 3.9 syntax (needs from typing import List)

# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Function with multiple parameters
def process_items(items: list[str], count: int = 10) -> None:
    pass
```

### Using the typing Module
```python
from typing import List, Dict, Tuple, Set, Optional, Union, Any, Callable, TypeVar

# Container types
names: List[str] = ["Alice", "Bob"]
ages: Dict[str, int] = {"Alice": 30, "Bob": 25}
point: Tuple[int, int] = (10, 20)
unique_numbers: Set[int] = {1, 2, 3}

# Optional (value or None)
maybe_name: Optional[str] = None  # Same as Union[str, None]

# Union (multiple possible types)
id_number: Union[int, str] = "A12345"  # Can be int or str

# Any (any type, disables type checking)
data: Any = get_data()

# Callable (functions)
callback: Callable[[int, str], bool] = lambda x, y: True  # Takes int, str, returns bool

# TypeVar (generic types)
T = TypeVar('T')
def first(items: List[T]) -> T:
    return items[0]
```

### Type Aliases and NewType
```python
from typing import List, Dict, NewType

# Type aliases
UserId = int
Vector = List[float]

def process_user(user_id: UserId) -> None:
    pass

# NewType (creates a distinct type)
UserId = NewType('UserId', int)
user_id = UserId(123)  # Type is UserId, not int
```

### Generics
```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []
        
    def push(self, item: T) -> None:
        self.items.append(item)
        
    def pop(self) -> T:
        return self.items.pop()

# Usage
stack = Stack[int]()  # Stack of integers
stack.push(42)
```

### Type Checking Tools
```bash
# Install mypy
pip install mypy

# Run type checking
mypy script.py
```

## Async Programming

### Basics
```python
import asyncio

# Define coroutine function
async def say_hello(name: str) -> str:
    await asyncio.sleep(1)  # Non-blocking sleep
    return f"Hello, {name}!"

# Run coroutine in asyncio event loop
async def main():
    result = await say_hello("World")
    print(result)

# Python 3.7+
asyncio.run(main())
```

### Running Tasks Concurrently
```python
import asyncio
import time

async def fetch_data(url: str) -> str:
    print(f"Fetching {url}")
    await asyncio.sleep(1)  # Simulating network request
    return f"Data from {url}"

async def main():
    # Sequential execution
    start = time.time()
    result1 = await fetch_data("url1")
    result2 = await fetch_data("url2")
    print(f"Sequential: {time.time() - start:.2f} seconds")
    
    # Concurrent execution
    start = time.time()
    results = await asyncio.gather(
        fetch_data("url1"),
        fetch_data("url2")
    )
    print(f"Concurrent: {time.time() - start:.2f} seconds")

asyncio.run(main())
```

### Creating Tasks
```python
async def main():
    # Create and schedule a task
    task = asyncio.create_task(fetch_data("url"))
    
    # Do other work while the task runs
    print("Doing other work")
    
    # Wait for the task to complete
    result = await task
    
    # Run tasks with timeout
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=1.0)
    except asyncio.TimeoutError:
        print("Operation timed out")
```

### Working with Asynchronous Iterators
```python
async def async_generator():
    for i in range(5):
        await asyncio.sleep(0.1)
        yield i

async def main():
    # Async for loop
    async for value in async_generator():
        print(value)
    
    # Async comprehension (Python 3.6+)
    result = [value async for value in async_generator()]
```

## Generators and Iterators

### Creating Generators
```python
# Generator function using yield
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Using the generator
for number in count_up_to(5):
    print(number)  # Prints 1, 2, 3, 4, 5

# Generator expressions (similar to list comprehensions)
squares_gen = (x**2 for x in range(10))
```

### Generator Methods
```python
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
next(gen)  # 1
next(gen)  # 2
next(gen)  # 3
# next(gen)  # Raises StopIteration

# send() method
def echo_generator():
    while True:
        received = yield
        yield f"Echo: {received}"

echo = echo_generator()
next(echo)  # Prime the generator
echo.send("Hello")  # "Echo: Hello"
```

### Iterators
```python
# Create an iterator from an iterable
my_list = [1, 2, 3]
iterator = iter(my_list)

# Get next item
next(iterator)  # 1

# Custom iterator class
class Counter:
    def __init__(self, max):
        self.max = max
        self.count = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.count >= self.max:
            raise StopIteration
        self.count += 1
        return self.count
```

### itertools Module Highlights
```python
import itertools

# Infinite iterators
count = itertools.count(10, 2)     # 10, 12, 14, ...
cycle = itertools.cycle("ABC")     # A, B, C, A, B, C, ...
repeat = itertools.repeat(42, 3)   # 42, 42, 42

# Combinatoric iterators
permutations = itertools.permutations("ABC", 2)  # All permutations of length 2
combinations = itertools.combinations("ABC", 2)  # All combinations of length 2
product = itertools.product("AB", "12")         # Cartesian product

# Terminating iterators
chain = itertools.chain("ABC", "123")  # A, B, C, 1, 2, 3
islice = itertools.islice(range(10), 2, 8, 2)  # 2, 4, 6
groupby = itertools.groupby("AAABBBCCA")  # Group by consecutive elements
```

## Debugging and Logging

### Debugging with pdb
```python
# Basic debugging
import pdb

def buggy_function():
    x = 10
    y = 0
    pdb.set_trace()  # Start debugger here
    z = x / y  # This will cause an error
    return z

# Common pdb commands:
# n - next line
# s - step into function
# c - continue execution
# p variable - print variable
# l - show current line
# q - quit debugger
```

### Post-mortem Debugging
```python
try:
    result = buggy_function()
except Exception:
    import pdb
    pdb.post_mortem()  # Start debugger at the point of exception
```

### Breakpoint() function (Python 3.7+)
```python
def buggy_function():
    x = 10
    y = 0
    breakpoint()  # Equivalent to pdb.set_trace()
    z = x / y
    return z
```

### Logging
```python
import logging

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log'  # Optional: write to file instead of console
)

# Logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.debug("Detailed information for debugging")
logging.info("Confirmation that things are working")
logging.warning("Something unexpected happened")
logging.error("A more serious problem")
logging.critical("A fatal error")

# Creating a custom logger
logger = logging.getLogger('my_module')
logger.setLevel(logging.DEBUG)

# Add handler with custom formatter
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Using the custom logger
logger.debug("Debug message from custom logger")
```

## Testing

### unittest
```python
import unittest

# Function to test
def add(a, b):
    return a + b

# Test case class
class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add(3, 5)
        self.assertEqual(result, 8)
    
    def test_add_negative_numbers(self):
        result = add(-1, -1)
        self.assertEqual(result, -2)
    
    def test_add_zeros(self):
        result = add(0, 0)
        self.assertEqual(result, 0)
    
    # Setup and teardown methods
    def setUp(self):
        # Code to run before each test
        pass
    
    def tearDown(self):
        # Code to run after each test
        pass

# Run the tests
if __name__ == "__main__":
    unittest.main()
```

### pytest
```python
# Install: pip install pytest

# No special classes needed, just functions
def test_add_positive():
    assert add(3, 5) == 8

def test_add_negative():
    assert add(-1, -1) == -2

# Fixtures (setup and teardown)
import pytest

@pytest.fixture
def sample_data():
    # Setup
    data = {"key": "value"}
    yield data
    # Teardown (code after yield runs after test)
    # Clean up resources here

def test_with_fixture(sample_data):
    assert sample_data["key"] == "value"

# Parametrized tests
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, 5, 10),
    (0, 0, 0),
    (-1, 1, 0)
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

# Run pytest from command line:
# pytest test_file.py
# pytest test_file.py::test_function_name
# pytest -v (verbose)
# pytest -xvs (verbose, stop at first failure, print output)
```

### doctest
```python
def add(a, b):
    """
    Add two numbers and return the result.
    
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    """
    return a + b

# Run doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

## Performance Tips

### Profiling
```python
# Simple timing
import time

start = time.time()
# Code to profile
result = expensive_function()
end = time.time()
print(f"Time elapsed: {end - start:.6f} seconds")

# Using timeit for more accurate microbenchmarks
import timeit

# Time a single statement
seconds = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

# Time a function
def test_function():
    return [i**2 for i in range(1000)]

seconds = timeit.timeit(test_function, number=1000)

# cProfile for detailed profiling
import cProfile

cProfile.run('expensive_function()')

# Profile and save results to file
cProfile.run('expensive_function()', 'profile_stats')

# Analyze saved profile
import pstats
p = pstats.Stats('profile_stats')
p.sort_stats('cumulative').print_stats(10)  # Show top 10 functions by cumulative time
```

### Optimizations
```python
# 1. Use appropriate data structures
# - Lists for ordered data with frequent modifications
# - Tuples for immutable sequences
# - Sets for membership testing, removing duplicates
# - Dictionaries for key-value lookups

# 2. List comprehensions instead of loops
# Slow:
squares = []
for i in range(1000):
    squares.append(i * i)

# Faster:
squares = [i * i for i in range(1000)]

# 3. Generator expressions for large sequences
# Memory efficient:
sum(x * x for x in range(1000000))

# 4. Use built-in functions and libraries
# Slow:
total = 0
for num in numbers:
    total += num

# Faster:
total = sum(numbers)

# 5. Local variables over globals
def func_with_local():
    x = math.cos  # Local reference
    return x(1) + x(2) + x(3)

# 6. String concatenation
# Slow for many items:
result = ""
for i in range(1000):
    result += str(i)

# Faster:
result = "".join(str(i) for i in range(1000))

# 7. Use "in" operator for membership testing
if x in my_list:  # O(n)
    pass

if x in my_set:   # O(1)
    pass

if key in my_dict:  # O(1)
    pass
```

### Common Performance Pitfalls
```python
# 1. Creating copies unnecessarily
# Avoid:
for i in range(len(my_list)):
    item = my_list[i]
    # Process item

# Better:
for item in my_list:
    # Process item

# 2. Inefficient string operations
# Avoid (for many operations):
s = ""
for i in range(1000):
    s += str(i)

# Better:
parts = []
for i in range(1000):
    parts.append(str(i))
s = "".join(parts)

# 3. Repeated method lookups in loops
# Slow:
items = []
for i in range(1000):
    items.append(i)

# Faster:
items = []
append = items.append
for i in range(1000):
    append(i)

# 4. Not using generators for large datasets
# Memory issue:
result = [expensive_computation(x) for x in large_dataset]

# Memory efficient:
result = (expensive_computation(x) for x in large_dataset)
```

## Best Practices and Common Gotchas

### Pythonic Code Style
```python
# PEP 8 - Style Guide for Python Code
# - Use 4 spaces for indentation (not tabs)
# - Line length max 79 characters
# - Use blank lines to separate functions and classes
# - Use docstrings for documentation
# - Use spaces around operators and after commas
# - Use uppercase for constants: MAX_VALUE = 100
# - Use CamelCase for classes: MyClass
# - Use lowercase_with_underscores for functions/variables: my_function

# Naming conventions
# - Variables, functions, methods: lowercase_with_underscores
# - Classes: CamelCase
# - Constants: ALL_CAPS_WITH_UNDERSCORES
# - _name: "private" variables/methods (convention, not enforced)
# - __name: name mangling in classes
# - __name__: special methods
```

### Common Gotchas

#### 1. Mutable Default Arguments
```python
# Problematic: Default list is created once and reused
def add_item(item, items=[]):
    items.append(item)
    return items

# First call: [1]
# Second call: [1, 2] (not [2]!)

# Solution: Use None as default
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

#### 2. Late Binding Closures
```python
# Problem
functions = []
for i in range(5):
    functions.append(lambda: i)  # All functions refer to the same i

# All functions return 4!

# Solution: Capture current value with default argument
functions = []
for i in range(5):
    functions.append(lambda i=i: i)  # Each function gets its own i
```

#### 3. Copy vs. Deepcopy
```python
import copy

original = [[1, 2], [3, 4]]

# Shallow copy (nested objects still reference the same objects)
shallow = copy.copy(original)
shallow[0][0] = 99  # This also affects original[0][0]!

# Deep copy (fully independent copy)
deep = copy.deepcopy(original)
deep[0][0] = 100  # Original remains unchanged
```

#### 4. Truth Value Testing
```python
# These all evaluate to False:
False, None, 0, 0.0, '', [], {}, set(), ()

# All other values are True

# Proper way to check for None
if x is None:  # Use identity, not equality
    pass

# Proper way to check for empty collections
if not my_list:  # Better than len(my_list) == 0
    pass
```

#### 5. Variable Scope
```python
x = 10

def outer():
    # x is the global x
    print(x)  # 10
    
    def inner():
        # Without nonlocal or global, this creates a new local x
        x = 20  # Creates new local x, doesn't affect outer x
        print(x)  # 20
    
    inner()
    print(x)  # Still 10
    
    def inner_nonlocal():
        nonlocal x  # Refers to outer's x
        x = 30
    
    inner_nonlocal()
    print(x)  # Now 30

def global_func():
    global x  # Refers to the global x
    x = 50

global_func()
print(x)  # Now 50
```

#### 6. Context Managers for Resource Management
```python
# Use context managers for resources
with open('file.txt', 'r') as f:
    data = f.read()
# File is automatically closed

# Define your own context manager
class MyResource:
    def __init__(self, name):
        self.name = name
        
    def __enter__(self):
        print(f"Acquiring {self.name}")
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Releasing {self.name}")
        # Return True to suppress exceptions, False to propagate

# Using contextlib
from contextlib import contextmanager

@contextmanager
def my_resource(name):
    print(f"Acquiring {name}")
    try:
        yield name  # This is what gets assigned to the as variable
    finally:
        print(f"Releasing {name}")
```

#### 7. Proper Exception Handling
```python
# Be specific about exceptions
try:
    # Code that might raise exceptions
    file = open('file.txt')
    data = file.read()
    number = int(data)
except FileNotFoundError:
    # Handle missing file
    print("File not found")
except ValueError:
    # Handle invalid data
    print("Invalid data format")
except Exception as e:
    # Catch any other exceptions
    print(f"Unexpected error: {e}")
finally:
    # Clean up resources
    if 'file' in locals():
        file.close()
```