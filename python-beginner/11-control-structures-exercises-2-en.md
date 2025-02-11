# Python Exercises: Practice with 'and' & 'or'


## Exercise 1: Number Range Checker
Write a program that checks if a number is in a specific range OR is a special number:

Between 20-50 OR equals 77
Print "Valid number!" if condition is met
Print "Invalid number!" otherwise

Your code should start like this:

```py
number = int(input("Enter a number: "))
# Check if number is between 20-50 OR equals 77
```

## Exercise 2: Login System
Create a simple login system where:

Valid username is "admin" OR "user"
Password must be longer than 6 characters AND contain the number "1"
Print "Access granted" or an appropriate error message.

Your code should start like this:

```py
username = input("Enter username: ")
password = input("Enter password: ")
# Check username AND password conditions
```

## Exercise 3: Game Player Eligibility
Check if someone can join a game where they need to be:

Between 13 and 19 years old (teenager) OR
Have parental permission AND be over 10 years old

Your code should start like this:

```py
age = int(input("Enter your age: "))
has_permission = input("Do you have parental permission? (yes/no): ").lower()
# Check age AND permission conditions
```

## Exercise 4: Fruit Ripeness Checker
Create a program that checks if a fruit is ready to eat:

Banana: Should be yellow OR brown
Should NOT be green AND should NOT be black

Your code should start like this:

```py
fruit_color = input("What color is the banana? (green/yellow/brown/black): ").lower()
# Check color conditions using AND/OR
```

## Exercise 5: Special Order Discount
Write a program for a special discount where:

Customer gets a discount if:

Order is over $200 AND customer is a member, OR
Order is over $500 (regardless of membership)



Your code should start like this:

```py
order_amount = float(input("Enter order amount: $"))
is_member = input("Are you a member? (yes/no): ").lower() == "yes"
# Check discount conditions using AND/OR
```

