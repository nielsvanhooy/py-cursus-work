## working with files

In the previous lesson we learned to work with file paths.
thats good. because we can use that knowledge to work with files.

### Reading files 

Reading files is a fundamental operatin in many python programs. (and also in our company)
`pathlib` provides convenient shorthand methods for reading files as eiter text or raw bytes.

Example:

```python
from pathlib import Path

file = Path("file.txt")

print(file.read_text())
```
This is a sample text


for binary files we use the `read_bytes()` method.

```python
from pathlib import Path
image = Path("images/midjourney.png")

image.read_bytes()[:10]  # Display the first 10 bytes
```

Writing with pathlib is also easy. We can use the `write_text()` and `write_bytes()` methods.

```python
from pathlib import Path
file = Path("file.txt")

file.write_text("This is new text.")
```
the thing with write_text is that it will overwrite the file if it already exists. 
now you can use python tricks ofcourse. first read the file.
then append to the string. and write it back to the file.

```python
from pathlib import Path

file = Path("file.txt")

old_text = file.read_text() + "\n"
final_text = "This is the final text."

# Combine old and new texts and write them back
file.write_text(old_text + final_text)

print(file.read_text())
```
write bytes works the same way. 


Even if Pathlib is a modern method i dont see many people using it.
Therefor we shall learn the ways of working with reading and writing files with the `open()` function.

## working with files (the common way)

The `open()` function is the most common way to read and write files in Python.
It takes two arguments: the file path and the mode.

we can give the file path either as a string or as a `Path` object.
the second argument is the mode we open a file in.

here are all the available modes to open a file in:

```markdown
| Mode | Description |
|------|-------------|
| 'r' | Open text file for reading. Raises an I/O error if the file does not exist. |
| 'r+' | Open the file for reading and writing. Raises an I/O error if the file does not exist. |
| 'w' | Open the file for writing. Truncates the file if it already exists. Creates a new file if it does not exist. |
| 'w+' | Open the file for reading and writing. Truncates the file if it already exists. Creates a new file if it does not exist. |
| 'a' | Open the file for writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist. |
| 'a+' | Open the file for reading and writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist. |
| 'rb' | Open the file for reading in binary format. Raises an I/O error if the file does not exist. |
| 'rb+' | Open the file for reading and writing in binary format. Raises an I/O error if the file does not exist. |
| 'wb' | Open the file for writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist. |
| 'wb+' | Open the file for reading and writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist. |
| 'ab' | Open the file for appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist. |
| 'ab+' | Open the file for reading and appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist. |
```

```python
f = open('zen_of_python.txt', 'r') 
print(f.read())
f.close()

# prints
    # The Zen of Python, by Tim Peters
    # 
    # Beautiful is better than ugly.
    # Explicit is better than implicit.
    # Simple is better than complex.
    # Complex is better than complicated.
    # Flat is better than nested.
    # Sparse is better than dense.
    # Readability counts.
    # Special cases aren't special enough to break the rules.
    # Although practicality beats purity.
    # Errors should never pass silently.
    # Unless explicitly silenced.
    # In the face of ambiguity, refuse the temptation to guess.
    # There should be one-- and preferably only one --obvious way to do it.
    # Although that way may not be obvious at first unless you're Dutch.
    # Now is better than never.
    # Although never is often better than *right* now.
    # If the implementation is hard to explain, it's a bad idea.
    # If the implementation is easy to explain, it may be a good idea.
    # Namespaces are one honking great idea -- let's do more of those!

```
here we gave the file path as a common string.
but we could have given it a `Path` object as well.
and we chose the mode `r` to read the file.

## problems that happen with open()

One common problem you’ll face in programming is how to properly manage external resources, 
such as files, locks, and network connections. 

Sometimes, a program will retain those resources forever, even if you no longer need them. 

This kind of issue is called a memory leak because the available memory gets reduced every time you create and open a new instance of a given resource without closing an existing one.

Managing resources properly is often a tricky problem. It requires both a setup phase and a teardown phase. 
The latter phase requires you to perform some cleanup actions, such as closing a file, releasing a lock, or closing a network connection.

