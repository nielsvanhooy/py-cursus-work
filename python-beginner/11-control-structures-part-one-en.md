# Control Structures/Flow
---
## Control structures
---
Our life is full of conditions even if we don’t notice them most of the time. Let’s look at a few examples:

If tomorrow it doesn't rain, I’ll go out with my friends in the park. 
Otherwise, I’ll stay home with a cup of hot tea and watch TV.


If tomorrow it isn't too hot, I’ll go to the sea, but if it is, I’ll have a walk in the forest. 
However, if it rains, I’ll stay home.

## Basic if Statement
In Python, if statements are a starting point to implement a condition. Let’s look at the simplest example:

```shell
if <condition>:
    <expression>
```

When `<condition>` is evaluated by Python, it’ll become either True or False (Booleans). 
Thus, if the condition is True (i.e, it is met), the `<expression>` will be executed, 
but if <condition> is False (i.e., it is not met), the `<expression>` won’t be executed.

We are pretty free to decide what conditions and expressions can be because Python is very flexible.



for conditions we will need the following table:

| Operator | Meaning                  | Example |
|----------|--------------------------|---------|
| `==`     | equal to                 | x == y  |
| `!=`     | not equal to             | x != y  |
| `>`      | greater then             | x > y   |
| `>=`     | greater then or equal to | x >= y  |
| `<`      | less than                | x < y   |
| `<=`     | less then or equal       | x <= y  |

and for the logical operators we need the following table:

| Operator | Meaning                  | Example |
|----------|--------------------------|---------|
| `and`    | True if both are true    | x and y |
| `or`     | True if at least one is true  | x or y  |
| `not`    | True only if false           | not x   |


We now the concept of True and False right?
But in programming languages we also have `Truthy` and `Falsy` values.

# 🔸 Falsy Values in Python

some below here. we haven't discussed yet. ill point them out when we get there.

Sequences and Collections:

- Empty lists []
- Empty tuples ()
- Empty dictionaries {}
- Empty sets set()
- Empty strings ""
- Empty ranges range(0)
- Numbers

Zero of any numeric type:

- Integer: 0
- Float: 0.0
- Complex: 0j

Constants:

- None
- False

## 🔹 Truthy Values in Python
According to the Python Documentation:

By default, an object is considered true.

Truthy values include:

- Non-empty sequences or collections (lists, tuples, strings, dictionaries, sets).
- Numeric values that are not zero.
- True


## How to check this?

🔸 The Built-in bool() Function
You can check if a value is either truthy or falsy with the built-in `bool()` function.
---
# Playing with if statements
Now Let’s look at a concrete example.
```py
# Basic if statement
x = 3
y = 10

if x < y:
    print("x is smaller than y.")
```

the condition here is: x is smaller than y.

First of all, we define two variables, x and y. 
Then we say that if variable x is smaller than variable y, print out x is smaller than y). 
Indeed, if we execute this code, we’ll print out this output because 3 is smaller than 10.

Output: x is smaller than y.

```pycon
# A slightly more complex example
x = 3
y = 10
z = None

if x < y:
    z = 13
print(f"Variable z is now {z}.")
```

Variable z is now 13.

In this case, if the condition is met, 
then a value of 13 will be assigned to the variable z. 
Then Variable z is now 13. will be printed out (note that the print statement can be used both outside and inside the if statement).

As you can see, we aren't restrained in the choice of an expression to execute. 
You can now practice more by writing more complex code.

```py
# What happens here?
x = 3
y = 10

if x > y:
    print("x is greater than y.")
```
---
## Else Statement

What if we want to execute some code if the condition isn't met? 
We add an else statement below the if statement. 
Let’s look at an example.

```py
# else statement
x = 3
y = 10

if x > y:
    print("x is greater than y.")
else:
    print("x is smaller than y.")
```
What would be the answer here?

<details>
    <summary>Click to reveal more</summary>
<p>
Here, Python first executes the if condition and checks if it’s True. 
Since 3 is not greater than 10, the condition isn't met, 
so we don’t print out “x is greater than y.” 
Then we say that in all other cases we should execute the code under the else statement: x is smaller than y.
</p>
</details>

