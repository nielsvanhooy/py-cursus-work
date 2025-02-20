## Loops

Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages use loops. Python programming language also provides the following types of two loops:

1. while loop
2. for loop

### While Loop

if we think back to the if/elif/else lesson 

```shell
# syntax
if <condition>:
    <expression>
```

When `<condition>` is evaluated by Python, it’ll become either True or False (Booleans). 
Thus, if the condition is True (i.e, it is met), the `<expression>` will be executed, 
but if <condition> is False (i.e., it is not met), the `<expression>` won’t be executed.

`while` loops are bit of the same.

We use the reserved word `while` to make a while loop. 
It is used to execute a block of statements repeatedly until a given condition is satisfied. 
When the condition becomes false, the lines of code after the loop will be continued to be executed.


looping in programming is also called "iteration". 
and the thing you are going to loop over is called an "iterable" 
so what things we learned up until now are "iterables" ??

another way to think of it is iterating over sequences.
sequences are lists, tuples, strings, dictionaries, sets, etc.

whereas int, float, bool, None, etc are not sequences.
if you want to proof this:

```py
from collections.abc import Sequence      # what is Sequence?

def is_sequence(obj):
    return isinstance(obj, Sequence)

# Test cases
print(is_sequence([1, 2, 3]))        # True (list)
print(is_sequence((1, 2, 3)))       # True (tuple)
print(is_sequence("hello"))         # True (str)
print(is_sequence(range(5)))        # True (range)
print(is_sequence({1, 2, 3}))       # False (set)
print(is_sequence({"a": 1}))        # False (dict)
print(is_sequence(42))             # False (int)
```
but you dont have to remember this. just know that you can loop over sequences.


# lets go looping!
**Example:**

```py
count = 0                # we need to use this to keep track of the while loop
while count < 5:
    print(count)
    count = count + 1    # we increase the count by 1 each time the loop is executed
#prints from 0 to 4
```

In the above while loop, the condition becomes false when count is 5. That is when the loop stops.

In these examples we made a variable with the intention to keep track of the loop.
obviously you can also do this with a boolean value. and later set it to False.

If we are interested to run block of code once the condition is no longer true, we can use _else_.

```py
  # syntax
while condition:
    code goes here
else:
    code goes here
```

**Example:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

The above loop condition will be false when count is 5 and the loop stops, 
and execution starts the else statement. 
As a result 5 will be printed.


We can also nest control structures in while loops.

```py
count = 0                         # we keep track of the count
while count < 5:
   if count == 3:
       print("count is 3")
   elif count == 4:
       print("count is 4")
   count = count + 1              # we increase the count by 1 each time the loop is executed
else:
    print(count)
```


### Break and Continue - Part 1

- Break: We use break when we like to get out of or stop the loop.
- i like to think of it as: jumping out of the loop.

```py
# syntax
while condition:
    code goes here
    if another_condition:
        break
```

**Example:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```

The above while loop only prints 0, 1, 2, but when it reaches 3 it stops.

- Continue: With the continue statement we can skip the current iteration, and continue with the next:

```py
  # syntax
while condition:
    code goes here
    if another_condition:
        continue
```

**Example:**

```py
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
```

The above while loop only prints 0, 1, 2 and 4 (skips 3).

### For Loop

A `for` keyword is used to make a for loop, 
similar with other programming languages, but with some syntax differences. 

a `for` Loop is also used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

- For loop with list

```py
# syntax
for iterator in lst:
    code goes here
```

**Example:**

```py
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
```

another example:

```py
names = ['Lily', 'Brad', 'Fatima', 'Zining']

for name in names:
    print("Hello, " + name + "!")
```

This code in this simple loop raises a question, though: where did the variable name come from? 
We haven't defined it previously in our code! 
But loops iterate through sequences :lists, tuples, etc. 
This variable can actually be called almost anything. 
Python will interpret any variable name we put in that spot as referring to each list entry in sequence as the loop executes.

So, in the code above:

- name points to 'Lily' on the first iteration of the loop...
- ...then 'Brad' on the second iteration of the loop...
- ...and so on.

This will be the case regardless what we call that variable. 
So if, for example, we rewrite our code to replace name with x, we'll get the same exact result:

```py
names = ['Lily', 'Brad', 'Fatima', 'Zining']

for x in names:
    print(x)
```
will print:
- Lily
- Brad
- Fatima
- Zining



For loop with string

```py
# syntax
for iterator in string:
    code goes here
```

**Example:**

```py
language = 'Python'
for letter in language:
    print(letter)
    
# this would print each letter of the string on a new line

for i in range(len(language)):
    print(language[i])

# above does the same thing as the first loop
# we peel it back as always

# len(language)  gets the human range notation of the word Python (so 6 letters)
# range(6)  gets the computer range notation of the word Python (so 0 to 5)

# and then we loop over the range of the length of the word Python (and i is the index of the letter)
# then we print the letter
```

we will go more into len() and range() later on. and in the exercises.

Lets do a thought experiment:

```py
language = 'Python'
for i in len("Python"):
    print(language[i])
```
what do you expect?
why did this happened?

this happened because len("Python") is 6 (and an int is not iterable (not a sequence))
and range(6) is 0 to 5 (so that is a sequence)

it's getting harder he?

# other examples (iterating on collections/data structure/sequeces) we have not yet discussed
- For loop with tuple  (tuples havent been discussed yet) but is also a sequence and can be looped over. (collection)

```py
# syntax
for iterator in tpl:
    code goes here
```

**Example:**

```py
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

- For loop with dictionary
  Looping through a dictionary gives you the key of the dictionary.

```py
  # syntax
for iterator in dct:
    code goes here
```

**Example:**

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out
```

- Loops in set

```py
# syntax
for iterator in st:
    code goes here
```

**Example:**

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

# Let's move on
### Break and Continue - Part 2

Short reminder:
_Break_: We use break when we like to stop our loop before it is completed.

```py
# syntax
for iterator in sequence:
    code goes here
    if condition:
        break
```

**Example:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```

In the above example, the loop stops when it reaches 3.

Continue: We use continue when we like to skip some of the steps in the iteration of the loop.

```py
  # syntax
for iterator in sequence:
    code goes here
    if condition:
        continue
```

**Example:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')
```

In the example above, if the number equals 3, the step *after* the condition (but inside the loop) is skipped and the execution of the loop continues if there are any iterations left.

### The Range Function

The _range()_ function gives a list of numbers. 
The _range(start, end, step)_ takes three parameters: starting, ending and increment. 
By default it starts from 0 and the increment is 1. 
The range sequence needs at least 1 argument (end).

Creating sequences using range

```py
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}
```

```py
# syntax
for iterator in range(start, end, step):
```

**Example:**

```py
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
```

### Nested For Loop

We can write loops inside a loop.

```py
# syntax
for x in y:
    for t in x:
        print(t)
```

Example:

```py
ev_data = [['vehicle', 'range', 'price'], 
           ['Tesla Model 3 LR', '310', '49900'], 
           ['Hyundai Ioniq EV', '124', '30315'],
           ['Chevy Bolt', '238', '36620']]

for ev in ev_data:
    for ev_specs in ev:
        print(ev_specs)
```


**Example:**

```py
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

### For Else

If we want to execute some message when the loop ends, we use else.

```py
# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
```

**Example:**

```py
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
```

### Pass

In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word _pass_ to avoid errors. Also we can use it as a placeholder, for future statements.

**Example:**

```py
for number in range(6):
    pass
```

If you understand everything up until now.
You established a big milestone. trough practice you will get better and better.

# Note:

With all that knowledge up until know you can already make some beefy programs.


