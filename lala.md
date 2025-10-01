#### datatypes


# int (integer)
# float (floating point number)
# str (string): text
# bool (boolean): yes / no
# None : missing / unknown value

print(type(int(2)))
print(type(float(2)))
print(type(str(2)))
print(type(bool("True")))
print(type(None))



### control structures ###

# if statements
if True:
    print("This is true")

# of formeel.


# if <conditie>:
#     <expressie>

# Operator	Meaning	Example
# ==	equal to	x == y
# !=	not equal to	x != y
# >	greater then	x > y
# >=	greater then or equal to	x >= y
# <	less than	x < y
# <=	less then or equal	x <= y


# Operator	Meaning	Example
# and	True if both are true	x and y
# or	True if at least one is true	x or y
# not	True only if false	not x


########## Truthy / Falsy

#####  Falsy Values in Python
# Sequences and Collections:
#
# Empty lists []
# Empty tuples ()
# Empty dictionaries {}
# Empty sets set()
# Empty strings ""
# Empty ranges range(0)
# Numbers
# Zero of any numeric type:
#
# Integer: 0
# Float: 0.0
# Complex: 0j
# Constants:
#
# None
# False


# 🔹 Truthy Values in Python
# According to the Python Documentation:
#
# By default, an object is considered true.
#
# Truthy values include:
#
# Non-empty sequences or collections (lists, tuples, strings, dictionaries, sets).
# Numeric values that are not zero.
# True


# i have also added more information about the match case system for who finds this interesting.

# https://nielsvanhooy.github.io/py-cursus-work/11-1-match-case.html

########## lists

network_protocols = ["HTTP", "FTP", "TCP", "UDP", "SMTP"]

ip_addresses = ["192.168.0.1", "192.168.0.2", "192.168.0.3"]

network_devices = [
    ["Router", "192.168.0.1", "00:1A:2B:3C:4D:5E"],
    ["Laptop", "192.168.0.10", "00:1B:44:11:3A:B7"],
    ["Smartphone", "192.168.0.15", "00:1C:42:2E:60:4A"]
]

########### dicts

device_config = {
    "hostname": "laptop-01",
    "ip_address": "192.168.0.10",
    "mac_address": "00:1B:44:11:3A:B7",
    "connected": True
}

device_config_two = {
    "hostname": "laptop-01",
    "ip_address": "192.168.0.10",
    "mac_address": "00:1B:44:11:3A:B7",
    "connected": True
}

network_status = {
    "network_name": "HomeNetwork",
    "total_devices": 3,
    "online_devices": ["Laptop", "Smartphone"],
    "router": {
        "ip": "192.168.0.1",
        "uptime_hours": 72,
        "firmware": "v1.2.3"
    },
    "last_scan": None
}

####### methods on list and dicts.

# Lists

# Pro's of lists
# - Easy way to store a collection of related items
# - Easy to add, remove, and modify items
# - Usefull for creating nested data structures, such as lists of lists/dictionaries
#
# Con's of lists
# - Pretty slow when performing operations on large lists
# - Pretty slow if your doing math things on the indexes (use real arrays for that) python docs/Numpy project
# - Use more disk spave because how there implemented (is this a real deal anymore these days?) perhaps for the tech giants

my_list = [1, 2, 3]

# Method	Description
# append(x)	Adds an item x to the end of the list.
# extend(iterable)	Adds all elements of an iterable to the end.
# insert(i, x)	Inserts x at position i.
# remove(x)	Removes the first occurrence of x.
# pop([i])	Removes and returns the item at index i (default last).
# clear()	Removes all items from the list.
# index(x[, start[, end]])	Returns the index of the first occurrence of x.
# count(x)	Returns the number of times x appears.
# sort(key=None, reverse=False)	Sorts the list in place.
# reverse()	Reverses the list in place.
# copy()	Returns a shallow copy of the list.


# Dicts

# Pro's of dictionaries
# - Extremely fast for lookups
# - Easy to store and retrieve key-value pairs
# - Make code a bit easier to read. (instead of using indexes)
# - We can look up a certain value in a dictionary very quickly. Instead, with a list, we would have to read the list before we hit the required element. This difference grows drastically if we increase the number of elements.
#
# Con's of dictionaries
# - They occupy more memory than lists, for extreme amounts of data this is not the most suitable data type
# - As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


my_dict = {"key": "value"}

# Method	Description
# clear()	Removes all items from the dictionary.
# copy()	Returns a shallow copy.
# fromkeys(iterable, value=None)	Creates a new dict with keys from iterable.
# get(key[, default])	Returns the value for key if present.
# items()	Returns a view of (key, value) pairs.
# keys()	Returns a view of keys.
# values()	Returns a view of values.
# pop(key[, default])	Removes and returns key's value.
# popitem()	Removes and returns last inserted (key, value).
# setdefault(key[, default])	Returns the value for key; sets it if not present.
# update([other])	Updates the dictionary with key-value pairs from another dict or iterable.



# tuples


# Pro's of tuples
# - Immutable, once created. we can be sure that the data will not be changed.
#
# Con's of tuples
# - We cannot use them when we have to work with modifiable data, then we need to use lists.
# - Tuples cannot be copied
# - They occupy more memory than lists


server_address = ("192.168.1.100", 8080)
device_info = ("Router", "192.168.0.1", "00:1A:2B:3C:4D:5E")
protocol_ports = (
    ("HTTP", 80),
    ("HTTPS", 443),
    ("SSH", 22)
)

# Tuple unpacking # needs to be same length as tuple

# sets

connected_ips = {"192.168.0.10", "192.168.0.11", "192.168.0.12"}

active_protocols = {"TCP", "UDP", "ICMP"}

mac_list = ["00:1A:2B:3C:4D:5E", "00:1A:2B:3C:4D:5E", "00:1B:44:11:3A:B7"]

unique_macs = set(mac_list)

# i use it mostly to remove duplicates from a list, or to check if an item is in a list.

# Pro's of sets
# - We can perform unique (but similair) operations on sets
# - They are significantly faster than lists when it comes to checking for the existence of an element
#
# Con's of sets
# - They are unordered, so we can't access elements by index
# - we cannot change set elements by indexing as we can with lists


## list slicing

# Slicing allows you to access a portion of a list or string.


# working with dicts and accessing content.

# functions

# working with file paths and Pathlib.

# opening files without pathlib

# working with exceptions.