This can happen with databases, files, network connections and with working with files.

```python
file = open("hello.txt", "w")
file.write("Hello, World!")
file.close()
```

in the example the `open()` function opens the text file in reading mode,
allowing us to grab the information from the file without making changes to it.
we then use the `read()` method to read the file.

the problem with opening a file like this is that we have to remember to close it.
if we forget to close the file or the program crashes, it can cause memory leaks and other issues.
and leaves open processes on the system.


you could use a try... except... finally clause. to "teardown" the resource if an error occurs.

```python
# Safely open the file
file = open("hello.txt", "w")

try:
    file.write("Hello, World!")
finally:
    # Make sure to close the file after using it
    file.close()
```
In this example, you need to safely open the file hello.txt, which you can do by wrapping the call to open() in a try … except statement. 
Later, when you try to write to file, the finally clause will guarantee that file is properly closed, even if an exception occurs during the call to .write() in the try clause. 
You can use this pattern to handle setup and teardown logic when you’re managing external resources in Python.




to prevent this. the very smart people at python have created the `with` statement.

```python
with open('zen_of_python.txt') as f:
    print(f.read())
print("i have closed the file handle")
```

what this syntax does is that it automatically closes the file when the block of code is done.
you should always use the with statement when working with files, sockets, and other resources that need to be closed.

in the example as soon as it leaves the block of code the file is closed.

in this syntax open('zen_of_python.txt') as f is the same as f = open('zen_of_python.txt') 
but with the added benefit of closing the file when the block is done.

working with the file can only be done in this block of code. but we can assign the content to a variable.
so that we can use it a later point in the code.



## deeper into context managers:

The Python with statement creates a runtime context that allows you to run a group of statements under the control of a context manager. 
This is described in the python document: PEP 343 . 
This added the with statement to make it possible to factor out standard use cases of the try … finally statement.

Compared to traditional try … finally constructs, the with statement can make your code clearer, safer, and reusable. 
Many classes in the standard library support the with statement. 
A classic example of this is open(), which allows you to work with file objects using with.


To write a with statement, you need to use the following general syntax:

```python
with expression as target_var:
    do_something(target_var)
```
The context manager object results from evaluating the expression after with. In other words,
expression must return an object that implements the context management protocol. 
This protocol consists of two special methods:

.__enter__() is called by the with statement to enter the runtime context. (this is function that implements the opening of a resource)
.__exit__() is called when the execution leaves the with code block. (this is a function that implements the closing of a resource)

we will not go into this as this is very advanced python.

# combining with statements.

In Python 3.1 and later, the with statement supports multiple context managers. You can supply any number of context managers separated by commas:

with A() as a, B() as b:
    pass

This works like nested with statements but without nesting. This might be useful when you need to open two files at a time, the first for reading and the second for writing:

```python
with open("input.txt") as in_file, open("output.txt", "w") as out_file:
    # Read content from input.txt
    content = in_file.read()
    # Transform the content
    transformed_content = content.upper()  # Example transformation
    # Write the transformed content to output.txt
    out_file.write(transformed_content)
    pass
```

## most used file methods. 

all the methods that can be performed on a file object are:
and with this i mean on the `f` variable above.

but there are many more file methods we can use.

| Method | Description |
|--------|-------------|
| close() | Closes the file |
| detach() | Returns the separated raw stream from the buffer |
| fileno() | Returns a number that represents the stream, from the operating system's perspective |
| flush() | Flushes the internal buffer |
| isatty() | Returns whether the file stream is interactive or not |
| read() | Returns the file content |
| readable() | Returns whether the file stream can be read or not |
| readline() | Returns one line from the file |
| readlines() | Returns a list of lines from the file |
| seek() | Change the file position |
| seekable() | Returns whether the file allows us to change the file position |
| tell() | Returns the current file position |
| truncate() | Resizes the file to a specified size |
| writable() | Returns whether the file can be written to or not |
| write() | Writes the specified string to the file |
| writelines() | Writes a list of strings to the file |












