# Python Function Refactoring Solutions

Below are the solutions for each exercise, showing how to refactor the scripts into a function-based design.

## Solution 1: Temperature Converter

```python
def display_menu():
    """Display the main menu options."""
    print("\nOptions:")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")
    return input("Select an option (1-3): ")

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def get_temperature():
    """Get a valid temperature input from the user."""
    try:
        return float(input("Enter temperature: "))
    except ValueError:
        print("Please enter a valid number.")
        return None

def main():
    """Main function to control program flow."""
    print("Temperature Converter")
    print("---------------------")
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            temp = get_temperature()
            if temp is not None:
                result = celsius_to_fahrenheit(temp)
                print(f"{temp}°C is equal to {result:.1f}°F")
        
        elif choice == "2":
            temp = get_temperature()
            if temp is not None:
                result = fahrenheit_to_celsius(temp)
                print(f"{temp}°F is equal to {result:.1f}°C")
        
        elif choice == "3":
            print("Thank you for using Temperature Converter. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option (1-3).")

# Start the program
if __name__ == "__main__":
    main()
```

## Solution 2: To-Do List

```python
def display_menu():
    """Display the main menu options."""
    print("\nOptions:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Exit")
    return input("Select an option (1-4): ")

def add_task(todo_list):
    """Add a new task to the to-do list."""
    task = input("Enter task description: ")
    todo_list.append({"task": task, "done": False})
    print(f"Task '{task}' added to the list!")
    return todo_list

def display_tasks(todo_list):
    """Display all tasks in the to-do list."""
    if not todo_list:
        print("Your to-do list is empty!")
        return False
    
    print("\nYour To-Do List:")
    for i in range(len(todo_list)):
        task = todo_list[i]
        status = "✓" if task["done"] else " "
        print(f"{i+1}. [{status}] {task['task']}")
    
    return True

def mark_task_done(todo_list):
    """Mark a task as done in the to-do list."""
    if not display_tasks(todo_list):
        return todo_list
    
    try:
        task_num = int(input("\nEnter task number to mark as done: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num-1]["done"] = True
            print(f"Task '{todo_list[task_num-1]['task']}' marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    
    return todo_list

def main():
    """Main function to control program flow."""
    todo_list = []
    
    print("Simple To-Do List")
    print("-----------------")
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            todo_list = add_task(todo_list)
        
        elif choice == "2":
            display_tasks(todo_list)
        
        elif choice == "3":
            todo_list = mark_task_done(todo_list)
        
        elif choice == "4":
            print("Thank you for using the To-Do List. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option (1-4).")

# Start the program
if __name__ == "__main__":
    main()
```

## Solution 3: Simple Budget Tracker

```python
def display_menu():
    """Display the main menu options."""
    print("\nOptions:")
    print("1. Add income")
    print("2. Add expense")
    print("3. View transactions")
    print("4. Check current balance")
    print("5. Exit")
    return input("Select an option (1-5): ")

def get_amount(prompt):
    """Get a valid positive amount from user input."""
    try:
        amount = float(input(prompt))
        if amount <= 0:
            print("Amount must be positive.")
            return None
        return amount
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return None

def add_income(transactions, budget):
    """Add an income transaction."""
    description = input("Enter income description: ")
    amount = get_amount("Enter amount: $")
    
    if amount is None:
        return transactions, budget
        
    transactions.append({"type": "income", "description": description, "amount": amount})
    budget += amount
    print(f"Income of ${amount:.2f} added successfully!")
    
    return transactions, budget

def add_expense(transactions, budget):
    """Add an expense transaction."""
    description = input("Enter expense description: ")
    amount = get_amount("Enter amount: $")
    
    if amount is None:
        return transactions, budget
        
    transactions.append({"type": "expense", "description": description, "amount": amount})
    budget -= amount
    print(f"Expense of ${amount:.2f} added successfully!")
    
    return transactions, budget

def view_transactions(transactions):
    """Display all transactions."""
    if not transactions:
        print("No transactions recorded yet.")
    else:
        print("\nTransaction History:")
        for i in range(len(transactions)):
            t = transactions[i]
            t_type = "Income" if t["type"] == "income" else "Expense"
            print(f"{i+1}. {t_type}: {t['description']} - ${t['amount']:.2f}")

def check_balance(budget):
    """Check and display current balance."""
    print(f"Current Balance: ${budget:.2f}")
    
    if budget < 0:
        print("Warning: Your balance is negative!")

def initialize_budget():
    """Initialize the starting budget."""
    try:
        budget = float(input("Enter your starting budget: $"))
        return budget
    except ValueError:
        print("Invalid amount. Setting budget to $0.")
        return 0

def main():
    """Main function to control program flow."""
    transactions = []
    
    print("Simple Budget Tracker")
    print("--------------------")
    
    budget = initialize_budget()
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            transactions, budget = add_income(transactions, budget)
        
        elif choice == "2":
            transactions, budget = add_expense(transactions, budget)
        
        elif choice == "3":
            view_transactions(transactions)
        
        elif choice == "4":
            check_balance(budget)
        
        elif choice == "5":
            print("Thank you for using the Budget Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option (1-5).")

# Start the program
if __name__ == "__main__":
    main()
```

