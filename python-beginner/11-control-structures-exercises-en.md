# Python Conditional Exercises

## Exercise 1: Temperature Classifier
Write a program that asks for a temperature in Celsius and prints a message:

- If temperature is above 30°C: "It's hot!"
- If temperature is between 20°C and 30°C: "It's nice!"
- If temperature is between 10°C and 20°C: "It's cool!"
- If temperature is below 10°C: "It's cold!"

Your code should start like this:

```py
temperature = float(input("Enter the temperature in Celsius: "))
```

## Exercise 2: Grade Calculator
Create a program that converts a numerical grade to a letter grade:

- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Below 60: F

Your code should start like this:

```py
score = float(input("Enter your score (0-100): "))
```

## Exercise 3: Simple Calculator
Write a calculator program that:

- Asks for two numbers
- Asks for an operation (+, -, *, /)
- Prints the result
- For division, check if the second number is zero and print an error if it is

Your code should start like this:
```py
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
```

## Exercise 4: Password Strength Checker
Write a program that checks if a password is "Strong", "Medium", or "Weak":

- Strong: 8 or more characters
- Medium: 5-7 characters
- Weak: less than 5 characters

Your code should start like this:

```py
password = input("Enter your password: ")
password_length = len(password)
```

## Exercise 5: Movie Ticket Calculator
Create a program that calculates movie ticket prices based on age:

- Under 5: Free
- 5-12: $8
- 13-17: $12
- 18-64: $15
- 65 and over: $10

Your code should start like this:

```py
age = int(input("Enter your age: "))
```

## Bonus Challenge: Rock, Paper, Scissors
Create a simple rock, paper, scissors game where:

Ask the player to choose rock, paper, or scissors
Compare it against a fixed choice (e.g., "rock")
Determine if the player wins, loses, or if it's a tie


Your code should start like this:

```py
player_choice = input("Choose rock, paper, or scissors: ").lower()
computer_choice = "rock"  # Fixed choice for simplicity
```

## Practice Tips

- Test your code with different inputs
- Make sure to handle invalid inputs where necessary
- Pay attention to the indentation of your if/elif/else statements
- Try to make your code readable by using clear variable names

Solutions Format
For each exercise, your solution should follow this pattern:

- Get input from the user
- Use if/elif/else to check conditions
- Print appropriate output message