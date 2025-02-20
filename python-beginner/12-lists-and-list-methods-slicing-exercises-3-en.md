# Python List Slicing Exercises

## Basic Level

1. **Basic List Slicing**
```python
# Given: numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
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
```python
# Given: colors = ["red", "blue", "green", "yellow", "purple", "orange"]
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
```python
# Given: letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Write code to:
# - Get all letters in reverse order
# - Get every second letter in reverse order
# - Get the middle three letters (c, d, e)

# Your code below:


# Expected output:
# ['g', 'f', 'e', 'd', 'c', 'b', 'a']
# ['g', 'e', 'c', 'a']
# ['c', 'd', 'e']
```

4. **Mixed Data Slicing**
```python
# Given: mixed = [1, "A", 2, "B", 3, "C", 4, "D", 5, "E"]
# Write code to:
# - Get all numbers (using step slicing)
# - Get all letters (using step slicing)
# - Get elements from index 2 to 7 with step 2

# Your code below:


# Expected output:
# [1, 2, 3, 4, 5]
# ['A', 'B', 'C', 'D', 'E']
# [2, 3, 4]
```

## Advanced Level

5. **Nested List Slicing**
```python
# Given: matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
# Write code to:
# - Get the first two rows
# - Get the last two columns of all rows
# - Get the submatrix of elements 6,7,10,11

# Your code below:


# Expected output:
# [[1, 2, 3, 4], [5, 6, 7, 8]]
# [[3, 4], [7, 8], [11, 12], [15, 16]]
# [[6, 7], [10, 11]]
```

6. **Complex List Slicing**
```python
# Given: data = [
#     ["Jan", [1, 2, 3]],
#     ["Feb", [4, 5, 6]],
#     ["Mar", [7, 8, 9]],
#     ["Apr", [10, 11, 12]]
# ]
# Write code to:
# - Get the first two months' names only
# - Get the numbers from the last two months
# - Get the second number from each month

# Your code below:


# Expected output:
# ['Jan', 'Feb']
# [[7, 8, 9], [10, 11, 12]]
# [2, 5, 8, 11]
```

## Bonus Challenge

7. **Advanced Matrix Operations**
```python
# Given: cube = [
#     [[1, 2], [3, 4]],
#     [[5, 6], [7, 8]],
#     [[9, 10], [11, 12]]
# ]
# Write code to:
# - Get the first element of each sublist in the first two lists
# - Get the second column of each 2x2 matrix
# - Create a 2x2 matrix from the center elements (6,7,10,11)

# Your code below:


# Expected output:
# [1, 3, 5, 7]
# [[2, 4], [6, 8], [10, 12]]
# [[6, 7], [10, 11]]
```

## Practice Tips

1. Before writing code:
   - Write down what you expect the slice notation to do
   - Predict the output
   - Consider edge cases

2. Common slicing patterns:
   - `list[start:end]` - Elements from start to end-1
   - `list[start:]` - Elements from start to the end
   - `list[:end]` - Elements from beginning to end-1
   - `list[::step]` - Every step-th element
   - `list[::-1]` - Reverse the list

3. Remember:
   - Negative indices count from the end
   - The end index is exclusive
   - Step can be negative for reverse direction
   - Slicing never raises an IndexError