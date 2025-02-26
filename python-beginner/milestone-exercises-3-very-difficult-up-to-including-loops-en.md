# Python Milestone Exercises

These exercises are designed to practice the Python concepts you've learned so far, including:
- Variables and data types
- Conditional statements (if/elif/else)
- Logical operators (and, or, not)
- Lists and list operations
- Lists of lists
- Loops (while and for)
- Input/output
- String manipulation

Each exercise builds upon the previous ones and increases slightly in difficulty.

---
## Note these exercises can be really hard. The intention of these is to eventually be able to complete them.
## If you can complete them. you will have mastery over the basics of python.

## I think most will make it to exercise 3. for now. (we will get back later to them)
---

## Exercise 1: Temperature Converter

### Instructions:
Create a program that converts temperatures between Fahrenheit and Celsius.
1. Ask the user to choose conversion direction (F to C or C to F)
2. Ask for the temperature to convert
3. Display the converted temperature
4. Ask if they want to convert another temperature

### Conversion Formulas:
- Fahrenheit to Celsius: `C = (F - 32) * 5/9`
- Celsius to Fahrenheit: `F = (C * 9/5) + 32`

### Starter Code:
```python
# ===== EXERCISE 1: TEMPERATURE CONVERTER =====


print("=== TEMPERATURE CONVERTER ===")
print("Convert between Fahrenheit and Celsius!")

continue_converting = True

while continue_converting:
   # Get conversion direction
   print("\nConversion options:")
   print("1. Fahrenheit to Celsius")
   print("2. Celsius to Fahrenheit")
   
   # TODO: Check the user's choice and perform the appropriate conversion
   # ask for input
   # Remember to handle invalid input!
   
   # TODO: Ask if the user wants to convert another temperature
   # Set continue_converting to False if they don't

print("Thank you for using Temperature Converter!")

```

## Exercise 2: Word Counter

### Instructions:
Create a program that analyzes text input.
1. Ask the user to enter a sentence or paragraph
2. Count and display:
   - Total number of characters
   - Total number of words
   - Average word length
3. Ask if they want to analyze another text

### Hints:
- Use `len()` to count characters
- Use `string.split()` to split text into words
- Calculate average word length by dividing total character count (excluding spaces) by word count

### Starter Code:
```python
# ===== EXERCISE 2: WORD COUNTER =====


print("=== WORD COUNTER ===")
print("Analyze text to count words and characters!")
 
analyze_again = True
 
while analyze_again:
   # Get text from user
   text = input("\nEnter a sentence or paragraph to analyze: ")
   
   if text == "":
     print("Please enter some text to analyze!")
     continue
   
   # TODO: Count the total number of characters
   
   # TODO: Count the number of words
   
   # TODO: Calculate the average word length
   
   # TODO: Display the results
   
   # TODO: Ask if the user wants to analyze another text
   # Set analyze_again to False if they don't
 
print("Thank you for using Word Counter!")

```

## Exercise 3: To-Do List Manager

### Instructions:
Create a program that manages a simple to-do list.
1. Display a menu with options
2. Allow the user to add tasks with priority levels
3. View tasks sorted by priority
4. Mark tasks as completed
5. View only completed or uncompleted tasks

### Hints:
- Use a list of lists to store tasks: `[task_description, priority, completed]`
- For priority, use "High", "Medium", or "Low"
- For completed status, use a boolean value (True/False)
- Use the `sorted()` function with a key to sort tasks by priority

### Starter Code:
```python
# ===== EXERCISE 3: TO-DO LIST MANAGER =====

def todo_manager():
    # Initialize empty to-do list
    # Format: [task, priority, completed]
    todos = []
    
    print("=== TO-DO LIST MANAGER ===")
    print("Keep track of your tasks and priorities!")
    
    while True:
        # Display menu
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. View by completion status")
        print("4. Mark task as completed")
        print("5. Exit")
        
        # Get user choice
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            # TODO: Add a new task
            # Ask for task description and priority
            # Add the task to the todos list
            pass
                
        elif choice == "2":
            # TODO: View all tasks
            # Display tasks sorted by priority
            pass
                    
        elif choice == "3":
            # TODO: View by completion status
            # Ask the user whether to view completed or pending tasks
            # Display the appropriate tasks
            pass
                    
        elif choice == "4":
            # TODO: Mark task as completed
            # Show pending tasks
            # Ask user which task to mark as completed
            pass
                    
        elif choice == "5":
            # TODO: Exit the program
            pass
            
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

# Run this program by removing the comment symbol (#) from the line below
# todo_manager()
```

## Exercise 4: Simple Quiz Game

