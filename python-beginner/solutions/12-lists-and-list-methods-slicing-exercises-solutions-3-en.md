# Python List Slicing Exercise Solutions

## Basic Level Solutions

1. **Basic List Slicing**
```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Get the first four numbers
solution1 = numbers[:4]  # [10, 20, 30, 40]

# Get the last three numbers using negative indexing
solution2 = numbers[-3:]  # [70, 80, 90]

# Get every second number from the entire list
solution3 = numbers[::2]  # [10, 30, 50, 70, 90]
```

2. **Simple Slice Operations**
```python
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# Get colors from index 1 to 4 (inclusive)
solution1 = colors[1:5]  # ['blue', 'green', 'yellow', 'purple']

# Get the last four colors using negative indexing
solution2 = colors[-4:]  # ['yellow', 'purple', 'orange']

# Get all colors except first and last
solution3 = colors[1:-1]  # ['blue', 'green', 'yellow', 'purple']
```

## Intermediate Level Solutions

3. **Reverse Slicing**
```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Get all letters in reverse order
solution1 = letters[::-1]  # ['g', 'f', 'e', 'd', 'c', 'b', 'a']

# Get every second letter in reverse order
solution2 = letters[::-2]  # ['g', 'e', 'c', 'a']

# Get the middle three letters
solution3 = letters[2:5]  # ['c', 'd', 'e']
```

4. **Mixed Data Slicing**
```python
mixed = [1, "A", 2, "B", 3, "C", 4, "D", 5, "E"]

# Get all numbers (using step slicing)
solution1 = mixed[::2]  # [1, 2, 3, 4, 5]

# Get all letters (using step slicing)
solution2 = mixed[1::2]  # ['A', 'B', 'C', 'D', 'E']

# Get elements from index 2 to 7 with step 2
solution3 = mixed[2:8:2]  # [2, 3, 4]
```

## Advanced Level Solutions

5. **Nested List Slicing**
```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Get the first two rows
solution1 = matrix[:2]  # [[1, 2, 3, 4], [5, 6, 7, 8]]

# Get the last two columns of all rows
solution2 = [row[2:] for row in matrix]  # [[3, 4], [7, 8], [11, 12], [15, 16]]

# Get the submatrix of elements 6,7,10,11
solution3 = [row[1:3] for row in matrix[1:3]]  # [[6, 7], [10, 11]]
```

6. **Complex List Slicing**
```python
data = [
    ["Jan", [1, 2, 3]],
    ["Feb", [4, 5, 6]],
    ["Mar", [7, 8, 9]],
    ["Apr", [10, 11, 12]]
]

# Get the first two months' names only
solution1 = [month[0] for month in data[:2]]  # ['Jan', 'Feb']

# Get the numbers from the last two months
solution2 = [month[1] for month in data[-2:]]  # [[7, 8, 9], [10, 11, 12]]

# Get the second number from each month
solution3 = [month[1][1] for month in data]  # [2, 5, 8, 11]
```

## Bonus Challenge Solution

7. **Advanced Matrix Operations**
```python
cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]

# Get the first element of each sublist in the first two lists
solution1 = [sublist[0] for matrix in cube[:2] for sublist in matrix]  # [1, 3, 5, 7]

# Get the second column of each 2x2 matrix
solution2 = [[row[1] for row in matrix] for matrix in cube]  # [[2, 4], [6, 8], [10, 12]]

# Create a 2x2 matrix from the center elements
solution3 = [
    [cube[1][0][1], cube[1][1][0]],  # [6, 7]
    [cube[2][0][0], cube[2][0][1]]   # [10, 11]
]
```

## Key Concepts to Remember

1. **Slice Syntax Components**:
   - `list[start:end:step]`
   - All components are optional
   - Negative indices count from end
   - Step determines direction and skip count

2. **Common Patterns**:
   - `list[:]` - Full copy of list
   - `list[::-1]` - Reverse list
   - `list[::2]` - Every second element
   - `list[-3:]` - Last three elements
   - `list[:-1]` - All except last element

3. **Nested List Tips**:
   - Combine slicing with list comprehension for powerful operations
   - Break complex operations into smaller steps
   - Use multiple lines for better readability
   - Test with smaller examples first

4. **Best Practices**:
   - Always consider edge cases
   - Use meaningful variable names
   - Comment complex slicing operations
   - Test with different input sizes