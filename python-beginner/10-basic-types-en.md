# Basic (primitive) data types

---
## Basic (primitive) data types
---

- `int` (integer)
- `float` (floating point number)
- `str` (string): text
- `bool` (boolean): yes / no
- `None` : missing / unknown value

---
## int and float
---
Integers whole numbers (positive or negative) 
4
57
-10

Floating point numbers (real numbers)
3.14
6.1
1.3333
0.0
-1.0

Example
```py
(7 - 3) * 0.5 / 3.5
```

if i do the following

```py
1.0 + 4
```
what do you think the result will be?
and why is the result like this?


Whenever doing math with both floats and ints, the result is a float. Otherwise, 
we would potentially lose any of our data after the decimal point.

---
## order of operations
---

the acronym PEMDAS is a common way to remember the order of operations.
Parentheses, Exponents, Multiplication and Division (same level), and Addition and Subtraction (same level)

the symbols used in python are (from PEMDAS):
- `()` for Parentheses
- `**` for exponentiation
- `*` for multiplication
- `/` for division
- `+` for addition
- `-` for subtraction

and the special one is "modulo" which is the remainder of a division
- `%` for modulo (remainder)


Example:
```py
(7 - 3) * 0.5 / 3.5
```

---
## str
---
A _string_ represents text

Strings can be enclosed in single or double quotes

```py
greeting = "Hello"
name = 'John'
```

---
## Building strings
---

```py
name = "John"
```

Inserting a variable (f-strings):

```py
message1 = f"Hello, {name}!"
```

Joining strings:

```py
message2 = "Hello, " + name + "!"
```

There are several more methods of building strings, but if it was a race. then f-strings have won.

[Real python - string formatting](https://realpython.com/python-string-formatting/)

---
## Strings - escape sequences
---

Problem: how do we include characters like `"` in a string?

this is invalid:

```py
text = "He said: "hi!""
```

solution:

```py
text = "He said: \"hi!\""
```

Python treats the sequence `\"` like a single `"`


Line break: `\n`

```py
a = 'line 1\nline 2'
```

single Backslash: `\\`

```py
b = 'C:\\docs'
```

---
## bool
---
boolean value: yes/no

In Python: `True` or `False`

note the capitalization

---
## None
---
None represents a value that is unknown or missing

```py
first_name = "John"
middle_name = None
last_name = "Doe"
```

---
## Proof of a Primitive Data Type
---
lets say we want to make sure that a variable is of a certain type.
we can use the `isinstance()` function (more on that later in the course for now just know this)
`isinstante()` returns `True` if the variable is of the type you are checking for. and False if it is not

lets say we have a variable called:  what_am_i = 5.0
```py
what_am_i = 5.0
print(isinstance(what_am_i, float))
```
What do you think the will be the output?

Just remember that the function `isinstance()` exists. we are going to use it later. when we learn about control
structures. (if, elif, else, finally)