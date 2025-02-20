# Python List Slicing Exercises

## Basic Level

1. **Basic List Slicing**
```py
# Given: 
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Write code to:
# - Get the first four numbers
# - Get the last three numbers using negative indexing
# - Get every second number from the entire list

# Your code below:


# Expected output:
# [10, 20, 30, 40]
# [70, 80, 90]
# [10, 30, 50, 70, 90]
```

2. **Simple Slice Operations**
```py
# Given: 
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
# Write code to:
# - Get colors from index 1 to 4 (inclusive)
# - Get the last four colors using negative indexing
# - Get all colors except first and last

# Your code below:


# Expected output:
# ['blue', 'green', 'yellow', 'purple']
# ['yellow', 'purple', 'orange']
# ['blue', 'green', 'yellow', 'purple']
```

## Intermediate Level

3. **Reverse Slicing**
```py
# Given: 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Write code to:
# - Get all letters in reverse order
# - Get every second letter in reverse order
# - Get the middle three letters (c, d, e)

# Your code below:



```

4. **Mixed Data Slicing**
```py
# Given: 
mixed = [1, "A", 2, "B", 3, "C", 4, "D", 5, "E"]
# Write code to:
# - Get all numbers (using step slicing)
# - Get all letters (using step slicing)
# - Get elements from index 2 to 7 with step 2

# Your code below:


```

## Advanced Level

5. **Nested List Slicing**
```py
# Given: 
matrix = [
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 10, 11, 12],
   [13, 14, 15, 16]
]
# Write code to:
# - Get the first two rows
# - Get the last two columns of all rows
# - Get the submatrix of elements 6,7,10,11

# Your code below:



```

6. **Complex List Slicing**
```py
# Given: 
data = [
    ["Jan", [1, 2, 3]],
    ["Feb", [4, 5, 6]],
    ["Mar", [7, 8, 9]],
    ["Apr", [10, 11, 12]]
]
# Write code to:
# - Get the first two months' names only
# - Get the numbers from the last two months
# - Get the second number from each month

# Your code below:


```

## Bonus Challenge

7. **Advanced Matrix Operations**
```py
#Given: 
cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]
# Write code to:
# - Get the first element of each sublist in the first two lists
# - Get the second column of each 2x2 matrix
# - Create a 2x2 matrix from the center elements (6,7,10,11)

# Your code below:


```

## Practice Tips

Before writing code:
   - Write down what you expect the slice notation to do
   - Predict the output
   - Consider edge cases

Common slicing patterns:
   - `list[start:end]` - Elements from start to end-1
   - `list[start:]` - Elements from start to the end
   - `list[:end]` - Elements from beginning to end-1
   - `list[::step]` - Every step-th element
   - `list[::-1]` - Reverse the list

Remember:
   - Negative indices count from the end
   - The end index is exclusive
   - Step can be negative for reverse direction
   - Slicing never raises an IndexError