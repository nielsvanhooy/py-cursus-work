```py
# Exercise 1: Temperature Classifier
def temperature_classifier():
    temperature = float(input("Enter the temperature in Celsius: "))
    
    if temperature > 30:
        print("It's hot!")
    elif temperature >= 20:  # Between 20 and 30
        print("It's nice!")
    elif temperature >= 10:  # Between 10 and 20
        print("It's cool!")
    else:  # Below 10
        print("It's cold!")

# Exercise 2: Grade Calculator
def grade_calculator():
    score = float(input("Enter your score (0-100): "))
    
    if score >= 90 and score <= 100:
        print("Your grade is: A")
    elif score >= 80:
        print("Your grade is: B")
    elif score >= 70:
        print("Your grade is: C")
    elif score >= 60:
        print("Your grade is: D")
    elif score >= 0:
        print("Your grade is: F")
    else:
        print("Invalid score! Please enter a number between 0 and 100")

# Exercise 3: Simple Calculator
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    
    if operation == "+":
        print(f"Result: {num1 + num2}")
    elif operation == "-":
        print(f"Result: {num1 - num2}")
    elif operation == "*":
        print(f"Result: {num1 * num2}")
    elif operation == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print(f"Result: {num1 / num2}")
    else:
        print("Invalid operation! Please use +, -, *, or /")

# Exercise 4: Password Strength Checker
def password_checker():
    password = input("Enter your password: ")
    password_length = len(password)
    
    if password_length >= 8:
        print("Strong password")
    elif password_length >= 5:
        print("Medium password")
    else:
        print("Weak password")

# Exercise 5: Movie Ticket Calculator
def ticket_calculator():
    age = int(input("Enter your age: "))
    
    if age < 5:
        price = 0
        print("Your ticket is free!")
    elif age <= 12:
        price = 8
        print(f"Your ticket costs ${price}")
    elif age <= 17:
        price = 12
        print(f"Your ticket costs ${price}")
    elif age <= 64:
        price = 15
        print(f"Your ticket costs ${price}")
    else:
        price = 10
        print(f"Your ticket costs ${price}")

# Bonus Challenge: Rock, Paper, Scissors
def rock_paper_scissors():
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = "rock"  # Fixed choice for simplicity
    
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors")
        return
        
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "paper":
        print("You win! Paper covers rock")
    elif player_choice == "scissors":
        print("You lose! Rock crushes scissors")
    else:  # player chose rock
        print("It's a tie!")

# Test any solution by calling its function
if __name__ == "__main__":
    print("Testing Temperature Classifier:")
    temperature_classifier()
```