## Understanding Exceptions and Syntax Errors

Syntax errors occur when the parser detects an incorrect statement. Observe the following example:

```python
>>> print(0 / 0))
  File "<stdin>", line 1
    print(0 / 0))
                ^
SyntaxError: unmatched ')'
```

The arrow indicates where the parser ran into the syntax error. Additionally, 
the error message gives you a hint about what went wrong. 
In this example, there was one bracket too many. Remove it and run your code again:

```python
>>> print(0 / 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

This time, you ran into an exception error. 
This type of error occurs whenever syntactically correct Python code results in an error.
The last line of the message indicates what type of exception error you ran into.


## Raising an Exception in Python
There are scenarios where you might want to stop your program by raising an exception if a condition occurs. 
You can do this with the raise keyword:

```python
number = 10
if number > 5:
    raise Exception(f"The number should not exceed 5. ({number=})")
print(number)
```

In this example, you raised an Exception object and passed it an informative custom message. 

when you run this program you will see this:

```python
Traceback (most recent call last):
  File "./low.py", line 3, in <module>
    raise Exception(f"The number should not exceed 5. ({number=})")
Exception: The number should not exceed 5. (number=10)
```

now the program stops. and offer you a message to what could go wrong.


## Handling Exceptions

Handling Exceptions With the try and except Block

In Python, you use the try and except block to catch and handle exceptions. 
Python executes code following the try statement as a normal part of the program.
The code that follows the except statement is the program’s response to any exceptions in the preceding try clause:


The following function can help you understand the try and except block:
NOTE: if you are on linux, change the name in the line "if "linux" not in sys.platform:" to "windows"

```python
def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing Linux things.")
```

The linux_interaction() can only run on a Linux system. 
Python will raise a RuntimeError exception if you call it on an operating system other then Linux.    


Note: Picking the right exception type can sometimes be tricky. 
Python comes with many built-in exceptions that are hierarchically related, 
so if you browse the documentation, you’re likely to find a fitting one.

https://docs.python.org/3/library/exceptions.html#concrete-exceptions
by hierarchy
https://docs.python.org/3/library/exceptions.html#exception-hierarchy

summarized:

Raise  = Gives a developer to gracefully generate errors in a program if 


You can give the function a try by adding the following code:

```python
try:
    linux_interaction()
except:
    pass
```
if you run the program now. there is no output. as u used the pass.
this is "partly good" because the program doenst crash now!



try and except = Gives you de power to work around exceptions to generate some code around it.

we can use a print statement to give some output:

```python
try:
    linux_interaction()
except:
    print("Linux function wasn't executed.")
```

when an exception in this program occurs now. the program just continues on.
but we didnt get to see what type of error that python raised.
in order to see it we need to capture it.

## Capturing Exceptions
see the following example:

```python
try:
    linux_interaction()
except RuntimeError as error:
    print(error)
    print("The linux_interaction() function wasn't executed.")
```

In the except clause, 
you assign the RuntimeError to the temporary variable error—often also called err—so that you can access the exception 
object in the indented block. In this case, you’re printing the object’s string representation, 
which corresponds to the error message attached to the object.

Running this function on a macOS or Windows machine outputs the following:

```python
Function can only run on Linux systems.
The linux_interaction() function wasn't executed.
```

The first message is the RuntimeError, informing you that Python can only execute the function on a Linux machine. 
The second message tells you which function wasn’t executed

here is another example of opening a file:

```python
try:
    with open("file.log") as file:
        read_data = file.read()
except:
    print("Couldn't open file.log")
If file.log doesn’t exist, then this block of code will output the following:


Couldn't open file.log
```

# note about using bare exceptions

Warning: When you use a bare except clause, 
then Python catches any exception that inherits from Exception—which are most built-in exceptions! 
Catching the parent class, Exception, hides all errors—even those which you didn’t expect at all. 
This is why you should avoid bare except clauses in your Python programs.


```python
try:
    linux_interaction()
    with open("file.log") as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except RuntimeError as error:
    print(error)
    print("Linux linux_interaction() function wasn't executed.")
```

If you run this code on a macOS or Windows machine, then you’ll see the following:

```python
Function can only run on Linux systems.
Linux linux_interaction() function wasn't executed
```

## We will continue at a later time with the more advanced Exception stuff
