# Uses of Python Tuples — Demonstrations
# Reference: https://www.geeksforgeeks.org/python/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/
# Notes:
# - Tuples are ordered and immutable; allow duplicates; can be nested; hashable if elements are hashable.
# - Common applications: immutable records (e.g., coordinates), dictionary keys, multiple return values.

print("--- 1) Immutable Data Storage ---")
coords = (10, 20)
print("coords:", coords)
# coords[0] = 99  # would raise TypeError (immutability)

print("--- 2) Dictionary Keys (hashable) ---")
location_to_name = {
    (28.6139, 77.2090): "New Delhi",
    (19.0760, 72.8777): "Mumbai",
}
print("lookup New Delhi:", location_to_name[(28.6139, 77.2090)])
print("all keys:", list(location_to_name.keys()))

print("--- 3) Multiple Return Values (function returns tuple) ---")

def divide_with_remainder(a: int, b: int) -> tuple[int, int]:
    return a // b, a % b

q, r = divide_with_remainder(10, 3)
print("10 // 3 =", q, ", 10 % 3 =", r) 