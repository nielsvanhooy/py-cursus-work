# Python Lists of Lists Exercises

## Beginner Level

1. **Shopping Cart Items and Prices**
```py
# Given this shopping cart where each item has [name, price, quantity]:
cart = [
    ["milk", 2.50, 2],
    ["bread", 1.80, 1],
    ["eggs", 3.20, 1],
    ["cheese", 4.50, 1]
]
# Write code to:
# - Print the first item's name
# - Print the price of eggs
# - Print the quantity of milk

# Solution:
first_item = cart[0][0]        # Should print: "milk"
eggs_price = cart[2][1]        # Should print: 3.20
milk_quantity = cart[0][2]     # Should print: 2
```

2. **Restaurant Menu Categories**
```py
# Given this menu where each category has [name, price, spicy_level]:
menu = [
    ["Pizza Margherita", 12.99, 0],
    ["Spicy Chicken Wings", 9.99, 2],
    ["Buffalo Wings", 10.99, 3],
    ["Garden Salad", 7.99, 0]
]
# Write code to:
# - Print the name of the second dish
# - Print all information about the last dish
# - Create a list of just the prices

# Solution:
second_dish = menu[1][0]        # Should print: "Spicy Chicken Wings"
last_dish = menu[-1]            # Should print: ["Garden Salad", 7.99, 0]
prices = [menu[0][1], menu[1][1], menu[2][1], menu[3][1]]  
# Should print: [12.99, 9.99, 10.99, 7.99]
```

3. **Weekly Grocery List**
```py
# Given this grocery list where each item has [name, quantity, bought(True/False)]:
groceries = [
    ["apples", 6, False],
    ["bananas", 4, True],
    ["milk", 2, False],
    ["bread", 1, True]
]
# Write code to:
# - Create a list of items not bought yet
# - Print the quantities of all items
# - Print the status of milk

# Solution:
not_bought = [groceries[0][0], groceries[2][0]]  # Should be: ["apples", "milk"]
quantities = [groceries[0][1], groceries[1][1], groceries[2][1], groceries[3][1]]
# Should be: [6, 4, 2, 1]
milk_status = groceries[2][2]   # Should be: False
```

## Intermediate Level

4. **Monthly Budget Tracker**
```py
# Given this budget where each item has [category, budget, spent]:
budget = [
    ["groceries", 500.00, 420.50],
    ["transport", 200.00, 150.75],
    ["entertainment", 150.00, 145.00],
    ["utilities", 300.00, 300.00]
]
# Write code to:
# - Create a list of categories
# - Find how much is left in groceries budget
# - Create a list of amounts spent

# Solution:
categories = [budget[0][0], budget[1][0], budget[2][0], budget[3][0]]
# Should be: ["groceries", "transport", "entertainment", "utilities"]

groceries_left = budget[0][1] - budget[0][2]  # Should be: 79.50

spent = [budget[0][2], budget[1][2], budget[2][2], budget[3][2]]
# Should be: [420.50, 150.75, 145.00, 300.00]
```

5. **Online Store Products**
```py
# Given these products where each has [name, price, stock, rating]:
products = [
    ["Gaming Mouse", 29.99, 50, 4.5],
    ["Keyboard", 59.99, 30, 4.8],
    ["Headphones", 99.99, 15, 4.7],
    ["Mousepad", 19.99, 100, 4.3]
]
# Write code to:
# - Find the most expensive product (without loops)
# - Create a list of products that cost less than 50.00
# - Find the product with the highest rating

# Solution:
sorted_by_price = sorted(products, key=lambda x: x[1])
most_expensive = sorted_by_price[-1][0]  # Should be: "Headphones"

cheap_products = [products[0][0], products[3][0]]  
# Should be: ["Gaming Mouse", "Mousepad"]

sorted_by_rating = sorted(products, key=lambda x: x[3])
best_rated = sorted_by_rating[-1][0]  # Should be: "Keyboard"
```

## Important Tips:
1. Remember to use double square brackets: list[row][column]
2. First index selects the item, second index selects the property
3. You can store different types in the same inner list (strings, numbers, booleans)
4. Drawing the data as a table can help visualize the structure

## Practice Suggestions:
1. Try to write the code without looking at the solutions
2. Predict what each piece of code will output
3. Try creating your own similar examples with different data
4. Practice with different data types in the inner lists
```

Would you like more examples focusing on any particular real-world scenario? I can create more exercises based on:
- Restaurant orders
- School grades and subjects
- Product inventory
- Movie/Book ratings and reviews
- Sports scores and statistics