# Python Match Case Statement

Introduced in Python 3.10, the **match case** statement offers a powerful mechanism for pattern matching in Python. It allows us to perform more expressive and readable conditional checks. Unlike traditional if-elif-else chains, which can become unwieldy with complex conditions, the match-case statement provides a more elegant and flexible solution.

## Example:

```python
def check_number(x):
    match x:
        case 10:
            print("It's 10")
        case 20:
            print("It's 20")
        case _:
            print("It's neither 10 nor 20")

check_number(10)
check_number(30)
```

**Explanation:**

- In this example, the function `check_number(x)` uses a match-case statement to compare the value of x to the constants 10 and 20.
- If x equals 10, it prints "It's 10". If x equals 20, it prints "It's 20".
- If neither condition is met, the wildcard `_` matches any value, leading to the message "It's neither 10 nor 20".

Let's take a look at python match case statement in detail:

## Table of Contents

- [Python Match Case Statement Syntax](#python-match-case-statement-syntax)
- [Match Case Statements with Constants](#match-case-statements-with-constants)
- [Match Case Statement with OR Operator](#match-case-statement-with-or-operator)
- [Match Case Statement with Python If Condition](#match-case-statement-with-python-if-condition)
- [Match Case Statement on Sequences](#match-case-statement-on-sequences)
- [Match Case Statement on Mappings (Dictionaries)](#match-case-statement-on-mappings-dictionaries)
- [Match Case Statement with Python Class](#match-case-statement-with-python-class)

## Python Match Case Statement Syntax

The match-case syntax is based on structural pattern matching, which enables matching against data structures like sequences, mappings and even classes, providing more granularity and flexibility in handling various conditions. This feature is particularly useful when dealing with different types of data in a clear and organized manner.

```python
match subject:
    case pattern1:
        # Code block if pattern1 matches
    case pattern2:
        # Code block if pattern2 matches
    case _:
        # Default case (wildcard) if no other pattern matches
```

- **match subject:** The value (or variable) to match against.
- **case pattern:** A pattern to match the subject.
- **_ (Wildcard):** A default catch-all pattern, similar to a "default" in other languages' switch statements.

Now, let us see a few examples to know how the match case statement works in Python.

The power of the match-case statement lies in its ability to match a variety of data types, including constants, sequences, mappings and custom classes. Let's explore how to use match-case with different data types.

## Match Case Statements with Constants

Matching constants is one of the simplest uses of the match-case statement. It checks if a variable matches specific constant values and allows for different actions based on the matched constant.

```python
def greet(person):
    match person:
        case "A":
            print("Hello, A!")
        case "B":
            print("Hello, B!")
        case _:
            print("Hello, stranger!")

greet("A")
greet("B")
```

**Explanation:**

- The function `greet(person)` checks the value of person using the match-case statement.
- It specifically matches "A" and "B", printing a personalized greeting.
- If the value of person doesn't match any of the constants, the wildcard `_` matches any value and prints "Hello, stranger!".

## Match Case Statement with OR Operator

The match-case statement can also be used with logical operators like or to combine multiple patterns. This allows for a more flexible matching system where you can group patterns and check for a match against any of them.

**Example:**

```python
def num_check(x):
    match x:
        case 10 | 20 | 30:  # Matches 10, 20, or 30
            print(f"Matched: {x}")
        case _:
            print("No match found")

num_check(10)
num_check(20)
num_check(25)
```

**Explanation:**

- The pattern `10 | 20 | 30` uses the or operator to match any of these three values. If x equals 10, 20 or 30, the case will execute.
- If x doesn't match any of the values, the wildcard `_` catches it and prints "No match found".

## Match Case Statement with Python If Condition

We can also add an if condition after a case to create more granular control over the matching process. This allows us to add additional checks within a case.

**Example:**

```python
def num_check(x):
    match x:
        case 10 if x % 2 == 0:  # Match 10 only if it's even
            print("Matched 10 and it's even!")
        case 10:
            print("Matched 10, but it's not even.")
        case _:
            print("No match found")

num_check(10)
num_check(15)
```

**Explanation:**

- The first case matches 10 but only if `x % 2 == 0`. If this condition is met, it prints a specific message.
- The second case matches 10 without the condition, ensuring that a fallback message is shown if the first case isn't executed.

## Match Case Statement on Sequences

The match-case statement is particularly powerful when working with sequences such as lists or tuples. We can match individual elements of a sequence or even match the structure of the sequence itself.

**Example:**

```python
def process(data):
    match data:
        case [x, y]:  
            # A list with two elements
            print(f"Two-element list: {x}, {y}")
        case [x, y, z]:  
            # A list with three elements
            print(f"Three-element list: {x}, {y}, {z}")
        case _:
            print("Unknown data format")

process([1, 2])
process([1, 2, 3])
process([1, 2, 3, 4])
```

**Explanation:**

- The function `process(data)` matches the structure of the list data.
- The first case matches if the list has exactly two elements, binding the first and second elements to x and y respectively.
- The second case matches if the list has exactly three elements, binding them to x, y and z.
- If the list does not match either pattern, the wildcard `_` is used to print "Unknown data format".

## Match Case Statement on Mappings (Dictionaries)

A mapping is another common data type in Python and match-case can be used to match against dictionaries, checking for specific keys and values.

```python
def person(person):
    match person:
        # Dictionary with name and age keys
        case {"name": name, "age": age}:  
            print(f"Name: {name}, Age: {age}")
        # Dictionary with only name key    
        case {"name": name}:  
            print(f"Name: {name}")
        case _:
            print("Unknown format")

person({"name": "Alice", "age": 25})
person({"name": "Bob"})
person({"city": "New York"})
```

**Explanation:**

- The function `person(person)` matches the structure of a dictionary person.
- The first case matches a dictionary that contains both "name" and "age" keys, binding their corresponding values to the variables name and age.
- The second case matches a dictionary with just the "name" key.
- The wildcard `_` is used to catch any other dictionary structure that doesn't match these patterns, printing "Unknown format".

## Match Case Statement with Python Class

One of the most powerful features of match-case is the ability to match against classes. We can match instances of a class and even extract specific attributes of an object for further handling.

**Example:**

```python
class Shape:
    pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

def check_shape(shape):
    match shape:
        # Match Circle and extract the radius
        case Circle(radius):  
            print(f"circle radius {radius}.")
        # Match Rectangle and extract width and height
        case Rectangle(width, height):  
            print(f"Rectangle width {width} and height {height}.")
        # Default case for any other object
        case _:  
            print("This is an unknown shape.")

# Create objects of Circle and Rectangle
circle = Circle(10)
rectangle = Rectangle(4, 6)

# Test with different shapes
check_shape(circle)     
check_shape(rectangle)  
```

**Explanation:**

- We have a Shape class and two types of shapes: Circle and Rectangle.
- The `check_shape` function checks if the shape is a Circle or Rectangle and prints their details.
- If the shape isn't one of these, it says "unknown shape."