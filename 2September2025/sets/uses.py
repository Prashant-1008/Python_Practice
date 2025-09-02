# Uses of Python Sets — Demonstrations
# Reference: https://www.geeksforgeeks.org/python/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/
# Notes:
# - Sets are unordered collections of unique, hashable elements; mutable container.
# - Common applications: set algebra (union, intersection, difference), membership testing, de-duplication.

print("--- 1) Set Algebra (Union, Intersection, Difference) ---")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("A:", a)
print("B:", b)
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (A - B):", a - b)

print("--- 2) Membership Testing (Fast) ---")
ban = {"knife", "gun", "drugs"}
item = "knife"
print(f"{item} in ban?", item in ban)

print("--- 3) Finding Common Elements ---")
a_f = {"Aryan", "Anurag", "Vishakshi"}
b_f = {"Prajjwal", "Brijkant", "Aryan", "Kareena"}
print("Common friends:", a_f & b_f)

print("--- 4) De-duplication ---")
items = ["apple", "banana", "apple", "orange", "banana"]
unique_items = set(items)
print("Unique items:", unique_items) 