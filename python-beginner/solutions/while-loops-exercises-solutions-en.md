## Beginner Exercises

### Exercise 1: Print Numbers from 1 to 10

#### Description
Write a program that uses a `while` loop to print the numbers from 1 to 10.

keep note you need something to keep track with a while loop.

#### Solution
```python
num = 1
while num <= 10:
    print(num)
    num += 1
```

---

### Exercise 2: Guess the Number

#### Description
Write a program that lets the user guess a number between 1 and 10. 
The program should keep asking until the user guesses correctly.

hint:
you can use the following to get a random number between 1 and 10.

```python
import random
secret_number = random.randint(1, 10)
```

#### Solution
```python
import random
secret_number = random.randint(1, 10)
guess = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess != secret_number:
        print("Wrong guess, try again!")

print("Congratulations! You guessed the correct number.")
```

---

## Intermediate Exercises

### Exercise 4: Countdown Timer

#### Description
Create a program that asks the user to enter a number and then counts down to zero, printing each number. When it reaches zero, print "Time's up!".

#### Solution
```python
num = int(input("Enter a number to start the countdown: "))

while num >= 0:
    print(num)
    num -= 1

print("Time's up!")
```

---

### Exercise 4: Shopping List

#### Description
Create a shopping list program where users can continuously add items to their list. The program should allow users to type "done" when they finish adding items. Finally, print the full shopping list.

#### Solution
```python
shopping_list = []

while True:
    item = input("Enter an item for your shopping list (or type 'done' to finish): ")
    if item.lower() == "done":
        break
    shopping_list.append(item)

print("Your shopping list:")
for item in shopping_list:
    print("-", item)
```

