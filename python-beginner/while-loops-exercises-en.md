## Beginner Exercises

### Exercise 1: Print Numbers from 1 to 10

#### Description
Write a program that uses a `while` loop to print the numbers from 1 to 10.
Note: you need something to keep track with a while loop.

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

---

## Intermediate Exercises

### Exercise 4: Countdown Timer

#### Description
Create a program that asks the user to enter a number and then counts down to zero, 
printing each number. When it reaches zero, print "Time's up!".


---

### Exercise 4: Shopping List

#### Description
Create a shopping list program where users can continuously add items to their list. The program should allow users to type "done" when they finish adding items. Finally, print the full shopping list.



## Hints

- Remember that a while loop runs as long as a condition is True. Be careful to update your condition inside the loop to prevent infinite loops.
- User Input: Always ensure that inputs are converted to the correct type (e.g., int(input(...)) if working with numbers).
- Incrementing values: If your loop isn't stopping when expected, check whether you're correctly updating the variables inside the loop.
- Edge Cases: Think about what happens if the user enters unexpected input (e.g., negative numbers or letters instead of numbers).