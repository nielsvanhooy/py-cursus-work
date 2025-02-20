# Python Exercises

## Basic Exercises with if/elif/else, Boolean Conditions, Indexing, and Lists of Lists

### 1. Fruit Color Finder
- **Task:** Create a list of fruits and their colors (list of lists). Use a for loop to print the color of each fruit. If the fruit is not in the list, print a message: "Sorry, I don't know that fruit."

**Solution:**
```python
fruits = [['apple', 'red'], ['banana', 'yellow'], ['grape', 'purple'], ['orange', 'orange']]

fruit_to_find = input("Enter a fruit name: ").lower()

found = False
for fruit in fruits:
    if fruit[0] == fruit_to_find:
        print(f"The color of {fruit[0]} is {fruit[1]}.")
        found = True
        break

if not found:
    print("Sorry, I don't know that fruit.")
```

### 2. Weather Checker
- **Task:** Create a list of weather conditions (e.g., sunny, rainy, snowy, etc.). Ask the user to enter today's weather, and print a message based on the weather. Use `if/elif/else` to provide different messages depending on whether the weather is sunny, rainy, or snowy.

**Solution:**
```python
weather = input("What's the weather like today (sunny, rainy, snowy)? ").lower()

if weather == 'sunny':
    print("It's a great day to go outside!")
elif weather == 'rainy':
    print("Don't forget your umbrella!")
elif weather == 'snowy':
    print("Stay warm and enjoy the snow!")
else:
    print("I don't know that weather condition.")
```

### 3. Favorite Foods with Boolean Conditions
- **Task:** Create a list of your favorite foods and ask the user to enter a food item. Use a boolean condition to check if the food item is in your list and print a message saying whether or not it's a favorite food.

**Solution:**
```python
favorite_foods = ['pizza', 'pasta', 'ice cream', 'sushi']

user_food = input("Enter your favorite food: ").lower()

if user_food in favorite_foods:
    print(f"Yum! {user_food} is one of my favorite foods too!")
else:
    print(f"{user_food} is not one of my favorites, but it sounds delicious!")
```

### 4. Find the Index of a Fruit
- **Task:** Create a list of fruits. Ask the user to enter a fruit's name and use indexing to print the index of that fruit in the list. If the fruit is not found, print a message saying "Fruit not found."

**Solution:**
```python
fruits = ['apple', 'banana', 'grape', 'orange']

user_fruit = input("Enter a fruit name: ").lower()

if user_fruit in fruits:
    index = fruits.index(user_fruit)
    print(f"The index of {user_fruit} is {index}.")
else:
    print("Fruit not found.")
```

### 5. Nested Lists – Classroom Roll Call
- **Task:** Create a list of lists where each sublist contains the name of a student and their grade. Ask the user for a student's name and print the grade for that student. If the student is not found, print a message saying "Student not found."

**Solution:**
```python
students = [['Alice', 'A'], ['Bob', 'B'], ['Charlie', 'C'], ['David', 'A']]

student_name = input("Enter a student's name: ").capitalize()

found = False
for student in students:
    if student[0] == student_name:
        print(f"{student_name}'s grade is {student[1]}.")
        found = True
        break

if not found:
    print("Student not found.")
```

## Intermediate Exercises with if/elif/else, Boolean Conditions, Indexing, and Lists of Lists

### 1. Library Book Search
- **Task:** Create a list of lists where each sublist contains a book title and its availability (True or False). Ask the user to input a book title and check if the book is available. Print a message saying whether the book is available or not.

**Solution:**
```python
library_books = [['Harry Potter', True], ['The Hobbit', False], ['1984', True], ['To Kill a Mockingbird', False]]

book_title = input("Enter the book title: ").title()

found = False
for book in library_books:
    if book[0] == book_title:
        if book[1]:
            print(f"{book_title} is available.")
        else:
            print(f"{book_title} is currently not available.")
        found = True
        break

if not found:
    print("Book not found.")
```

### 2. Nested List Comparison
- **Task:** Create two lists of lists. The first list contains student names, and the second list contains their corresponding scores. Use a for loop and `if/elif/else` to compare each student's score to a passing grade (e.g., 60). Print a message for each student saying whether they passed or failed.

**Solution:**
```python
students = [['Alice', 85], ['Bob', 55], ['Charlie', 75], ['David', 45]]
passing_grade = 60

for student in students:
    if student[1] >= passing_grade:
        print(f"{student[0]} passed with a score of {student[1]}.")
    else:
        print(f"{student[0]} failed with a score of {student[1]}.")
```

---

### Notes:
These exercises engage your students with more complex real-life scenarios, helping them practice key Python concepts such as conditions, indexing, and working with nested lists. They also introduce boolean logic, making the exercises more interactive!
```

You can now copy and paste this full markdown file!