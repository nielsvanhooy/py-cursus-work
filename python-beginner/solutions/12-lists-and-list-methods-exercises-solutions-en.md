# Python List Exercises
## Basic Level

1. **List Creation and Access**
```py
# Create a list called 'fruits' with these items: "apple", "banana", "orange", "grape", "mango"
# Then write code to:
# - Print the first fruit
# - Print the last fruit using negative indexing
# - Print the length of the list

# Solution:
fruits = ["apple", "banana", "orange", "grape", "mango"]
print(fruits[0])      # Should print: apple
print(fruits[-1])     # Should print: mango
print(len(fruits))    # Should print: 5
```

2. **List Slicing Basics**
```py
numbers = [10, 20, 30, 40, 50, 60, 70]
# Write code to:
# - Get the first three numbers
# - Get the last three numbers using negative indexing
# - Get every second number starting from index 0

# Solution:
first_three = numbers[0:3]    # Should be: [10, 20, 30]
last_three = numbers[-3:]     # Should be: [50, 60, 70]
every_second = numbers[::2]   # Should be: [10, 30, 50, 70]
```

3. **Simple List Lookup**
```py
animals = ["dog", "cat", "bird", "fish", "hamster"]
# Write code to:
# - Print the middle animal (index 2)
# - Print the second-to-last animal using negative indexing
# - Check if "cat" is in the list

# Solution:
print(animals[2])       # Should print: bird
print(animals[-2])      # Should print: fish
has_cat = "cat" in animals    # Should be: True
```

4. **Basic List Measurements**
```py
scores = [95, 89, 78, 92, 85]
# Write code to:
# - Print how many scores are in the list
# - Print the first and last score together
# - Check if 100 is in the list

# Solution:
score_count = len(scores)     # Should be: 5
first_last = [scores[0], scores[-1]]  # Should be: [95, 85]
has_100 = 100 in scores      # Should be: False
```

5. **Simple List Modification**
```py
vegetables = ["carrot", "potato", "tomato"]
# Write code to:
# - Add "cucumber" to the end
# - Add "lettuce" to the beginning
# - Print the new list length

# Solution:
vegetables.append("cucumber")
vegetables.insert(0, "lettuce")
print(len(vegetables))    # Should print: 5
```

6. **Basic List Combining**
```py
part1 = ["a", "b", "c"]
part2 = ["d", "e", "f"]
# Write code to:
# - Combine part1 and part2 into full_list
# - Create double_list that has part1 repeated twice
# - Print the length of both new lists

# Solution:
full_list = part1 + part2    # Should be: ['a', 'b', 'c', 'd', 'e', 'f']
double_list = part1 * 2      # Should be: ['a', 'b', 'c', 'a', 'b', 'c']
print(len(full_list))        # Should print: 6
print(len(double_list))      # Should print: 6
```

7. **Simple Index Operations**
```py
colors = ["red", "blue", "green", "yellow", "purple"]
# Write code to:
# - Find the index of "green"
# - Print the color at index 1
# - Print the colors from index 1 to 3 (inclusive)

# Solution:
green_index = colors.index("green")    # Should be: 2
second_color = colors[1]               # Should be: "blue"
color_slice = colors[1:4]              # Should be: ["blue", "green", "yellow"]
```

8. **Basic List Checking**
```py
mixed_list = [42, "hello", True, "world"]
# Write code to:
# - Print the length of the list
# - Check if "hello" is in the list
# - Get the first two items
# - Get the last two items using negative indexing

# Solution:
list_length = len(mixed_list)          # Should be: 4
contains_hello = "hello" in mixed_list  # Should be: True
first_two = mixed_list[0:2]            # Should be: [42, "hello"]
last_two = mixed_list[-2:]             # Should be: [True, "world"]
```

## Intermediate Level

9. **List Modification**
```py
# Given this list: colors = ["red", "blue", "green", "yellow"]
# Write code to:
# - Add "purple" to the end
# - Insert "orange" at index 2
# - Remove "blue" and store it in a variable
# - Replace "yellow" with "pink"

# Solution:
colors = ["red", "blue", "green", "yellow"]
colors.append("purple")
colors.insert(2, "orange")
removed_color = colors.remove("blue")
colors[colors.index("yellow")] = "pink"
```

10. **List Operations**
```py
# Given: list1 = [1, 2, 3] and list2 = [4, 5, 6]
# Write code to:
# - Combine the lists into list3
# - Create list4 with list1 repeated 3 times
# - Check if 4 is in list3
# - Find the index of 5 in list3

# Solution:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2           # Should be: [1, 2, 3, 4, 5, 6]
list4 = list1 * 3               # Should be: [1, 2, 3, 1, 2, 3, 1, 2, 3]
contains_4 = 4 in list3         # Should be: True
index_of_5 = list3.index(5)     # Should be: 4
```

## Advanced Level

11. **List Analysis**
```py
# Given: grades = [85, 92, 78, 95, 88, 90]
# Write code to:
# - Find the highest grade without using max()
# - Find the lowest grade without using min()
# - Calculate the difference between highest and lowest grades

# Solution:
grades = [85, 92, 78, 95, 88, 90]
sorted_grades = sorted(grades)
lowest = sorted_grades[0]     # Should be: 78
highest = sorted_grades[-1]   # Should be: 95
difference = highest - lowest # Should be: 17
```

12. **List Manipulation Challenge**
```py
# Given: text = "Hello World"
# Write code to:
# - Create a list of characters from the text
# - Remove all spaces
# - Create a new list with only unique characters (no duplicates)
# - Sort the unique characters alphabetically

# Solution:
text = "Hello World"
char_list = list(text)
no_spaces = list(text.replace(" ", ""))
unique_chars = list(set(no_spaces))
sorted_unique = sorted(unique_chars)
```

## Bonus Challenge

13. **Advanced String and List Operations**
```py
# Given: sentence = "Python Programming Is Fun"
# Write code to:
# - Create a list of words
# - Create a new list with the length of each word
# - Find the longest word (without loops)
# - Create a list of only the first letters of each word

# Solution:
sentence = "Python Programming Is Fun"
words = sentence.split()
word_lengths = [len(word) for word in words]  # Teacher Note: List comprehension not needed, students can do this manually
longest_word = sorted(words, key=len)[-1]
first_letters = [word[0] for word in words]   # Teacher Note: List comprehension not needed, students can do this manually
```

## Practice Problems

For each of these exercises, students should:
1. Write the code before looking at the solution
2. Predict what the output will be
3. Test their code to verify the results
4. Try to come up with alternative ways to solve the same problem

Remember to emphasize:
- The difference between positive and negative indexing
- How to properly use len() function
- The difference between slicing and individual element access
- How to check if items exist in a list
- Basic list methods (append, insert)
- List concatenation and multiplication
