# Topic: Immutability, Convert Tuple <-> List to "modify", Concatenate, Multiply
# Reference: https://www.w3schools.com/python/python_tuples_update.asp
# Tuples cannot be changed in-place. We can convert to a list, modify, then convert back.

t = ("apple", "banana", "cherry")
print("Original tuple:", t)

# Convert to list to modify
as_list = list(t)
print("As list (before changes):", as_list)
as_list[1] = "blueberry"
as_list.append("date")
modified = tuple(as_list)
print("Modified (back to tuple):", modified)

# Concatenate tuples creates a new tuple
u = (1, 2) + (3, 4)
print("Concatenation (1,2)+(3,4):", u)

# Repetition (multiply) repeats the tuple
rep = ("A",) * 3
print("Repetition ('A',)*3:", rep) 