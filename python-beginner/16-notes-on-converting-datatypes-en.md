## Converting from a type. to another type

A short chapter because there is not allot to explain about this.

in python we are able to change the type of a variable to another type.

There are 2 types of conversions (also called `Casting`:

- Implicit Casting
- Explicit Casting


### Implicit Casting

```python
a = 10   # integer
b = 10.5 # float

c = a + b
print(c) # 20.5 <---- now a float. 
```
In the above example when adding a + b together. 
the type from a is automatically converted to a float. because the result of the sum is a float.

This is called Implicit Casting.

Implicit Casting is only limited to `int` and `float` types.

### Explicit Casting

To explicitly convert a variable from one type to another, 
you can use the built-in functions `int()`, `float()`, `str()`, `bool()`, and `list()`.

### int

Python's built-in int() function converts an integer literal to 
- an integer object
- a float to integer
- and a string to integer if the string itself has a valid integer literal representation.

```python
a = int(10)  # Using int() with an int object as argument is equivalent to declaring an int object directly.
b = int(10.5)  # 10   <---- 10.5 is converted to 10. it is not rounded down. it is just cut off.
c = int(True) # results in 1. cause in machine language 1 is True and 0 is False
d = int(False) # results in 0. cause in machine language 1 is True and 0 is False
```
You can also turn strings into int. but only if the string is a number.


```python
a = int("10")  # 10
```

If the string is not a number you will get an error.

```python
a = int("10.5")

Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '10.5'


a = int("Hello World")

Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'Hello World'
```

There a also ways to convert 
- `binary string` to `int` 
- `hexadecimal string` to `int`.
- `octal string` to `int`.

Examples

```python
a = int("110011", 2) # 51     Binary
b = int("20", 8)     # 16     Octal
c = int("2A9", 16)   # 681    Hexadecimal
```
Decimal equivalent of Hexadecimal 2A9 is 681. 
You can easily verify these conversions with calculator app in Windows, Ubuntu or Smartphones.

### float

The float() is a built-in function in Python. 
It returns a float object if the argument is a float literal, 
integer or a string with valid floating point representation.

```python
a = float(9.99)   # Using float() with a float object as argument is equivalent to declaring a float object directly.
b = 9.99          # 9.99 is a float literal  so the type is a float
c = float(100)    # 100.0
d = float("9.99") # 9.99
```

what if the string is not a number? for example the string `99,99` (with a comma) instead of `9.99` (with a dot)

```python
a = float("1,234.50")

Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: '1,234.50'
```


### string

We saw how a Python obtains integer or float number from corresponding string representation. 
The str() function works the opposite. 
It surrounds an integer or a float object with quotes (') to return a str object. 
The str() function returns the string representation of any Python object. 

```python
a = str(10)   # '10'
b = str(11.10) # '11.1'
c = str(True)  # 'True'
```
nothing more to say about it. it just wraps everything in quotes to make it a string.


### conversion of sequence Types

List, Tuple and String are Python's sequence types. They are ordered or indexed collection of items.
A string and tuple can be converted into a list object by using the list() function. Similarly, the tuple() function converts a string or list to a tuple.
We shall take an object each of these three sequence types and study their inter-conversion.

```python
a =[1,2,3,4,5]   # List Object
b =(1,2,3,4,5)   # Tupple Object
c ="Hello"       # String Object

### list() separates each character in the string and builds the list
obj =list(c)

['H', 'e', 'l', 'l', 'o']

### The parentheses of tuple are replaced by square brackets
obj=list(b)

[1, 2, 3, 4, 5]

### tuple() separates each character from string and builds a tuple of characters
obj=tuple(c)

('H', 'e', 'l', 'l', 'o')

### square brackets of list are replaced by parentheses.
obj=tuple(a)
(1, 2, 3, 4, 5)

### str() function puts the list and tuple inside the quote symbols.
obj=str(a)

'[1, 2, 3, 4, 5]'

obj=str(b)

'(1, 2, 3, 4, 5)'
```

### Data Type Conversion Functions
There are several built-in functions to perform conversion from one data type to another. 
These functions return a new object representing the converted value.


| Sr. No. | Function & Description |
|---------|------------------------|
| 1 | **Python int() function** <br> Converts x to an integer. base specifies the base if x is a string. |
| 2 | **Python long() function** <br> Converts x to a long integer. base specifies the base if x is a string. |
| 3 | **Python float() function** <br> Converts x to a floating-point number. |
| 4 | **Python complex() function** <br> Creates a complex number. |
| 5 | **Python str() function** <br> Converts object x to a string representation. |
| 6 | **Python repr() function** <br> Converts object x to an expression string. |
| 7 | **Python eval() function** <br> Evaluates a string and returns an object. |
| 8 | **Python tuple() function** <br> Converts s to a tuple. |
| 9 | **Python list() function** <br> Converts s to a list. |
| 10 | **Python set() function** <br> Converts s to a set. |
| 11 | **Python dict() function** <br> Creates a dictionary. d must be a sequence of (key,value) tuples. |
| 12 | **Python frozenset() function** <br> Converts s to a frozen set. |
| 13 | **Python chr() function** <br> Converts an integer to a character. |
| 14 | **Python unichr() function** <br> Converts an integer to a Unicode character. |
| 15 | **Python ord() function** <br> Converts a single character to its integer value. |
| 16 | **Python hex() function** <br> Converts an integer to a hexadecimal string. |
| 17 | **Python oct() function** <br> Converts an integer to an octal string. |