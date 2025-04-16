## Demystifying Functions in Python

### What are functions?

The best way to summarize a function is a
- self-contained block of code comprised of related statements used to accomplish a specific task or related group of tasks.
- encapsulates a specific task or related group of tasks.
- in some languages also called a `subprogram`

We use functions for a number of reasons
- code reusability
- code organization
- modularity

Within Python, these functions exist as one of three types
- built-in functions
- user-defined functions
- Lambda functions (also known as anonymous functions)


We will discuss these 3 types of functions in more detail below..
But beofre all of that, It's necessary to ask the big question.


### Why use functions.

Python functions are reusable code blocks that carry out particular tasks, 
helping programmers structure their code and make it easier to read. 
By preventing duplication, functions make the code more modular and manageable. 
The `def` keyword, the function name, and any parameters included in parenthesis define a function. 
The code to be performed is contained in the function body, and the 'return' statement allows the function to produce a result.

I like to think of functions as: avoiding replicating code everywhere. 
so that i can test functionality in one place and use it everywhere.

not repeating yourself is a good thing in programming.
They have also created a term for that.

- DRY - Don't Repeat Yourself

---

When we started coding in Python we used the Python build in `print()` function. and often the `input()` function.

In programming, this is called `abstraction`.
It lets you use functions by "calling" the function with required arguments.

# example
```python
print()  # <--- this is the function

print("hello")   # <---- what we put in the function is an argument!!!
```

We have already seen several more "built-in" functions in Python.
- `len()`
- `type()`
- `int()`
- `str()`
- `float()`
- `bool()`
- `list()`
- `dict()`
- `set()`
- `tuple()`
- `range()`
- `input()`

etc etc you can find em all in The python documentation.

