# Python Exercises

## Basic Exercises

### 1. Create a Shopping List
- Create a list of items you want to buy. 
- Then, write a for loop to print out each item in the shopping list one by one. 
- Add a check to see if an item is in your list (for example, "milk") 
- and print "I already have milk!" if it's there.

**Solution:**
```python
shopping_list = ['bread', 'milk', 'eggs', 'butter', 'cheese']

for item in shopping_list:
    if item == 'milk':
        print("I already have milk!")
    else:
        print(f"Next item: {item}")
```

### 2. Favorite Movies List
- Create a list of your favorite movies. 
- Write a for loop to print a message for each movie, 
- like: "I love watching movie name." 
- Modify the loop to print a special message for one movie (e.g., "The Lion King" should print "This is my all-time favorite movie!").

**Solution:**
```python
movies = ['Inception', 'The Lion King', 'Avatar', 'The Matrix']

for movie in movies:
    if movie == 'The Lion King':
        print(f"{movie}: This is my all-time favorite movie!")
    else:
        print(f"I love watching {movie}.")
```

### 3. User-generated list

# this one is harder and will need something like range() to work

- Ask the user to enter 5 items into a list using the input() function. 
- Then, print each item entered by the user in a nice format using a for loop.

**Solution:**
```python
user_items = []
for _ in range(5):
    item = input("Enter an item: ")
    user_items.append(item)

for item in user_items:
    print(f"You entered: {item}")
```

## Intermediate Exercises

### 4. Pet list

- Create a list of pets. 
- Use a for loop to print each pet’s name. 
- Then, write a part of the program that asks the user for a pet's name and checks if that pet is in the list (using `in`).

**Solution:**
```python
pets = ['dog', 'cat', 'hamster', 'parrot']

for pet in pets:
    print(pet)

user_pet = input("Enter the name of a pet: ")
if user_pet in pets:
    print(f"{user_pet} is in the list!")
else:
    print(f"{user_pet} is not in the list.")
```


### 5. Guess the word

# hint: you need to :  import random   for this  (google for how to random something in python)

- Write a program where the computer randomly selects a word from a list of animals (e.g., "cat", "dog", "elephant"). 
- The user has to guess the word. 
- Each time the user guesses wrong, the program should print a hint (for example, the first letter of the word) and let them try again.

**Solution:**
```python
import random

animals = ['cat', 'dog', 'elephant', 'lion']
selected_animal = random.choice(animals)

guess = ""
while guess != selected_animal:
    guess = input("Guess the animal: ")
    if guess != selected_animal:
        print(f"Hint: The word starts with {selected_animal[0]}")
    
print(f"Congrats! You guessed the right word: {selected_animal}")
```