### Instructions:
Create a simple quiz game with multiple-choice questions.
1. Store questions, options, and answers in a list of lists
2. Present questions to the user
3. Check their answers and keep score
4. Display final score and percentage

### Hints:
- Format each question as: `[question_text, [options], correct_answer_index]`
- Remember that list indices start at 0, but users will enter 1-based answers

### Starter Code:
```python
# ===== EXERCISE 4: SIMPLE QUIZ GAME =====

def quiz_game():
    # Quiz questions format: [question, [options], correct_answer_index]
    quiz_questions = [
        ["What is the capital of France?", 
         ["London", "Berlin", "Paris", "Madrid"], 
         2],  # Index 2 is Paris
         
        ["Which planet is known as the Red Planet?", 
         ["Venus", "Mars", "Jupiter", "Saturn"], 
         1],  # Index 1 is Mars
         
        ["Which of these is NOT a programming language?", 
         ["Python", "Java", "HTML", "Cobra"], 
         3],  # Index 3 is Cobra
         
        ["What does CPU stand for?", 
         ["Central Processing Unit", "Computer Personal Unit", 
          "Central Processor Utility", "Central Program Unit"], 
         0]   # Index 0 is Central Processing Unit
    ]
    
    print("=== SIMPLE QUIZ GAME ===")
    print(f"This quiz has {len(quiz_questions)} multiple-choice questions.")
    print("Let's see how well you do!")
    
    # TODO: Initialize score
    
    # TODO: Loop through questions
    # Display each question and its options
    # Get the user's answer
    # Check if the answer is correct and update the score
    
    # TODO: Display final score and percentage
    # Give feedback based on score

# Run this program by removing the comment symbol (#) from the line below
# quiz_game()
```

## Exercise 5: Hangman Game

### Instructions:
Create a simple Hangman game where:
1. The program selects a random word from a predefined list
2. The player tries to guess the word one letter at a time
3. The program keeps track of correct and incorrect guesses
4. The player has a limited number of wrong guesses

### Hints:
- Use the `random` module to select a random word
- Use a list to keep track of guessed letters
- Use a loop to check each letter of the word

### Starter Code:
```python
# ===== EXERCISE 5: HANGMAN GAME =====

def hangman():
    # List of words to choose from
    words = ["python", "programming", "computer", "keyboard", "developer", 
             "learning", "algorithm", "variable", "condition", "function"]
    
    # Import random module for word selection
    import random
    
    # TODO: Select a random word from the list
    
    # TODO: Initialize variables to track guessed letters and wrong guesses
    
    print("=== HANGMAN GAME ===")
    print("Guess the word! You can make 6 wrong guesses.")
    
    # TODO: Implement the game loop
    # Display the word with guessed letters
    # Get the player's guess
    # Check if the guess is correct
    # Update wrong guesses count if needed
    # Check for win/loss conditions
    
    print("Thanks for playing Hangman!")

# Run this program by removing the comment symbol (#) from the line below
# hangman()
```

## Exercise 6: Tic-Tac-Toe Game

### Instructions:
Create a two-player Tic-Tac-Toe game where:
1. The game board is displayed as a 3x3 grid
2. Two players take turns placing X and O
3. The program checks for wins and draws
4. Players can play multiple rounds

### Hints:
- Use a list of lists to represent the 3x3 board
- Remember to check for horizontal, vertical, and diagonal wins
- Keep track of whose turn it is

### Starter Code:
```python
# ===== EXERCISE 6: TIC-TAC-TOE GAME =====

def tic_tac_toe():
    print("=== TIC-TAC-TOE GAME ===")
    print("Two players take turns placing X and O on the board.")
    
    play_again = True
    
    while play_again:
        # Initialize empty 3x3 board
        # Use list of lists, each position contains " ", "X", or "O"
        board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        
        # Track current player (X goes first)
        current_player = "X"
        
        # TODO: Implement the game loop
        # Display the current board
        # Get the current player's move
        # Update the board
        # Check for win conditions
        # Check for a draw
        # Switch to the other player
        
        # TODO: Ask if players want to play again
        # Set play_again to False if they don't
    
    print("Thanks for playing Tic-Tac-Toe!")

# Run this program by removing the comment symbol (#) from the line below
# tic_tac_toe()
```

## Challenge Ideas

Once you've completed the exercises, try extending them with these challenges:

1. **Temperature Converter**: Add Kelvin as a third temperature unit.

2. **Word Counter**: Count the number of sentences and paragraphs in the text.

3. **To-Do List Manager**: Add due dates to tasks and sort by date.

4. **Quiz Game**: Add a timer for each question.

5. **Hangman Game**: Add difficulty levels with different word lists.

6. **Tic-Tac-Toe**: Create a simple computer opponent that makes random moves.