```py
# x is equal to y
x = 3
y = 3

if x < y:
    print("x is smaller than y.")
else:
    print("x is greater than y.")
```
what would happen here??

<details>
    <summary>Click to reveal more</summary>
<p>
The output is clearly wrong because 3 is equal to 3! 
We have another condition outside the greater or less than comparison symbols; 
thus, we have to use the elif statement.
</p>
</details>

---
## elif Statement
Let’s rewrite the above example and add an elif statement.

```py
# x is equal to y with elif statement
x = 3
y = 3

if x < y:
    print("x is smaller than y.")
elif x == y:
    print("x is equal to y.")
else:
    print("x is greater than y.")
```

Python first checks if the condition x < y is met. 
It isn't, so it goes on to the second condition, 
which in Python, we write as elif, which is short for else if. 
If the first condition isn't met, check the second condition, and if it’s met,
execute the expression. 
Else, do something else. 

The output is “x is equal to y.”

---
Let’s now get back to one of our first examples of conditional statements:

If tomorrow it isn't too hot, I’ll go to the sea, but if it is, I’ll have a walk in the forest. However, if it rains, I’ll stay home.

Here, our first condition is that tomorrow it’s not too hot (if statement). 
If this condition isn't met, then we go for a walk in the forest (elif statement). 
Finally, if neither condition is met, we’ll stay home (else statement).

Now let’s translate this sentence into Python.

```py
# elif condition
tomorrow = "warm"

if tomorrow == "warm":
    print("I'll go to the sea.")
elif tomorrow == "very hot":
    print("I'll go to the forest.")
else:
    print("I'll stay home.")
```

<details>
    <summary>Click to reveal more</summary>
<p>
Python first checks if the variable tomorrow is equal to “warm” and if it is, 
then it prints out I'll go to the sea. 
and stops the execution. 
</p>
</details>


What happens if the first condition isn't met?

```py
# Tomorrow is very hot
tomorrow = "very hot"

if tomorrow == "warm":
    print("I'll go to the sea.")
elif tomorrow == "very hot":
    print("I'll go to the forest.")
else:
    print("I'll stay home.")
```

<details>
    <summary>Click to reveal more</summary>
<p>
In this case, 
Python evaluates the first condition to False and goes to the second condition. 
This condition is True, so it prints out I'll go to the forest. 
and stops the execution.

If neither of the two conditions is met, then it’ll print out I’ll stay home.
</p>
</details>

Of course, you can use whatever number of elif statements you want. 
Let’s add more conditions and also change what is printed out under the else statement to Weather not recognized. 
(for example, if tomorrow is “f”, we don’t know what it means).

```py
# Several elif conditions
tomorrow = "snowy"

if tomorrow == "warm":
    print("I'll go to the sea.")
elif tomorrow == "very hot":
    print("I'll go to the forest.")
elif tomorrow == "snowy":
    print("I'll build a snowman.")
elif tomorrow == "rainy":
    print("I'll stay home.")
else:
    print("Weather not recognized.")
```
guess what would be printed now?
<details>
    <summary>Click to reveal more</summary>
<p>
I'll build a snowman.
</p>
</details>

---
## Multiple Conditions
Let’s now add some complexity. 
What if we want to meet multiple conditions in one if statement?

Let’s say we want to predict a biome (i.e., desert or tropical forest) based on two climate measurements: temperature and humidity. 

For example, if it’s hot and dry, then it’s a hot desert, but if it’s cold and dry, then it’s an arctic desert. 

You can see that we cannot classify these two biomes based only on their humidity (they are both dry) so we also have to add the temperature measure.

In Python, we can use logical operators (i.e., and, or) to use multiple conditions in the same if statement.

Look at the code below.

```py
# Biome prediction with and logical operator
humidity = "low"
temperature = "high"

if humidity == "low" and temperature == "high":
    print("It's a hot desert.")
elif humidity == "low" and temperature == "low":
    print("It's an arctic desert.")
elif humidity == "high" and temperature == "high":
    print("It's a tropical forest.")
else:
    print("I don't know!")
```
<details>
    <summary>Click to reveal more</summary>
