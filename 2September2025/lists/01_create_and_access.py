# Topic: Create Lists, Types, len(), Access Items, Negative Indexing, Slicing
# Reference: https://www.w3schools.com/python/python_lists.asp
# This file focuses on creation and read-only access patterns to keep outputs simple.

# Creating lists with different types. Lists are ordered and changeable (mutable).
fruits = ["apple", "banana", "cherry"]
mixed = ["abc", 34, True, 40, "male"]
ints = [1, 5, 7, 9, 3]

# Using list() constructor (note the double parentheses when passing a tuple)
constructed = list(("apple", "banana", "cherry"))

# Length of a list
length_fruits = len(fruits)

# Access by index (0-based). Negative indices start from the end: -1 is last item.
first = fruits[0]
last = fruits[-1]
second_to_last = fruits[-2]

# Slicing returns a new list: [start:end] (end not included)
first_two = fruits[0:2]
from_second_on = fruits[1:]
up_to_last = fruits[:-1]

# Step in slicing: [start:end:step]
every_other = ints[0:len(ints):2]
reversed_list = ints[::-1]

print("fruits:", fruits)
print("mixed:", mixed)
print("constructed:", constructed)
print("length_fruits:", length_fruits)
print("Indexing -> first:", first, "last:", last, "second_to_last:", second_to_last)
print("Slicing -> first_two:", first_two)
print("Slicing -> from_second_on:", from_second_on)
print("Slicing -> up_to_last:", up_to_last)
print("Stepped slice -> every_other:", every_other)
print("Reverse via slicing -> reversed_list:", reversed_list) 