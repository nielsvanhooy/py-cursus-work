# Lists, Loops & More

## Lists

Lists are one of the most powerful data types in Python.
With some fictive data we are going to analyze data about mobile apps.


We will be working with this data:

| Name                      | Price | Currency | Rating Count | Rating |
|---------------------------|-------|----------|--------------|--------|
| Facebook                 | 0.0   | USD      | 2,974,676    | 3.5    |
| Instagram                | 0.0   | USD      | 2,161,558    | 4.5    |
| Clash of Clans           | 0.0   | USD      | 2,130,805    | 4.5    |
| Temple Run              | 0.0   | USD      | 1,724,546    | 4.5    |
| Pandora - Music & Radio | 0.0   | USD      | 1,126,879    | 4.0    |


We will call each value in the table a data point. 
For instance, the first row (after the column titles) has five data points:

- Facebook
- 0.0
- USD
- 2974676
- 3.5


lets call this collection of data a `dataset`.
our dataset has 5 rows and 5 columns.

With all the knowledge up to know we could store this data in variables like this:

```py
app_one_name = "Facebook"
app_one_price = 0.0
app_one_currency = "USD"
app_one_rating_count = 2974676
app_one_rating = 3.5
```

<details>
    <summary>Click to reveal more</summary>
<p>
The text "Facebook" as a string<br>
The price 0.0 as a float<br>
The text "USD" as a string<br>
The rating count 2,974,676 as an integer<br>
The user rating 3.5 as a float<br>
</p>
</details>

Creating a variable for each data point in our data set would be a cumbersome process. Fortunately, 
we can store data more efficiently using lists. 
This is how we can create a list of data points for the first row:

```py
row_one = ["Facebook", 0.0, "USD", 2974676, 3.5]
print(row_one)
type_row_one = type(row_one)
```

To create the `list` above, we:

Typed out a sequence of data points and separated each with a comma: 'Facebook', 0.0, 'USD', 2974676, 3.5
Surrounded the sequence with brackets: `['Facebook', 0.0, 'USD', 2974676, 3.5]`
After we created the list, we stored it in the computer's memory by assigning it to a variable named row_one.

To create a list of data points, we only need to:

Separate the data points with a comma.
Surround the sequence of data points with brackets.


## A note on lists

There are 2 ways to create an empty list in python:

- list()
- []

Functionally there the same. 
However there a speed tradeoffs and that is due to implementation details in the C compiler behind python.

To see the speed difference we can use the `timeit` module.
```py
from timeit import timeit

timeit("[]")
0.040084982867934334

timeit("list()")
0.17704233359267718
```
We can see that the `[]` is faster than the `list()` function. By a big margin.

# Let's move on.
Now let's create five lists, one for each row in our dataset:

```py
row_one   = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_two   = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_three = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_four  = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_five  = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
```

## Indexing python lists

A list can contain a variety of data types. A list like [4, 5, 6] has identical data types (only integers), 
while the list ['Facebook', 0.0, 'USD', 2974676, 3.5] has mixed data types:

- Two strings ('Facebook', 'USD')
- Two floats (0.0, 3.5)
- One integer (2974676)

- The ['Facebook', 0.0, 'USD', 2974676, 3.5] list has five data points. 
To find the length of a list, we can use the `len()` command we discussed earlier:

Example:

```py
row_one   = ['Facebook', 0.0, 'USD', 2974676, 3.5]
print(len(row_one))

list_one = [1, 2, 3]
print(len(list_one))

list_two = []
print(len(list_two))
```
Output would be:
- 5
- 3
- 0


For small lists, we can just count the data points on our screens to find the length, 
but the len() command will prove very useful whenever you work with lists containing many elements, 
or need to write code for data where you don't know the length ahead of time.


Each element (data point) in a list has a specific number associated with it, 
called an index number. The indexing always starts at 0, 
so the first element will have the index number 0, 
the second element the index number 1, and so on.

![indexing plaatje](img/lists-indexing.svg)

To quickly find the index of a list element, 
identify its position number in the list, and then subtract 1. 

For example, the string 'USD' is the third element of the list (position number 3), 
so its index number must be 2 since 3 - 1 = 2.

or what i find easier. just remember that the first element is 0 and the second is 1 and so on

The index numbers help us retrieve individual elements from a list. 
Looking back at the list row_one from the code example above, 

we can retrieve the first element (the string 'Facebook') with the index number 0 by running the code row_one[0].


```py
row_one = ['Facebook', 0.0, 'USD', 2974676, 3.5]
print(row_one[0])
```
Gives us the output: "Facebook"

The syntax for retrieving individual list elements follows the model `list_name[index_number]`. 

For instance, the name of our list above is row_one and the index number of the first element is 0 
— following the `list_name[index_number]` model, we get row_one[0], 
where the index number 0 is in square brackets after the variable name row_one.

![indexing plaatje 2](img/lists-indexing-two.svg)

This is how we can retrieve each element in row_one:

```py
row_one = ['Facebook', 0.0, 'USD', 2974676, 3.5]

print(row_one[0])
print(row_one[1])
print(row_one[2])
print(row_one[3])
print(row_one[4])
```

output:

- Facebook
- 0.0
- USD
- 2974676
- 3.5

Retrieving list elements makes it easier to perform operations. 
For instance, we can select the ratings for Facebook and Instagram, 
and find the average or the difference between the two:


```py
row_one   = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_two   = ['Instagram', 0.0, 'USD', 2161558, 4.5]

difference = row_one[4] - row_two[4]
average_rating = (row_one[4] + row_two[4]) / 2

print(difference)
print(average_rating)
```
Output:

- 1.0
- 4.0