<p>
The output will be It's a hot desert.<br>
because only when humidity is low and temperature is high, the combined condition is True.
<br>
It’s not sufficient to have only one of the conditions to be True.
<br>
Formally, Python checks if the first condition of humidity is True (indeed, it is),
<br>
then it checks if the second condition of temperature is True (and it is) and only in this case the combined condition is True. 
<br>
If at least one of these conditions isn't met, then the combined condition evaluates to False.

</p>
</details>

---
# Nested if Statements

Python is a very flexible programming language, and it allows you to use if statements inside other if statements, 
so called nested if statements. Let’s look at an example.

```py
# Nested if statements
mark =  85

if mark >= 60 and mark <= 100:
    if mark >= 90:
        print("You are the best!")
    elif mark >= 80:
        print("Well done!")
    elif mark >= 70:
        print("You can do better.")
    else:
        print("Pass.")
elif mark > 100:
    print("This mark is too high.")
elif mark < 0:
    print("This mark is too low.")
else:
    print("Failed.")
```
<details>
    <summary>Click to reveal more</summary>
<p>
Well done!

Here, if the mark is between 60 and 100, 
<br>
the expression under the if statement is executed. 
<br><br>
But then we have other conditions that are also evaluated. 
<br>
So, our mark is 85, which is between 60 and 100. However, 85 is smaller than 90, so the first nested if condition is False, and the first nested expression isn't executed. 
<br><br>
But 85 is higher than 80, so the second expression is executed and “Well done!” is printed out.
<br><br>
Of course, we also have elif statements outside the expression below the first if statement. 
<br><br>
For example, what if the mark is higher than 100? If the first condition (number between 60 and 100) is False, then we go directly to the elif statement mark > 100 and print out This mark is too low..
<br><br>
Try to assign different numbers to the mark variable to understand the logic of this code.
</p>
</details>
---
## Pattern Matching in Python

The pattern matching was added in Python 3.10, released in October, 2021. 
In short, it can be seen a different syntax for if..elif statements. 

However i have never come in across it in codebases around the internet (yet)
Just know it exists we will not use it in this course. and in the projects we have. (unless its proven to be faster)

Let's look at an example by rewrting a previous example using the pattern matching.


```py
# Previous example
tomorrow = "snowy"

if tomorrow == "warm":
    print("I'll go to the sea.")
elif tomorrow == "very hot":
    print("I'll go to the forest.")
elif tomorrow == "snowy":
    print("I'll build a snowman.")
elif tomorrow == "rainy":
    print("I'll stay home.")
else:
    print("Weather not recognized.")
```

now with pattern matching:

```py
# Pattern matching with match..case syntax
tomorrow = "snowy"

match tomorrow:
    case "warm":
        print("I'll go to the sea.")
    case "very hot":
        print("I'll go to the forest.")
    case "snowy":
        print("I'll build a snowman.")
    case "rainy":
         print("I'll stay home.")
    case _:
        print("Weather not recognized.")
```

result is: i'll build a snowman.

We can see similarities between using the if..elif statements and the match..case syntax. 
First, we define what variable we want to match, and when we define the cases (or values this variable can take). 
The rest of the code is similar. 
If a case is matched (that's equivalent of a double equal sign), then the print expression is executed.

Note the last case statement, 
it's the _ case, which is equivalent to else: if no cases are matched, then we print Weather not recognized.

---
## pass Statement

As you start writing more complex code, you may find yourself in the situation where you have to use a placeholder instead of the code you want to implement later. 
The pass statement is this placeholder. Let’s look at an example with and without the pass statement.

```py
# Without pass
num = 3
if num == 3:

print("I'll write this code later.")
```
would result in an error

```py
  Input In [24]
    print("I'll write this code later.")
    ^
IndentationError: expected an indented block after 'if' statement on line 3
```

Python expects some code under the if statement, but you are yet to implement it! 
You can write pass there and solve this problem.

```py
# With pass
num = 3
if num == 3:
    pass

print("I'll write this code later.")
```
If instead you place pass in the if statement, 
Python won’t throw any error and will pass to any code you have below the if statement. 
This works even if you have other conditions below the first if statement.