## Solution 4: Quiz Game

```python
def display_welcome(total_questions):
    """Display welcome message and quiz info."""
    print("Welcome to the Quiz Game!")
    print("-----------------------")
    print(f"This quiz has {total_questions} questions.\n")

def ask_question(question_data, question_number):
    """Ask a question and check the answer."""
    print(f"Question {question_number}: {question_data['question']}")
    
    for i in range(len(question_data['options'])):
        print(question_data['options'][i])
    
    # Get user's answer
    user_answer = input("\nYour answer (A, B, C, or D): ").upper()
    
    # Check if valid answer
    if user_answer not in ["A", "B", "C", "D"]:
        print("Invalid choice. Moving to next question.")
        return 0
    
    # Check if correct answer
    if user_answer == question_data['correct_answer']:
        print("Correct!")
        return 1
    else:
        print(f"Incorrect. The correct answer is {question_data['correct_answer']}.")
        return 0

def display_results(score, total_questions):
    """Display quiz results."""
    print("Quiz completed!")
    print(f"Your score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")

    if percentage >= 70:
        print("Great job!")
    else:
        print("Better luck next time!")

def main():
    """Main function to control program flow."""
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
    
    display_welcome(total_questions)
    
    # Ask each question
    for i in range(len(questions)):
        score += ask_question(questions[i], i+1)
        print()  # Empty line between questions
    
    display_results(score, total_questions)

# Start the program
if __name__ == "__main__":
    main()
```

## Solution 5: Password Generator

```python
import random
import string

def display_welcome():
    """Display welcome message."""
    print("Password Generator")
    print("-----------------")

def get_password_length():
    """Get valid password length from user."""
    while True:
        try:
            length = int(input("Enter password length (8-16): "))
            if 8 <= length <= 16:
                return length
            else:
                print("Password length should be between 8 and 16 characters.")
        except ValueError:
            print("Please enter a valid number.")

def get_password_options():
    """Get password complexity options from user."""
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    include_numbers = input("Include numbers? (y/n): ").lower() == "y"
    include_symbols = input("Include symbols? (y/n): ").lower() == "y"
    
    return include_uppercase, include_numbers, include_symbols

def create_character_pool(include_uppercase, include_numbers, include_symbols):
    """Create character pool based on selected options."""
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
        include_numbers = True
    
    return characters, include_uppercase, include_numbers, include_symbols

def generate_password(length, characters, include_uppercase, include_numbers, include_symbols):
    """Generate a password with the given requirements."""
    password = ""
    for _ in range(length):
        password += random.choice(characters)

    # Ensure password meets complexity requirements
    # Check if password has at least one uppercase letter
    has_uppercase = False
    for c in password:
        if c.isupper():
            has_uppercase = True
            break
            
    # Check if password has at least one digit
    has_digit = False
    for c in password:
        if c in string.digits:
            has_digit = True
            break
            
    # Check if password has at least one symbol
    has_symbol = False
    for c in password:
        if c in string.punctuation:
            has_symbol = True
            break
    
    # Add required characters if missing
    if include_uppercase and not has_uppercase:
        password = password[:-1] + random.choice(string.ascii_uppercase)
        
    if include_numbers and not has_digit:
        password = password[:-1] + random.choice(string.digits)
        
    if include_symbols and not has_symbol:
        password = password[:-1] + random.choice(string.punctuation)
    
    return password

def evaluate_password_strength(length, include_uppercase, include_numbers, include_symbols):
    """Evaluate password strength based on complexity."""
    strength = "Weak"
    
    if length >= 12 and include_uppercase and include_numbers and include_symbols:
        strength = "Strong"
    elif length >= 10 and ((include_uppercase and include_numbers) or 
                          (include_uppercase and include_symbols) or 
                          (include_numbers and include_symbols)):
        strength = "Medium"
    
    return strength

def main():
    """Main function to control program flow."""
    display_welcome()
    
    # Get password requirements
    length = get_password_length()
    include_uppercase, include_numbers, include_symbols = get_password_options()
    
    # Create character pool
    characters, include_uppercase, include_numbers, include_symbols = create_character_pool(
        include_uppercase, include_numbers, include_symbols
    )
    
    # Generate password
    password = generate_password(
        length, characters, include_uppercase, include_numbers, include_symbols
    )
    
    # Display results
    print("\nGenerated Password:")
    print(password)
    
    # Evaluate and display password strength
    strength = evaluate_password_strength(
        length, include_uppercase, include_numbers, include_symbols
    )
    print(f"Password Strength: {strength}")
    print("\nThank you for using the Password Generator!")

# Start the program
if __name__ == "__main__":
    main()
```