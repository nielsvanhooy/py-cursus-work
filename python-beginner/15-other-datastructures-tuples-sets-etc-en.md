## Other Datastructures in python

datastructures are a way to store and organize data in a program.
this organization is required for efficient storage and retrieval of data. and modification of data

datastructures can be divided into two categories:
- Mutable
- Immutable

besides the datastructures that we handled in the previous chapters (list and dict), 
there are a few more that are worth mentioning.
we will get into more complex data structures in the future.


### lists (already discussed)
Dynamic mutable "arrays" which can store any type of data.


Pro's of lists
- Easy way to store a collection of related items
- Easy to add, remove, and modify items
- Usefull for creating nested data structures, such as lists of lists/dictionaries

Con's of lists
- Pretty slow when performing operations on large lists
- Pretty slow if your doing math things on the indexes (use real arrays for that) python docs/Numpy project
- Use more disk spave because how there implemented (is this a real deal anymore these days?) perhaps for the tech giants

### Dictionaries (already discussed)

Dictionaries in python look like real life dictionaries.
You find a key in the book. and read a value.

It is a mutable datastructure (meaning contents can be changed after creation)
Dictionaries are extremely fast for lookups (searching for a key) (O(1) time complexity)
That means near instant access to the value of a key.

They key must be of an immutable type. (string, number, tuple)
in practise you will mostly use string and number.

value can be of any type (including lists, dictionaries, and other data structures)

Pro's of dictionaries
- Extremely fast for lookups
- Easy to store and retrieve key-value pairs
- Make code a bit easier to read. (instead of using indexes)
- We can look up a certain value in a dictionary very quickly. Instead, with a list, we would have to read the list before we hit the required element. This difference grows drastically if we increase the number of elements.

Con's of dictionaries
- They occupy more memory than lists, for extreme amounts of data this is not the most suitable data type 
- As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


### Sets

Sets in Python can be defined as mutable dynamic collections of immutable unique elements. 
The elements contained in a set must be immutable. 
Sets may seem very similar to lists, but in reality, they are very different.

They can only contain unique elements (no duplicates),
Thus, sets can be used to remove duplicated from a list.
They can use mathematical set operations like union, intersection, difference, and symmetric difference. (however personally i have never used this)

Finally they are very efficient in checking weather an element is in the set or not. (O(1) time complexity) (meaning near instant access)

Pro's of sets
- We can perform unique (but similair) operations on sets 
- They are significantly faster than lists when it comes to checking for the existence of an element

Con's of sets
- They are unordered, so we can't access elements by index
- we cannot change set elements by indexing as we can with lists

## Syntax

a set usses curly brackets `{}` just like a dictionary, but without the key-value pairs.
only immutable elements can be added to a set.

example all immutable elements
```python
example_set = {"apple", "banana", "cherry", 1 , 2}
```

this wont work with sets:
```python
example_set = {[], "banana", "cherry", 1 , 2}
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unhashable type: 'list'

```


Sets require their items to be hashable. 
Out of types predefined by Python only the immutable ones, such as strings, numbers, and tuples, are hashable. 
Mutable types, such as lists and dicts, are not hashable because a change of their contents would change the hash and break the lookup code.

### Creating sets

To create a set, we can use either curly brackets `{}` or the `set()` constructor. 

```python
# Create a set using curly brackets
s1 = {1, 2, 3}

# Create a set using the set() constructor
s2 = set([1, 2, 3, 4])

# Print out sets
print(f"Set s1: {s1}")
print(f"Set s2: {s2}")
```
In the second example, we used an iterable (such as a list) to create a set. that works.
However you cant store a list in a set (see Type error above)


### operations on sets
sets originate from the world of math. so you can perform certain "math" operations on them.

For example, we can create a union of sets, which basically means merging two sets together. 
However, if two sets have two or more identical values, the resulting set will contain only one of these values. 
There are two ways to create a union: either with the `union()` method or with the vertical bar `|` operator. Let's make an example:

```python
# Create two new sets
names1 = set(["Glory", "Tony", "Joel", "Dennis"])
names2 = set(["Morgan", "Joel", "Tony", "Emmanuel", "Diego"])

# Create a union of two sets using the union() method
names_union = names1.union(names2)

# Create a union of two sets using the | operator
names_union = names1 | names2

# Print out the resulting union
print(names_union)

#gives
{'Glory', 'Dennis', 'Diego', 'Joel', 'Emmanuel', 'Tony', 'Morgan'}

```
In the above union, we can see that Tony and Joel appear only once, even though we merged two sets.
that is because sets only store unique elements.

what i use mostly for sets is to remove duplicates from a list. by converting to a set. and then back to a list to continue working with it.

