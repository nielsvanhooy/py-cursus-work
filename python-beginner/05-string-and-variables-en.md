# Printing, Variables


# Printing in python.

We begin our python journey with a command that most of you already now.

**the print function.**

We will use the  `print()` function.
you can use it to display formatted messages onto the screen and perhaps find some bugs

The classic "my first program" in Python:
```py
print("Hello World")
```
what you may notice is that print gets another (syntax highlighting) color in Pycharm.
**Why is that??**

<details>
    <summary>Click to reveal more</summary>
<p>
This is because it is a built-in function in python. 
And functions always start with a word. followed bij parantheses ()  <---- (more on functions later in the course)
</p>
</details>



Create a new file in pycharm
Type the following in pycharm (dont run it yet)

```py
print("Hello World)
```
What do you notice (hint. check the colors in pycharms) (not perse on the web document i show you).
The squiggly red line means there is a syntax error. 
This can be a cause of many. but in this case it is because we forgot to close the string with a double quote.
You can also see this when you mouse over in pycharm. it will give you a hint.

Now run the code. There are several ways to do this

- press the green play button in the top right corner (make sure in the dropdown it is on current file)
- right click in the editor and press run

```py
  File "/Users/nielsvanhooij/git/python_cursus_exercises/1/printing/exercise_one.py", line 1
    print("Hello world)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

SyntaxError: Unterminated string literal it says. ok thats nice. but what does it mean?

<details>
    <summary>Click to reveal more</summary>
<p>
A string literal is just an oldschool programmer word (from ancient programming languages).
that says: "a string that is not closed properly"

will that help us solve this??.
The MEGA hint here is in the SyntaxError. this is generated because it does not follow the rules that python wants
</p>
</details>

Lets do Exercise 1 now. (from the git.kpn repo that we downloaded earlier.)


## A note on "newline character"

A newline character is a special control character used to indicate the end of a line (EOL). 
It usually doesn’t have a visible representation on the screen, 
but some text editors can display such non-printable characters with little graphics.

A newline character is also dictated by your operating system.
- Windows: \r\n
- Unix/Linux/Modern MACos: \n

we can verify this on our own system like this (start a python console)
- trough typing python in the command prompt
- trough clicking the python logo in pycharm (bottom left) uppermost logo

and type in the following

```py
import os
os.linesep
```

it should spit out your linesep per your operating system.

To make software portable we have to take this in consideration (Does it ring a bell with our CPE configurations?)


## Printing Strings

with the information we learned earlier we can now do more things when printing.
for example my linesep is \n

```py
print("Hello\nWorld")
```

What do you expect to happen?
Why is there an extra newline?

<details>
    <summary>Click to reveal more</summary>
<p>
print() always adds a newline at the end of the string.
</p>
</details>


## Combining strings

we can also combine strings by using the + symbol.

How would this work do you think?

<details>
    <summary>Click to reveal more</summary>
<p>
Example
```py
print("Hello" + "World")
```
</p>
</details>

What would the result look like? is that what you expected?

## Input and output of text
We can get user input for our program by using the `input()` function.


```py
input("What is your name?")
```

`input` will always return a string

How would we combine this with the print statement to make a greeting?

For Example as result:
```py
Hello Niels
```
(think about printing, and combining strings.)

use scratchfiles -> 1 - > scratchfile_1.py to play around with this.

And how would i get it with an ! at the end?

For Example as result:
```py
Hello Niels!
```

Solutions:
<details>
    <summary>Click to reveal more</summary>
<p>
1:
```py
print("Hello " + input("What is your name?"))
```

2:
```py
print("Hello " + input("What is your name?") + "!")
```
</p>
</details>

One of the most usefull skills as a programmer is to be able to google.
If you are stuck on something. try to google it.

Exercise!: How do i get the length of a string in python?. 
(use google) and combine your knew knowledge with the input function.
---

As you can see the code is starting to get "Muddy" with all the different strings and plusses and syntax.
On to the world of Variables!

## Variables

Variables are containers for storing data values.

```py
birth_year = 1970
current_year = 2020
age = current_year - birth_year
```

This doenst mean it that it can only be **"primitive"** types like **integers/strings/floats/booleans**(more on that later).
But "functions" or the result of "functions" can also be stored in variables. (like `print()` and `input()`)
```py
name = input("What is your name?")
```

Names of variables are usually written in lower case, separating words by underscores
**Variable names may only consist of letters, digits and underscores**

## Variables

Overwriting (reassigning) variables example 1:

```py
name = "John"
name = "Jane"
a = 3
a = a + 1
```

example 2:

we "Reassign" the variables. 

```py
greeting = "Hello"
farewell_greeting = "Goodbye"

farewell_greeting, greeting = greeting, farewell_greeting
```

how would we print the variables now?
why does print(farewell_greeting) print "Hello" and not "Goodbye"?
why does print() take variables? and not just strings?

## Conventions

PEP-8 guidelines for naming variables in Python: Use lowercase letters for variable names , 
with words separated by underscores (snake_case). 
Variables names follow the same conventions as for functions in python

[Python Official Style Guide](https://peps.python.org/pep-0008/)


```py
NIELS_BIRTH_YEAR = 1987  # we call this a CONSTANT. because my birth year will never change
_current_year = 2025     # we call this a PRIVATE variable. it is not enforced by the language, but it is a convention for data the developer doenst want touched.
NIELS_BIRTH_YEAR_1987 = "1987" # we dont use numbers in variable names. this is a bad example.
```

## Exercise: Variable naming

What would be a good name for the variable below

- p1_user_name = "jackbauer"
- 1_player_username = "jackbauer"
- player_one_username = "jackbauer"
- p1u = "jackbauer"


<details>
    <summary>Click to reveal more</summary>
<p>
the third one. it follows lowercase letters for variable names, and also is descriptive.
dont be they guy that in a full code base uses, x, y ,z ,j, l everywhere (Eric smid example :P)
</p>
</details>