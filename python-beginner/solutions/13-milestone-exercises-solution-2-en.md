## Milestone tot en met 12 - lists

## Milestone Project 1: Simple Voting System


### Project Description

Create a simple voting system where users can vote for one of three candidates. The program should:

- Ask the user to enter their name.
- Display a list of three candidates.
- Allow the user to vote by entering the candidate's name.
- Store the votes in a list.
- Display the total votes for each candidate at the end.

### Solution

```python
# Voting System
candidates = ["Alice", "Bob", "Charlie"]
votes = []

print("Welcome to the voting system!")
name = input("Enter your name: ")

print("Candidates:")
print("1. Alice\n2. Bob\n3. Charlie")

vote = input("Enter the name of the candidate you want to vote for: ")
if vote in candidates:
    votes.append(vote)
    print("Vote recorded!")
else:
    print("Invalid candidate!")

# Counting votes manually without using dictionaries
alice_votes = votes.count("Alice")
bob_votes = votes.count("Bob")
charlie_votes = votes.count("Charlie")

print("Voting Results:")
print(f"Alice: {alice_votes} votes")
print(f"Bob: {bob_votes} votes")
print(f"Charlie: {charlie_votes} votes")
```

---

## Milestone Project 2: Simple Event Registration System

### Project Description

Create an event registration system where users can:

- Enter their name.
- Choose an event from a list of three options.
- Confirm their registration.
- Display their registration details at the end.

### Solution

```python
# Event Registration System
print("Welcome to the Event Registration System!")
name = input("Enter your name: ")

print("Available Events:")
print("1. Coding Workshop")
print("2. Art Class")
print("3. Music Festival")

choice = input("Enter the number of the event you want to register for: ")

if choice == "1":
    event = "Coding Workshop"
elif choice == "2":
    event = "Art Class"
elif choice == "3":
    event = "Music Festival"
else:
    event = None
    print("Invalid selection. Please restart and choose a valid event.")

if event:
    print(f"Thank you, {name}! You have successfully registered for {event}.")
```

---

## Milestone Project 3: Basic Contact List

### Project Description

Create a basic contact list program where the user can:

- Add a new contact (name and phone number).
- View all saved contacts.
- Search for a contact by name.

### Solution

```python
# Contact List
contacts = []

print("Welcome to the Contact List Manager")
print("Options:")
print("1. Add a new contact")
print("2. View all contacts")
print("3. Search for a contact")

choice = input("Enter your choice: ")

if choice == "1":
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts.append([name, phone])
    print("Contact added successfully!")

elif choice == "2":
    print("Contact List:")
    if contacts:
        print(f"Name: {contacts[0][0]}, Phone: {contacts[0][1]}")
    else:
        print("No contacts saved yet.")

elif choice == "3":
    search_name = input("Enter name to search: ")
    if contacts and contacts[0][0].lower() == search_name.lower():
        print(f"Found: Name: {contacts[0][0]}, Phone: {contacts[0][1]}")
    else:
        print("Contact not found!")

else:
    print("Invalid option. Please try again.")
```

