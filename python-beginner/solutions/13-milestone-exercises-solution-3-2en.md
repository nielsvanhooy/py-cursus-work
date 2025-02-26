# Python Milestone Exercises - Solutions

## Exercise 1: Temperature Converter

```python
# ===== EXERCISE 1: TEMPERATURE CONVERTER =====

def temperature_converter():
    print("=== TEMPERATURE CONVERTER ===")
    print("Convert between Fahrenheit and Celsius!")
    
    continue_converting = True
    
    while continue_converting:
        # Get conversion direction
        print("\nConversion options:")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            # F to C
            try:
                temp = float(input("Enter temperature in Fahrenheit: "))
                celsius = (temp - 32) * 5/9
                print(f"{temp}°F = {celsius:.1f}°C")
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == "2":
            # C to F
            try:
                temp = float(input("Enter temperature in Celsius: "))
                fahrenheit = (temp * 9/5) + 32
                print(f"{temp}°C = {fahrenheit:.1f}°F")
            except ValueError:
                print("Please enter a valid number!")
                
        else:
            print("Invalid choice! Please enter 1 or 2.")
            continue
        
        # Ask if user wants to continue
        another = input("\nDo you want to convert another temperature? (yes/no): ").lower()
        if another != "yes" and another != "y":
            continue_converting = False
    
    print("Thank you for using Temperature Converter!")
```

## Exercise 2: Word Counter

```python
# ===== EXERCISE 2: WORD COUNTER =====

def word_counter():
    print("=== WORD COUNTER ===")
    print("Analyze text to count words and characters!")
    
    analyze_again = True
    
    while analyze_again:
        # Get text from user
        text = input("\nEnter a sentence or paragraph to analyze: ")
        
        if text == "":
            print("Please enter some text to analyze!")
            continue
        
        # Count characters (including spaces)
        char_count = len(text)
        
        # Count words
        words = text.split()
        word_count = len(words)
        
        # Calculate average word length
        if word_count > 0:
            total_word_length = 0
            for word in words:
                total_word_length += len(word)
            avg_word_length = total_word_length / word_count
        else:
            avg_word_length = 0
        
        # Display results
        print("\nText Analysis Results:")
        print(f"Character count: {char_count}")
        print(f"Word count: {word_count}")
        print(f"Average word length: {avg_word_length:.1f} characters")
        
        # Ask to analyze again
        choice = input("\nWould you like to analyze another text? (yes/no): ").lower()
        if choice != "yes" and choice != "y":
            analyze_again = False
    
    print("Thank you for using Word Counter!")
```

## Exercise 4: To-Do List Manager

```python
# ===== EXERCISE 4: TO-DO LIST MANAGER =====

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
            # Add new task
            task = input("Enter task description: ")
            if task == "":
                print("Task description cannot be empty!")
                continue
            
            # Get priority (1=High, 2=Medium, 3=Low)
            priority = input("Enter priority (1=High, 2=Medium, 3=Low): ")
            if priority not in ["1", "2", "3"]:
                print("Invalid priority! Using Medium (2) as default.")
                priority = "2"
            
            # Convert priority to text
            priority_text = ["High", "Medium", "Low"][int(priority) - 1]
            
            # Add to list (not completed by default)
            todos.append([task, priority_text, False])
            print(f"Added: {task} (Priority: {priority_text})")
                
        elif choice == "2":
            # View all tasks
            if len(todos) == 0:
                print("To-do list is empty!")
            else:
                print("\nAll Tasks:")
                print("ID | Priority | Status     | Task")
                print("---|----------|------------|-------------")
                
                # Sort by priority (High first, then Medium, then Low)
                sorted_todos = sorted(todos, key=lambda x: ["High", "Medium", "Low"].index(x[1]))
                
                for i, todo in enumerate(sorted_todos):
                    status = "Completed" if todo[2] else "Pending"
                    print(f"{i+1:2} | {todo[1]:8} | {status:10} | {todo[0]}")
                    
        elif choice == "3":
            # View by completion status
            if len(todos) == 0:
                print("To-do list is empty!")
                continue
                
            status_choice = input("View (1) Completed or (2) Pending tasks? ")
            
            if status_choice == "1":
                # Show completed tasks
                completed_tasks = [t for t in todos if t[2]]
                if len(completed_tasks) == 0:
                    print("No completed tasks!")
                else:
                    print("\nCompleted Tasks:")
                    for i, todo in enumerate(completed_tasks):
                        print(f"{i+1}. {todo[0]} (Priority: {todo[1]})")
                        
            elif status_choice == "2":
                # Show pending tasks
                pending_tasks = [t for t in todos if not t[2]]
                if len(pending_tasks) == 0:
                    print("No pending tasks!")
                else:
                    print("\nPending Tasks:")
                    for i, todo in enumerate(pending_tasks):
                        print(f"{i+1}. {todo[0]} (Priority: {todo[1]})")
            else:
                print("Invalid choice!")
                    
        elif choice == "4":
            # Mark task as completed
            if len(todos) == 0:
                print("To-do list is empty!")
                continue
                
            # Show pending tasks
            pending_tasks = [t for t in todos if not t[2]]
            if len(pending_tasks) == 0:
                print("No pending tasks!")
                continue
                
            print("\nPending Tasks:")
            for i, todo in enumerate(pending_tasks):
                print(f"{i+1}. {todo[0]} (Priority: {todo[1]})")
                
            try:
                task_num = int(input("\nEnter the number of the task to mark as completed: "))
                if 1 <= task_num <= len(pending_tasks):
                    # Find the task in the original list
                    task_to_complete = pending_tasks[task_num-1]
                    for todo in todos:
                        if todo == task_to_complete:
                            todo[2] = True
                            print(f"Marked '{todo[0]}' as completed!")
                            break
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")
                    
        elif choice == "5":
            # Exit
            print("Thank you for using the To-Do List Manager. Goodbye!")
            break
            
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
```

