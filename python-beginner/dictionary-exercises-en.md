# Very Basic Dictionary Exercises

These exercises focus on the most fundamental dictionary operations in Python. Each exercise practices just one or two simple dictionary concepts.

## Exercise 1: Create and Print a Dictionary

Practice creating a dictionary and accessing its values.

```python
# ===== EXERCISE 1: CREATE AND PRINT A DICTIONARY =====

def fruit_colors():
    print("=== FRUIT COLORS ===")
    
    # TODO: Create a dictionary where:
    # - Keys are fruit names: "apple", "banana", "cherry"
    # - Values are their colors: "red", "yellow", "red"
    # Example: fruits = {"apple": "red", "banana": "yellow", "cherry": "red"}
    
    # TODO: Print the color of each fruit
    # Example:
    # print("Apple is", fruits["apple"])
    # print("Banana is", fruits["banana"])
    # print("Cherry is", fruits["cherry"])
    
    print("\nDone!")

# Run this program by removing the comment symbol (#) from the line below
# fruit_colors()
```

## Exercise 2: Add and Modify Dictionary Items

Practice adding new key-value pairs and changing existing values.

```python
# ===== EXERCISE 2: ADD AND MODIFY DICTIONARY ITEMS =====

def pet_ages():
    print("=== PET AGES ===")
    
    # Starting with a dictionary of pets and their ages
    pets = {"Rex": 3, "Fluffy": 2}
    
    # Print the starting dictionary
    print("Starting pet ages:", pets)
    
    # TODO: Add a new pet "Spot" who is 5 years old to the dictionary
    
    # TODO: Change Rex's age to 4 (he had a birthday)
    
    # Print the updated dictionary
    print("Updated pet ages:", pets)
    
    print("\nDone!")

# Run this program by removing the comment symbol (#) from the line below
# pet_ages()
```

## Exercise 3: Check if a Key Exists

Practice checking if a key is in a dictionary.

```python
# ===== EXERCISE 3: CHECK IF KEY EXISTS =====

def check_stock():
    print("=== INVENTORY CHECKER ===")
    
    # Dictionary of items in stock
    inventory = {"apples": 10, "bananas": 5, "oranges": 8}
    
    # TODO: Ask the user what fruit they want to check
    # Example: fruit = input("What fruit do you want to check? ")
    
    # TODO: Check if the fruit is in the inventory dictionary
    # If it is, print how many are in stock
    # If not, print that the fruit is not in stock
    # Example:
    # if fruit in inventory:
    #     print(f"We have {inventory[fruit]} {fruit} in stock")
    # else:
    #     print(f"Sorry, we don't have {fruit} in stock")
    
    print("\nDone!")

# Run this program by removing the comment symbol (#) from the line below
# check_stock()
```

## Exercise 4: Loop Through a Dictionary

Practice using a loop to go through all keys and values in a dictionary.

```python
# ===== EXERCISE 4: LOOP THROUGH A DICTIONARY =====

def print_scores():
    print("=== STUDENT SCORES ===")
    
    # Dictionary of student scores
    scores = {"Alice": 92, "Bob": 85, "Charlie": 78, "Diana": 95}
    
    # TODO: Loop through the dictionary and print each student's name and score
    # Example:
    # for student, score in scores.items():
    #     print(f"{student}: {score}")
    
    # TODO: Calculate and print the average score
    # Hint: Use a variable to keep track of the total, then divide by the number of students
    
    print("\nDone!")

# Run this program by removing the comment symbol (#) from the line below
# print_scores()
```

## Exercise 5: Delete Items from a Dictionary

Practice removing items from a dictionary.

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
    
    # TODO: Ask the user for a name to delete
    # Example: name = input("\nEnter a name to delete: ")
    
    # TODO: Check if the name exists in the contacts
    # If it does, delete it and print a success message
    # If not, print that the contact wasn't found
    # Hint: Use the 'del' keyword to delete a dictionary item
    
    # Print the updated contacts
    print("\nUpdated contacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
    
    print("\nDone!")

# Run this program by removing the comment symbol (#) from the line below
# manage_contacts()
```

## Exercise 6: Count Items (Slightly More Advanced)

Practice counting items by storing counts in a dictionary.

```python
# ===== EXERCISE 6: COUNT ITEMS =====

def count_letters():
    print("=== LETTER COUNTER ===")
    
    # Get a word from the user
    word = input("Enter a word: ")
    
    # TODO: Create an empty dictionary to store letter counts
    # Example: letter_counts = {}
    
    # TODO: Loop through each letter in the word
    # For each letter, if it's already in the dictionary, add 1 to its count
    # If it's not in the dictionary yet, set its count to 1
    # Example:
    # for letter in word:
    #     if letter in letter_counts:
    #         letter_counts[letter] += 1
    #     else:
    #         letter_counts[letter] = 1
    
    # TODO: Print each letter and its count
    # Example:
    # for letter, count in letter_counts.items():
    #     print(f"'{letter}' appears {count} time(s)")
    
    print("\nDone!")

# Run this program by removing the comment symbol (#) from the line below
# count_letters()
```

## Dictionary Tips

- A dictionary is created with curly braces `{}` and consists of key-value pairs
- Each key-value pair is written as `key: value`
- Access a value using square brackets and the key: `dict_name[key]`
- Add a new item or change an existing item with: `dict_name[key] = value`
- Check if a key exists with: `if key in dict_name:`
- Loop through a dictionary with:
  ```python
  for key in dict_name:
      # Do something with key and dict_name[key]
  ```
  or
  ```python
  for key, value in dict_name.items():
      # Do something with key and value
  ```
- Delete an item with: `del dict_name[key]`