# Basic (primitive) data types

## Basic (primitive) data types

- `int` (integer)
- `float` (floating point number)
- `str` (string): text
- `bool` (boolean): yes / no
- `None` : missing / unknown value

## int and float

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

## int and float pt2
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

## int and float pt 3
Whenever doing math with both floats and ints, the result is a float. Otherwise, 
we would potentially lose any of our data after the decimal point.

## order of operations

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

## order of operations pt2
Example:
```py
(7 - 3) * 0.5 / 3.5
```

## str

A _string_ represents text

Strings can be enclosed in single or double quotes

```py
greeting = "Hello"
name = 'John'
```

## Building strings

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

## Strings - escape sequences

Problem: how do we include characters like `"` in a string?

this is invalid:

```py
text = "He said: "hi!""
```

## Strings - escape sequences

solution:

```py
text = "He said: \"hi!\""
```

Python treats the sequence `\"` like a single `"`

## Strings - escape sequences

Line break: `\n`

```py
a = 'line 1\nline 2'
```

single Backslash: `\\`

```py
b = 'C:\\docs'
```

## bool

boolean value: yes/no

In Python: `True` or `False`

note the capitalization

## None

None represents a value that is unknown or missing

```py
first_name = "John"
middle_name = None
last_name = "Doe"
```
