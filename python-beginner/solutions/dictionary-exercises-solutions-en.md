# Very Basic Dictionary Exercises - Solutions

## Exercise 1: Create and Print a Dictionary

```python
# ===== EXERCISE 1: CREATE AND PRINT A DICTIONARY =====

def fruit_colors():
    print("=== FRUIT COLORS ===")
    
    # Create a dictionary of fruits and their colors
    fruits = {"apple": "red", "banana": "yellow", "cherry": "red"}
    
    # Print the color of each fruit
    print("Apple is", fruits["apple"])
    print("Banana is", fruits["banana"])
    print("Cherry is", fruits["cherry"])
    
    print("\nDone!")
```

## Exercise 2: Add and Modify Dictionary Items

```python
# ===== EXERCISE 2: ADD AND MODIFY DICTIONARY ITEMS =====

def pet_ages():
    print("=== PET AGES ===")
    
    # Starting with a dictionary of pets and their ages
    pets = {"Rex": 3, "Fluffy": 2}
    
    # Print the starting dictionary
    print("Starting pet ages:", pets)
    
    # Add a new pet "Spot" who is 5 years old
    pets["Spot"] = 5
    
    # Change Rex's age to 4 (he had a birthday)
    pets["Rex"] = 4
    
    # Print the updated dictionary
    print("Updated pet ages:", pets)
    
    print("\nDone!")
```

## Exercise 3: Check if a Key Exists

```python
# ===== EXERCISE 3: CHECK IF KEY EXISTS =====

def check_stock():
    print("=== INVENTORY CHECKER ===")
    
    # Dictionary of items in stock
    inventory = {"apples": 10, "bananas": 5, "oranges": 8}
    
    # Ask the user what fruit they want to check
    fruit = input("What fruit do you want to check? ")
    
    # Check if the fruit is in the inventory dictionary
    if fruit in inventory:
        print(f"We have {inventory[fruit]} {fruit} in stock")
    else:
        print(f"Sorry, we don't have {fruit} in stock")
    
    print("\nDone!")
```

## Exercise 4: Loop Through a Dictionary

```python
# ===== EXERCISE 4: LOOP THROUGH A DICTIONARY =====

def print_scores():
    print("=== STUDENT SCORES ===")
    
    # Dictionary of student scores
    scores = {"Alice": 92, "Bob": 85, "Charlie": 78, "Diana": 95}
    
    # Loop through the dictionary and print each student's name and score
    for student, score in scores.items():
        print(f"{student}: {score}")
    
    # Calculate and print the average score
    total = 0
    for score in scores.values():
        total += score
    
    average = total / len(scores)
    print(f"\nAverage score: {average:.1f}")
    
    print("\nDone!")
```

## Exercise 5: Delete Items from a Dictionary

```python
# ===== EXERCISE 5: DELETE ITEMS FROM A DICTIONARY =====

def manage_contacts():
    print("=== CONTACT MANAGER ===")
    
    # Dictionary of contacts
    contacts = {"John": "555-1234", "Mary": "555-5678", "Bob": "555-4321"}
    
    # Print all contacts
    print("Current contacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
    
    # Ask the user for a name to delete
    name = input("\nEnter a name to delete: ")
    
    # Check if the name exists in the contacts
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted from contacts")
    else:
        print(f"{name} was not found in contacts")
    
    # Print the updated contacts
    print("\nUpdated contacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
    
    print("\nDone!")
```

## Exercise 6: Count Items (Slightly More Advanced)

```python
# ===== EXERCISE 6: COUNT ITEMS =====

def count_letters():
    print("=== LETTER COUNTER ===")
    
    # Get a word from the user
    word = input("Enter a word: ")
    
    # Create an empty dictionary to store letter counts
    letter_counts = {}
    
    # Loop through each letter in the word
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    
    # Print each letter and its count
    for letter, count in letter_counts.items():
        print(f"'{letter}' appears {count} time(s)")
    
    print("\nDone!")
```