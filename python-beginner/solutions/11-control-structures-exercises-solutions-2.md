```py
Here are the solutions:
pythonCopy# Exercise 1: Number Range Checker
def check_number():
    number = int(input("Enter a number: "))
    if (number >= 20 and number <= 50) or number == 77:
        print("Valid number!")
    else:
        print("Invalid number!")

# Exercise 2: Login System
def login_checker():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if (username == "admin" or username == "user") and len(password) > 6 and "1" in password:
        print("Access granted!")
    else:
        if username != "admin" and username != "user":
            print("Invalid username!")
        else:
            print("Invalid password! Must be longer than 6 characters and contain the number 1")

# Exercise 3: Game Player Eligibility
def check_eligibility():
    age = int(input("Enter your age: "))
    has_permission = input("Do you have parental permission? (yes/no): ").lower()
    
    if (age >= 13 and age <= 19) or (age > 10 and has_permission == "yes"):
        print("You can play the game!")
    else:
        print("Sorry, you're not eligible to play.")

# Exercise 4: Fruit Ripeness Checker
def check_fruit():
    fruit_color = input("What color is the banana? (green/yellow/brown/black): ").lower()
    
    if (fruit_color == "yellow" or fruit_color == "brown") and not (fruit_color == "green" or fruit_color == "black"):
        print("The banana is ready to eat!")
    else:
        print("The banana is not ready to eat!")

# Exercise 5: Special Order Discount
def check_discount():
    order_amount = float(input("Enter order amount: $"))
    is_member = input("Are you a member? (yes/no): ").lower() == "yes"
    
    if (order_amount > 200 and is_member) or order_amount > 500:
        print("Congratulations! You get a special discount!")
    else:
        print("Sorry, you don't qualify for the special discount.")
```