## Exercise 5: Simple Quiz Game

```python
# ===== EXERCISE 5: SIMPLE QUIZ GAME =====

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
    
    # Initialize score
    score = 0
    
    # Loop through questions
    for i, question_data in enumerate(quiz_questions):
        question = question_data[0]
        options = question_data[1]
        correct_index = question_data[2]
        
        # Display question and options
        print(f"\nQuestion {i+1}: {question}")
        for j, option in enumerate(options):
            print(f"{j+1}. {option}")
            
        # Get user's answer
        while True:
            try:
                answer = int(input("Enter your answer (number): "))
                if 1 <= answer <= len(options):
                    break
                else:
                    print(f"Please enter a number between 1 and {len(options)}!")
            except ValueError:
                print("Please enter a valid number!")
        
        # Check if answer is correct
        if answer - 1 == correct_index:  # Convert from 1-based to 0-based indexing
            print("Correct!")
            score += 1
        else:
            correct_option = options[correct_index]
            print(f"Incorrect! The correct answer is: {correct_option}")
    
    # Display final score
    percentage = (score / len(quiz_questions)) * 100
    print(f"\nQuiz complete! Your score: {score}/{len(quiz_questions)} ({percentage:.1f}%)")
    
    # Give feedback based on score
    if percentage >= 80:
        print("Excellent job!")
    elif percentage >= 60:
        print("Good job!")
    else:
        print("Keep practicing!")
```

## Exercise 6: Hangman Game

```python
# ===== EXERCISE 6: HANGMAN GAME =====

def hangman():
    # List of words to choose from
    words = ["python", "programming", "computer", "keyboard", "developer", 
             "learning", "algorithm", "variable", "condition", "function"]
    
    # Import random module for word selection
    import random
    
    # Select a random word
    word = random.choice(words)
    
    # Track guessed letters
    guessed_letters = []
    
    # Maximum wrong guesses allowed
    max_wrong_guesses = 6
    wrong_guesses = 0
    
    print("=== HANGMAN GAME ===")
    print(f"Guess the word! You can make {max_wrong_guesses} wrong guesses.")
    
    # Game loop
    while wrong_guesses < max_wrong_guesses:
        # Display word with guessed letters
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong_guesses}")
        
        # Check if word is complete
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
        
        # Get player's guess
        guess = input("\nEnter a letter: ").lower()
        
        # Validate input
        if len(guess) != 1:
            print("Please enter exactly one letter!")
            continue
        
        if not guess.isalpha():
            print("Please enter a letter!")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        # Add to guessed letters
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            wrong_guesses += 1
    
    # Check if player lost
    if wrong_guesses >= max_wrong_guesses:
        print(f"\nGame over! The word was: {word}")
    
    print("Thanks for playing Hangman!")
```

## Exercise 7: Tic-Tac-Toe Game

```python
# ===== EXERCISE 7: TIC-TAC-TOE GAME =====

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
        game_over = False
        
        # Game loop
        while not game_over:
            # Display the board
            print("\nCurrent board:")
            print("  1 2 3")
            for i in range(3):
                print(f"{i+1} {board[i][0]}|{board[i][1]}|{board[i][2]}")
                if i < 2:
                    print("  -+-+-")
            
            # Get player's move
            print(f"\nPlayer {current_player}'s turn")
            
            while True:
                try:
                    row = int(input("Enter row (1-3): ")) - 1
                    col = int(input("Enter column (1-3): ")) - 1
                    
                    # Check if input is valid
                    if not (0 <= row <= 2 and 0 <= col <= 2):
                        print("Row and column must be between 1 and 3!")
                        continue
                    
                    # Check if position is empty
                    if board[row][col] != " ":
                        print("That position is already taken!")
                        continue
                    
                    break
                    
                except ValueError:
                    print("Please enter valid numbers!")
            
            # Make the move
            board[row][col] = current_player
            
            # Check for win
            # Check rows
            for i in range(3):
                if board[i][0] == board[i][1] == board[i][2] != " ":
                    print(f"\nPlayer {current_player} wins!")
                    game_over = True
                    break
            
            # Check columns
            if not game_over:
                for i in range(3):
                    if board[0][i] == board[1][i] == board[2][i] != " ":
                        print(f"\nPlayer {current_player} wins!")
                        game_over = True
                        break
            
            # Check diagonals
            if not game_over:
                if board[0][0] == board[1][1] == board[2][2] != " " or \
                   board[0][2] == board[1][1] == board[2][0] != " ":
                    print(f"\nPlayer {current_player} wins!")
                    game_over = True
            
            # Check for draw (board is full)
            if not game_over:
                is_full = True
                for row in board:
                    if " " in row:
                        is_full = False
                        break
                
                if is_full:
                    print("\nIt's a draw!")
                    game_over = True
            
            # Switch player if game is not over
            if not game_over:
                current_player = "O" if current_player == "X" else "X"
        
        # Display final board
        print("\nFinal board:")
        print("  1 2 3")
        for i in range(3):
            print(f"{i+1} {board[i][0]}|{board[i][1]}|{board[i][2]}")
            if i < 2:
                print("  -+-+-")
        
        # Ask to play again
        choice = input("\nDo you want to play again? (yes/no): ").lower()
        if choice != "yes" and choice != "y":
            play_again = False
    
    print("Thanks for playing Tic-Tac-Toe!")
```