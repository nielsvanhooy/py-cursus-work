# Python Function Refactoring Exercises

These exercises will help you practice refactoring simple scripts into a function-based design. For each exercise, you'll be given a script that works but isn't well-structured. Your task is to identify the different functionalities and refactor them into functions.

## Refactoring Instructions:

For each exercise:
1. Identify the different functionalities in the script
2. Create appropriate functions for each functionality
3. Create a main function that controls the program flow
4. Make sure your solution maintains all the original functionality

Your refactored code should be more modular, easier to maintain, and follow good function-based design principles. (below)

1. Use a function whenever you see any code repetition.
2. Use long clear names that make it obvious what your function is doing.
3. Docstrings (google this but only do it when youre done)
4. Try to have small function interfaces. 3-4 input parameters at the most.
5. Validate your inputs. Like if your function expects numbers as inputs, verify that they are numbers before performing any operations. In case of bad inputs, throw an exception or handle it gracefully in the function while returning an error message.
6. Try to make sure your function does only one thing. This will help avoid longer functions.


## Exercise 1: Temperature Converter

```python
# Current script: Temperature Converter

print("Temperature Converter")
print("---------------------")

while True:
    print("\nOptions:")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")
    
    choice = input("Select an option (1-3): ")
    
    if choice == "1":
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C is equal to {fahrenheit:.1f}°F")
        except ValueError:
            print("Please enter a valid number.")
    
    elif choice == "2":
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F is equal to {celsius:.1f}°C")
        except ValueError:
            print("Please enter a valid number.")
    
    elif choice == "3":
        print("Thank you for using Temperature Converter. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option (1-3).")
```

## Exercise 2: To-Do List

```python
# Current script: To-Do List

todo_list = []

print("Simple To-Do List")
print("-----------------")

while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")
    
    if choice == "1":
        task = input("Enter task description: ")
        todo_list.append({"task": task, "done": False})
        print(f"Task '{task}' added to the list!")
    
    elif choice == "2":
        if not todo_list:
            print("Your to-do list is empty!")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(todo_list, 1):
                status = "✓" if task["done"] else " "
                print(f"{i}. [{status}] {task['task']}")
    
    elif choice == "3":
        if not todo_list:
            print("Your to-do list is empty!")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(todo_list, 1):
                status = "✓" if task["done"] else " "
                print(f"{i}. [{status}] {task['task']}")
            
            try:
                task_num = int(input("\nEnter task number to mark as done: "))
                if 1 <= task_num <= len(todo_list):
                    todo_list[task_num-1]["done"] = True
                    print(f"Task '{todo_list[task_num-1]['task']}' marked as done!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    
    elif choice == "4":
        print("Thank you for using the To-Do List. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option (1-4).")
```

## Exercise 3: Simple Budget Tracker

```python
# Current script: Simple Budget Tracker

transactions = []
budget = 0

print("Simple Budget Tracker")
print("--------------------")

# Set initial budget
try:
    budget = float(input("Enter your starting budget: $"))
except ValueError:
    print("Invalid amount. Setting budget to $0.")
    budget = 0

while True:
    print("\nOptions:")
    print("1. Add income")
    print("2. Add expense")
    print("3. View transactions")
    print("4. Check current balance")
    print("5. Exit")
    
    choice = input("Select an option (1-5): ")
    
    if choice == "1":
        try:
            description = input("Enter income description: ")
            amount = float(input("Enter amount: $"))
            
            if amount <= 0:
                print("Amount must be positive.")
                continue
                
            transactions.append({"type": "income", "description": description, "amount": amount})
            budget += amount
            print(f"Income of ${amount:.2f} added successfully!")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    
    elif choice == "2":
        try:
            description = input("Enter expense description: ")
            amount = float(input("Enter amount: $"))
            
            if amount <= 0:
                print("Amount must be positive.")
                continue
                
            transactions.append({"type": "expense", "description": description, "amount": amount})
            budget -= amount
            print(f"Expense of ${amount:.2f} added successfully!")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    
    elif choice == "3":
        if not transactions:
            print("No transactions recorded yet.")
        else:
            print("\nTransaction History:")
            for i, t in enumerate(transactions, 1):
                t_type = "Income" if t["type"] == "income" else "Expense"
                print(f"{i}. {t_type}: {t['description']} - ${t['amount']:.2f}")
    
    elif choice == "4":
        print(f"Current Balance: ${budget:.2f}")
        
        if budget < 0:
            print("Warning: Your balance is negative!")
    
    elif choice == "5":
        print("Thank you for using the Budget Tracker. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option (1-5).")
```

## Exercise 4: Quiz Game

```python
# Current script: Quiz Game

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "correct_answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "correct_answer": "B"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A. Elephant", "B. Giraffe", "C. Blue Whale", "D. Gorilla"],
        "correct_answer": "C"
    }
]

score = 0
total_questions = len(questions)

print("Welcome to the Quiz Game!")
print("-----------------------")
print(f"This quiz has {total_questions} questions.\n")

# Ask each question
for i, q in enumerate(questions, 1):
    print(f"Question {i}: {q['question']}")
    
    for option in q['options']:
        print(option)
    
    # Get user's answer
    user_answer = input("\nYour answer (A, B, C, or D): ").upper()
    
    # Check if valid answer
    if user_answer not in ["A", "B", "C", "D"]:
        print("Invalid choice. Moving to next question.")
        continue
    
    # Check if correct answer
    if user_answer == q['correct_answer']:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {q['correct_answer']}.")
    
    print() # Empty line between questions

# Display results
print("Quiz completed!")
print(f"Your score: {score}/{total_questions}")
percentage = (score / total_questions) * 100
print(f"Percentage: {percentage:.1f}%")

if percentage >= 70:
    print("Great job!")
else:
    print("Better luck next time!")
```

## Exercise 5: Password Generator

```python
# Current script: Password Generator

import random
import string

print("Password Generator")
print("-----------------")

# Get password length
while True:
    try:
        length = int(input("Enter password length (8-16): "))
        if 8 <= length <= 16:
            break
        else:
            print("Password length should be between a and 16 characters.")
    except ValueError:
        print("Please enter a valid number.")

# Get password options
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
include_numbers = input("Include numbers? (y/n): ").lower() == "y"
include_symbols = input("Include symbols? (y/n): ").lower() == "y"

# Generate character pool based on selections
characters = string.ascii_lowercase
if include_uppercase:
    characters += string.ascii_uppercase
if include_numbers:
    characters += string.digits
if include_symbols:
    characters += string.punctuation

# Check if at least one option was selected
if characters == string.ascii_lowercase:
    characters += string.digits  # Add digits if no options were selected
    print("Note: Added numbers to ensure stronger password.")

# Generate password
password = ""
for _ in range(length):
    password += random.choice(characters)

# Ensure password meets complexity requirements
if include_uppercase and not any(c.isupper() for c in password):
    password = password[:-1] + random.choice(string.ascii_uppercase)
    
if include_numbers and not any(c.isdigit() for c in password):
    password = password[:-1] + random.choice(string.digits)
    
if include_symbols and not any(c in string.punctuation for c in password):
    password = password[:-1] + random.choice(string.punctuation)

# Display generated password
print("\nGenerated Password:")
print(password)

# Password strength evaluation
strength = "Weak"
if length >= 12 and all([include_uppercase, include_numbers, include_symbols]):
    strength = "Strong"
elif length >= 10 and sum([include_uppercase, include_numbers, include_symbols]) >= 2:
    strength = "Medium"

print(f"Password Strength: {strength}")
print("\nThank you for using the Password Generator!")
```