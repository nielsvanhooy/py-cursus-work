# Python Data Structures Tutorial: Working with CSV Data

## Introduction
This tutorial guides you through working with structured data in Python, specifically focusing on reading and organizing CSV-like data. We'll explore different approaches to storing and accessing data, and compare manual parsing with Python's built-in CSV module.

I have provided you with a file with data.

But for others following along on the internet. 
create a new dir.
inside that dir create a new file called export_data.txt
and a file called main.py

use de data below (and store it in the file called export_data.txt):

```python
name,company,serial_number,device_model,management_primair,router_name,location,krn_number
LALM1234.router,Customer A,123456789,Model A,10.12.199.178,NL-LALM1234,nl_1234na_18___etten-leur,123456678
LALM4567.router,Customer B,987654321,Model B,10.12.214.112,NL-LALM4567,nl_4567ps_35___best,98765432
LALM8910.router,Customer C,1314151617,Model C,10.12.213.87,NL-LALM8910,nl_8910bt_4g___rotterdam,97867554
```



## Exercise 1: Reading and Parsing Data

```python
from pathlib import Path

current_dir = Path.cwd()
export_data = current_dir / "export_data.txt"


######################################
# Exercise 1


# The goal of this exercise is to read the file export_data.txt and extract the column names from the first line.
# for now we will use the read_text() method on a Path object to read the file.
# if we just use read_text() and iterate over it with a for loop we go letter by letter through the file.
# but we want to go trough it line by line.
# we can use read_text().splitlines() to get a list of lines.

file_contents = export_data.read_text().splitlines()

# now get the column names from the first line. HINT: use list indexing to get it. and use split() to split the line by comma.
column_names = file_contents[0].split(",")

# now get the rest of the lines, and split them by comma, and store them in a list.


```

## Exercise 2: Choosing Data Structures

```python
######################################
# Exercise 2


# now that we have the column names and the data lines, we can create a "datastructure with this information".
# what datastructure would you use?

# There are 2 approaches here. and we are gonna make them both. and later think about which one is better.
# the first one is to create a list of dictionaries, where each dictionary represents a row in the data.

# you will need to create a "default" dictionary that maps to the names of the columns.

column_dictionary = {}
for column_name in column_names:
    column_dictionary[column_name] = None

# now that we created a default dictionary, we can iterate over the data lines and create a dictionary for each line.
# you wil need the following

# an empty list to store the dictionaries
# a for loop to iterate over the data lines
# a "temporary" dictionary to store the column names and their values
# a nested for loop to iterate over the columns
# and create a dictionary for each line
# and add it to the list of dictionaries

# this is probably the hardest part of the exercise, so take your time and think about it.
# use the debugger in pycharm to step through the code and see what is happening. so you can visualize it.

######### YOUR CODE BELOW

```

```python
# SECOND APPROACH
# the second approach is that we create one giant dictionary where the key is a value from the data.
# and the value is all the associated data as a dictionary with all the data.
# for this you will need to create a dictionary that maps the name of the router to its data.

# we start with a variable set to an empty dictionary.
# we can reuse the code we created above to create a dictionary for each line.
# but now we will add the dictionary to the data_records dictionary with the name of the router as the key.


######### YOUR CODE BELOW

```

## Exercise 3: Searching Records

```python
######################################
# Exercise 3

# now with both approaches i want to search for a record.

# lets say i want to find the record with the ip_address "10.12.192.115"
# how would you build this with both approaches??

## your code here (for both approaches)
```



## Final Thoughts: The Easier Way with CSV Module

```python
######################################
# Final thoughts


# Pffffewwww that was a lot of effort right? reading something as simple as a text file. should not be such a challenge.
# agreed?

# ok then. now that we look with our eyes to the export_data.txt file, we see that the first line is the header.
# and all data is comma separated.
# so that makes it like a .csv file right?

# python has ways to read a csv file.

import csv

data_dictionary = {}

with open(export_data, "r") as file:
    reader = csv.DictReader(file)      # this read the file as a dict. based on the column names.
    for row in reader:
        name = row["name"]
        data_dictionary[name] = row

print(data_dictionary)

# now we can use the csv module to read the file and create a dictionary for each line.
# and that is a lot simpler.
# but we have to do it the hard way first. so we understand how it works.
```

## Key Takeaways

1. Python offers multiple ways to structure data (lists of dictionaries vs dictionaries of dictionaries)
2. Each approach has advantages for different use cases:
   - List of dictionaries: Good for sequential processing
   - Dictionary by name: Good for quick lookups by key
3. Built-in modules like `csv` simplify common tasks
4. Understanding the manual implementation helps you learn fundamental concepts before using specialized libraries