```python
mijn_lijst = ["niels", "eelke", "jan", "jilaali", "niels", "eelke", "jan", "jilaali"]

mijn_lijst_zonder_dubbelen = list(set(mijn_lijst))

# prints
['niels', 'jilaali', 'jan', 'eelke']

```

Next, we may also want to find out which names appear in both sets. 
This can be done with the intersection() method or the ampersand (&) operator.

```python
# Create two new sets
names1 = set(["Glory", "Tony", "Joel", "Dennis"])
names2 = set(["Morgan", "Joel", "Tony", "Emmanuel", "Diego"])

# Intersection of two sets using the intersection() method
names_intersection = names1.intersection(names2)

# Intersection of two sets using the & operator
names_intersection = names1 & names2

# Print out the resulting intersection
print(names_intersection)

# prints
{'Joel', 'Tony'}
```

The last example of set operations is the difference between two sets. 
In other words, this operation will return all the elements that **are present in the first set**, **but not in the second one.** 
We can use either the `difference()` method or the minus operator `-`:

```python
names1 = set(["Glory", "Tony", "Joel", "Dennis"])
names2 = set(["Morgan", "Joel", "Tony", "Emmanuel", "Diego"])

# Create a set of all the names present in names1 but absent in names2 with the difference() method
names_difference = names1.difference(names2)

# Create a set of all the names present in names1 but absent in names2 with the - operator
names_difference = names1 - names2

# Print out the resulting difference
print(names_difference)

# gives
 {'Dennis', 'Glory'}
```

What would happen if you swapped the positions of the sets? 
Try to predict the result before the attempt.

if you dont know the answer. see the awnser above the code snippet.


### Lets find out how much faster sets are than lists

```python
import time

def find_element(iterable):
    """Find an element in range 0-4999 (included) in an iterable and pass."""
    for i in range(5000):
        if i in iterable:
            pass

# Create a list and a set
s = set(range(10000000))

l = list(range(10000000))

start_time = time.time()
find_element(s) # Find elements in a set
print(f"Finding an element in a set took {time.time() - start_time} seconds.")

start_time = time.time()
find_element(l) # Find elements in a list
print(f"Finding an element in a list took {time.time() - start_time} seconds.")


```
Finding an element in a set took 0.00016832351684570312 seconds.
Finding an element in a list took 0.04723954200744629 seconds.

This is an insane order of magnitude difference.
And this difference will only increase for larger sets and lists.



### Tuples

Tuples can feel like lists, but they are immutable.
We would use tuples if we needed a data structure that, once created, cannot be changed/modified anymore.

Like is said before. Tuples can be used as the keys in dictionaries, (if all items in the tuple are immutable). however i have never used this. and i dont come across it professionally.

Other then that, tuples have the same properties as lists.
to create a tuple 

- we use the `()` brackets
- or the `tuple()` constructor

Pro's of tuples
- Immutable, once created. we can be sure that the data will not be changed.

Con's of tuples
- We cannot use them when we have to work with modifiable data, then we need to use lists.
- Tuples cannot be copied
- They occupy more memory than lists

Time for Examples

```python
# Create a tuple using round brackets
t1 = (1, 2, 3, 4)

# Create a tuple from a list the tuple() constructor
t2 = tuple([1, 2, 3, 4, 5])

# Create a tuple using the tuple() constructor
t3 = tuple([1, 2, 3, 4, 5, 6])

# Print out tuples
print(f"Tuple t1: {t1}")
print(f"Tuple t2: {t2}")
print(f"Tuple t3: {t3}")

```

# result
    Tuple t1: (1, 2, 3, 4)
    Tuple t2: (1, 2, 3, 4, 5)
    Tuple t3: (1, 2, 3, 4, 5, 6)

Is it possible to create tuples from other data structures (i.e., sets or dictionaries)? 
Try it for practice.

As said before. Tuples are immutable. so we cannot change them once the tuple is created.
Lets see what happens if we try to change a tuple.

```python
# Try to change the value at index 0 in tuple t1
t1[0] = 1

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

```

It is a TypeError! Tuples do not support item assignments because they are immutable. 
To solve this problem, we can convert this tuple into a list.

## what can we do with tuples

we can access the elements of a tuple by indexing.

```python
t2 = (1, 2, 3, 4, 5)
# Print out the value at index 1 in the tuple t2
print(f"The value at index 1 in t2 is {t2[1]}.")
```
  The value at index 1 in t2 is 2.

## for methods that we can use on tuples. see the python docs or url below

[Tuple Methods](https://www.w3schools.com/python/python_ref_tuple.asp)