[Built in Python functions](https://docs.python.org/3/library/functions.html)

## Creating functions in python

The syntax looks like this

```python
def function_name(parameters):
    # What the function does goes here
    return result
```

or formally

```python
def <function_name>(<parameters>):
    <statement(s)>
```

- <function_name> is the name of the function ex: `print_hello`
- <parameters> is the input the function takes ex: `name`  (could be even more, comma separated)
- The `:` at the end. Punctuaction that denotes the end of the Python function definiton
- <statement(s)> is the code block that does the work of the function

functions are derived from the world of mathematics.

![math functions](img/function.avif)

Here f is function that operates on the inputs x and y to produce the output z.
However programming functions are more generalized and versatile then the mathematical definition.

Lets go pack and use the function `len` as an example.
The function len, takes one input. (how do i know this?) 
if using pycharm type `len()` and mouseover and it will tell you.

otherwise the python documentation!! (this is going to be one of your friends as a Python programmer)

# Example
we define a list and then use the `len()` function to get the length of the list.
```python
a = ['foo', 'bar', 'baz', 'qux']
print(len(a))
```
the result of this will be 4.

So we used the function `len()` and we passed the parameter a to the function.
The function does its work and returns the result. in this case `4`

In earlier exercises for example. we used the module random to generate random numbers.

```python
import random
a = random.randint(1, 10)
```

randint here. 
- is a function that takes 2 parameters. and returns a random number between those 2 numbers.
- randint is a function that is part of the random module.
- randint is a method of the object random.

so we see. we use many different names for essentially the same thing.

In Pycharm i can hop trough the code by pressing `ctrl` and clicking on the function name.
Altough this can be a bit of a "rabbit hole" ill demonstrate with images below.
when i do that on `randint(1, 10)` ill be taken to the source code of the function.

![first click trough](img/randint-click1.png)

i then ctrl click on `_inst.randint` and i get to implementation.

![second clicktrough](img/randint-click2.png)

we see here that the "method" randint which is a function is defined here.
as a function

```python
    def randint(self, a, b):
        """Return random integer in range [a, b], including both end points.
        """

        return self.randrange(a, b+1)
```

Thats why in this course i keep repeating the following mantra

# Everything in Python is an object.
# An object can have methods.
# a method is a function that is part of an object.
# and a method is just a function

---


## Modularity

Functions allow complex processes to be broken up into smaller, more manageable parts.

we will use the example of opening a file (we havent learned to open files yet but follow along)
we need to
- read a file
- process the contents of the file
- write an output file.

in how we learned python up until now we would structure that something like this.

```python
# Main program

# Code to read file in
<statement>
<statement>
<statement>
<statement>

# Code to process file
<statement>
<statement>
<statement>
<statement>

# Code to write file out
<statement>
<statement>
<statement>
<statement>
```

We call this: emerging programming. or scripting.
it is just a bunch of code strung together in a long sequence,
usually with whitespace and comments to help organize it a bit.
however this will get lengthy and hard to read and maintain.

with function we would structure it something like this.

```python
def read_file():
    # Code to read file in
    <statement>
    <statement>
    <statement>
    <statement>

def process_file():
    # Code to process file
    <statement>
    <statement>
    <statement>
    <statement>

def write_file():
    # Code to write file out
    <statement>
    <statement>
    <statement>
    <statement>


# Main program
read_file()   # we call it just like the built in functions.
process_file()
write_file()
```

This example is **modularized**
instead of all strung together in a long sequence.
it's broken out into seperate function, each of which focuses on a specific task.

in our example those tasks are:
- read a file
- process the contents of the file
- write an output file.


a mental exercise for this is how we do things in real life.
1. Take all the stuff off the shelves.
2. Take the shelves apart.
3. Carry the shelf parts across the garage to the new location.
4. Re-assemble the shelves.
5. Carry the stuff across the garage.
6. Put the stuff back on the shelves.

Breaking a large task into smaller tasks makes it easier to manage and understand.
just like in real life no one will ask you to move the entire garage in one go.

The bigger a program gets, the more important it is to break it down into smaller, more manageable parts.


### Let's make our first function!

using the syntax we had earlier

```python
def function_name(parameters):
    # What the function does goes here
    return result
```

lets break it down once more:
1. `def` is the keyword that tells Python we are defining a function.
2. `function_name` is the name of the function. (you can name it anything you want)
3. `parameters` are the values the function takes as input. (you can have multiple parameters)
4. `:` is the punctuation that denotes the end of the Python function definition.
5. The code block that does the work of the function is indented.
6. `return` is the keyword that tells Python what to return as the result of the function. (optional)


we create a function in Python that greets the user

```python
def my_func():
    print("Hello! Hope you're doing well")

my_func()
```
As you can see, the function `my_func()`
- has no parameters
- returns no value
- prints a greeting message to the console

This is a bit sneaky cause the function returns nothing. but still prints to the console.
This is due how print() is implemented. every other thing needs something returned.

we could have done this.

```python
def my_func():
  return "Hello! Hope you're doing well"

print(my_func())
```

what happens here is following
- the function `my_func()` is called
- executed
- and the result of `my_func()` is: "Hello! Hope you're doing well"
- so it has become a object string.
- we then print the result of the function.


Lets say we want to make a function that takes arguments

```python
def my_func(name, place):
  return(f"Hello {name}! Are you from {place}?")

print(my_func("John", "New York"))
```
Here we defined a function `my_func` that has 2 parameters `name` and `place`.
naming the paremeters is important as it shows intent to another program of what is going on.



We can `call` our function with 2 arguments. (arguments is what we pass to function)
in the function the variable
- name is "John"
- place is "New York"
- 
and the rest of the code will work with those variables.

the result would be
- `Hello John! Are you from New York?`

What happens if we swap "John" and "New York" in the function call?
we would get.

- `Hello New York! Are you from John?`

is that perse wrong? no not really. but it is not what we intended as programmer.
however the function happily takes the arguments and returns the result.

we call these arguments also `positional arguments` cause they are in the position of the parameters.

## still following it?
## let me repeat 

- arguments is what you `feed` or `pass` to the function.
- parameters are what the function `expects` or `receives`.
- arguments are positional. so the first argument is the first parameter.

we also have `keyword arguments` which are a bit more flexible. and can have "default" values

```python
def my_func(place="Hawaii",name="Robert"):
    return(f"Hello {name}! Are you from {place}?")

```
# Output
Hello Robert! Are you from Hawaii?


no i can call the function with arguments and it will use these values instead of the defaults

```python
def my_func(place="Hawaii",name="Robert"):
    return(f"Hello {name}! Are you from {place}?")

print(my_func("New York", "John"))
```

we also could have done this.

```python
def my_func(place="Hawaii",name="Robert"):
    return(f"Hello {name}! Are you from {place}?")

print(my_func(name="John", place="New York"))
```

completely the same result. but the second one is a bit more readable. and explicit.
everyone can see what is going on. and what will be passed to which variable in the function.

There is note about this.

- positional arguments must come before keyword arguments. !!!!!   mega important.

so you cant do this

```python
def my_func(name="Robert", place):
    return(f"Hello {name}! Are you from {place}?")

print(my_func(name="John", New York))

  File "<input>", line 1
    def my_func(name="Robert", place):
                               ^^^^^
SyntaxError: parameter without a default follows parameter with a default
```

## Return Values and Variables

### Return Statement in Detail
The `return` statement allows a function to send a result back to the caller. Without it, functions return `None` by default.

```python
def add(a, b):
    return a + b  # Returns the sum to the caller

result = add(5, 3)  # result = 8
```

### Multiple Return Values
Python functions can return multiple values using tuples:

```python
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)  # Returns a tuple

minimum, maximum, average = stats([1, 2, 3, 4, 5])  # Unpacking the tuple
print(f"Min: {minimum}, Max: {maximum}, Avg: {average}")
```

### Variable Scope
Variables defined inside a function have local scope - they only exist within the function:

```python
def my_function():
    local_var = "I only exist inside the function"
    print(local_var)

my_function()
# print(local_var)  # This would cause an error

# Using global variables
counter = 0  # Global variable

def increment():
    global counter  # Use the global keyword to modify global variables
    counter += 1
    return counter
```

## Lambda Functions

Lambda functions are small, anonymous functions defined with the `lambda` keyword:

```python
# Regular function
def double(x):
    return x * 2

# Equivalent lambda function
double_lambda = lambda x: x * 2

print(double(5))        # 10
print(double_lambda(5)) # 10
```

### Common Use Cases

1. **With sorting functions:**
```python
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
# Sort by score (second element of each tuple)
students.sort(key=lambda student: student[1], reverse=True)
```

2. **With filter and map:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squared = list(map(lambda x: x**2, numbers))
```

### Limitations
Lambda functions are restricted to a single expression and cannot contain multiple statements or complex logic.

## Function Documentation

### Docstrings
Docstrings document what a function does, making your code more maintainable:

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
        
    Returns:
        float: The area of the rectangle
    """
    return length * width
```

### Accessing Documentation
You can access docstrings using the `help()` function:

```python
help(calculate_area)
```


## Axiros functions
Below when you open a script in axiros.
the whole script is a function.
at the top you see a bar parameters. and that is just the same as making a normal function in python.
![axiros_function](img/axiros_function.png)


## Best Practices

### Function Naming
- Use lowercase with underscores (`calculate_total`, not `CalculateTotal`)
- Choose descriptive names that indicate what the function does
- Verb phrases are common for functions that perform actions

### Function Length
- Keep functions focused on a single task
- If a function is too long (over 20-30 lines), consider breaking it into smaller functions
- Remember: A function should do one thing and do it well

### Single Responsibility Principle
Each function should have a single, well-defined purpose:

```python
# Bad: Function does too many different things
def process_data(data):
    # Clean the data
    # Analyze the data
    # Generate a report
    # Save results to a file
    pass

# Better: Separate functions with clear purposes
def clean_data(data):
    return cleaned_data

def analyze_data(cleaned_data):
    return analysis_results

def generate_report(analysis_results):
    return report

def save_results(report, filename):
    # Save to file
    pass
```

### Testing Functions
Write functions that are easy to test:
- Avoid side effects (changing global state)
- Return values rather than printing them
- Keep input/output relationships clear and predictable

```python
# Hard to test (uses global variable, prints instead of returning)
total_sum = 0
def add_to_total(num):
    global total_sum
    total_sum += num
    print(f"Total is now {total_sum}")

# Easy to test (pure function, returns result)
def add_numbers(a, b):
    return a + b
```

## *args and **kwargs

### *args: Variable Positional Arguments
The `*args` parameter allows a function to accept any number of positional arguments:

```python
def sum_all(*args):
    """Accept any number of positional arguments and return their sum."""
    return sum(args)

print(sum_all(1, 2))          # 3
print(sum_all(1, 2, 3, 4, 5)) # 15
```

Here, `*args` collects all positional arguments into a tuple.

### **kwargs: Variable Keyword Arguments
The `**kwargs` parameter allows a function to accept any number of keyword arguments:

```python
def print_info(**kwargs):
    """Accept any number of keyword arguments and print them."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, job="Developer")
# Output:
# name: Alice
# age: 25
# job: Developer
```

Here, `**kwargs` collects all keyword arguments into a dictionary.

### Combining Regular Parameters with *args and **kwargs
You can use regular parameters, `*args`, and `**kwargs` together:

```python
def example_function(regular_param, *args, default_param="default", **kwargs):
    print(f"Regular parameter: {regular_param}")
    print(f"Args: {args}")
    print(f"Default parameter: {default_param}")
    print(f"Kwargs: {kwargs}")

example_function("required", 1, 2, 3, default_param="custom", x=10, y=20)
# Output:
# Regular parameter: required
# Args: (1, 2, 3)
# Default parameter: custom
# Kwargs: {'x': 10, 'y': 20}
```

### Passing Args and Kwargs
You can also use the `*` and `**` syntax to unpack sequences and dictionaries when calling functions:

```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))  # Unpacks the list into separate arguments: add(1, 2, 3)

params = {"a": 1, "b": 2, "c": 3}
print(add(**params))  # Unpacks the dictionary into keyword arguments: add(a=1, b=2, c=3)
```

Remember the parameter order: regular parameters, then `*args`, then default parameters, then `**kwargs`.
