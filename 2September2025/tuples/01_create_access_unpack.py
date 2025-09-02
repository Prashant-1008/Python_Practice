# Topic: Create Tuples, Access Items, Negative Indexing, Slicing, Unpacking
# Reference: https://www.w3schools.com/python/python_tuples.asp
# Tuples are ordered and immutable. They can contain duplicates and mixed types.

coords = (10, 20, 30)
singleton = (42,)  # A 1-item tuple needs a trailing comma
mixed = (1, "two", 3.0, True)

# Access by index
first = coords[0]
last = coords[-1]

# Slicing returns a new tuple
middle = coords[1:2]
reversed_tuple = coords[::-1]

# Unpacking: the number of variables must match the length
x, y, z = coords

# Extended unpacking with * collects remaining items into a list
nums = (1, 2, 3, 4, 5)
a, *mid, e = nums  # a=1, mid=[2,3,4], e=5

print("coords:", coords)
print("singleton:", singleton)
print("mixed:", mixed)
print("Indexing -> first:", first, "last:", last)
print("Slicing -> middle:", middle, "reverse:", reversed_tuple)
print("Unpacked ->", x, y, z)
print("Extended unpack -> a:", a, "mid:", mid, "e:", e) 