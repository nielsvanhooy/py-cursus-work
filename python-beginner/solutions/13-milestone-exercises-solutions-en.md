## 1. User Registration System

### **Exercise:**
Write a program that asks the user for their name, age, and email. Validate the inputs:
- The name should not be empty.
- The age should be a number between **10 and 120**.
- The email should contain an **'@'** symbol.
- Print a confirmation message if all inputs are valid. Otherwise, print an error message.

```python
name = input("Enter your name: ").strip()
age_input = input("Enter your age: ")
email = input("Enter your email: ").strip()

if not name:
    print("Error: Name cannot be empty.")
elif not age_input.isdigit():
    print("Error: Age must be a number.")
else:
    age = int(age_input)
    if age < 10 or age > 120:
        print("Error: Age must be between 10 and 120.")
    elif '@' not in email:
        print("Error: Invalid email format.")
    else:
        print("Registration successful! Welcome,", name)
```

---

## 2. Simple Grade Categorizer

### **Exercise:**
Write a program that asks the user for a numerical grade (0–100) and categorizes it:
- 90+ → "Excellent"
- 75–89 → "Good"
- 50–74 → "Pass"
- Below 50 → "Fail"
- If the number is out of range, print an error message.

```python
grade_input = input("Enter your grade (0-100): ")

if not grade_input.isdigit():
    print("Error: Please enter a valid number.")
else:
    grade = int(grade_input)
    if grade < 0 or grade > 100:
        print("Error: Grade must be between 0 and 100.")
    elif grade >= 90:
        print("Excellent")
    elif grade >= 75:
        print("Good")
    elif grade >= 50:
        print("Pass")
    else:
        print("Fail")
```

---

## 3. Contact List Manager

### **Exercise:**
Write a program that stores up to **five names** in a list and allows the user to:
1. Manually enter five names.
2. Display the total number of contacts.
3. Search for a name in the list.
4. Remove a name from the list.

```python
contacts = []

print("Enter 5 contact names:")
contacts.append(input("Enter name 1: ").strip())
contacts.append(input("Enter name 2: ").strip())
contacts.append(input("Enter name 3: ").strip())
contacts.append(input("Enter name 4: ").strip())
contacts.append(input("Enter name 5: ").strip())

print("\nTotal contacts:", len(contacts))

search_name = input("Enter a name to search: ").strip()
if search_name in contacts:
    print("Found.")
else:
    print("Not Found.")

remove_name = input("Enter a name to remove: ").strip()
if remove_name in contacts:
    contacts.remove(remove_name)
    print("Updated contact list:", contacts)
else:
    print("Name not found in list.")
```

---

## 4. Simple Authentication System

### **Exercise:**
Write a program that prompts the user for a username and password.
- The username must be **at least 4 characters long**.
- The password must be **at least 6 characters long** and **cannot be "password" (case-insensitive)**.
- If valid, print "Login successful"; otherwise, print an error message.

```python
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

if len(username) < 4:
    print("Error: Username must be at least 4 characters long.")
elif len(password) < 6:
    print("Error: Password must be at least 6 characters long.")
elif password.lower() == "password":
    print("Error: Password cannot be 'password'.")
else:
    print("Login successful!")
```

---

