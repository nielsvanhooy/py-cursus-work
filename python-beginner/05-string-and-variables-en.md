# Printing, Variables


# Printing in python.

We begin our python journey with a command that most of you already now.

**the print statement.**

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

## Variables

Variables are containers for storing data values.

```py
birth_year = 1970
current_year = 2020
age = current_year - birth_year
```

Names of variables are usually written in lower case, separating words by underscores

Variable names may only consist of letters, digits and underscores

## Variables

Overwriting (reassigning) variables:

```py
name = "John"
name = "Jane"
a = 3
a = a + 1
```

## Conventions

```py
NIELS_BIRTH_YEAR = 1987  # we call this a CONSTANT. because my birth year will never change
_current_year = 2025     # we call this a PRIVATE variable. it is not enforced by the language, but it is a convention for data the developer doenst want touched.
NIELS_BIRTH_YEAR_1987 = "1987" # we dont use numbers in variable names. this is a bad example.
```