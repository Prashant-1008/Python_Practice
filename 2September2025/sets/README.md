# Python Sets

Sets are unordered collections of unique, hashable elements. They are mutable; elements cannot be duplicated.

- Key properties:
  - Mutable container (add/remove), but elements must be hashable
  - Unordered, unindexed
  - No duplicates
  - Literal syntax: `{ ... }` (but `{}` is an empty dict!), constructor: `set()`

## Common operations

```python
s = {1, 2, 3}
s.add(4)
s.discard(2)   # no error if missing; remove() raises KeyError if missing
exists = 3 in s
length = len(s)
```

## Set algebra

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
union = a | b
inter = a & b
diff = a - b
symdiff = a ^ b
```

## Typical uses

```python
# 1) De-duplicate while preserving no order requirement
items = ["apple", "banana", "apple", "orange", "banana"]
unique = set(items)  # {'apple', 'banana', 'orange'}

# 2) Fast membership tests
banned = {"knife", "gun", "drugs"}
item = "knife"
if item in banned:
    print(f"{item} is prohibited.")

# 3) Find common elements
friends_a = {"Aryan", "Anurag", "Vishakshi"}
friends_b = {"Prajjwal", "Brijkant", "Aryan", "Kareena"}
common = friends_a & friends_b  # {'Aryan'}
```

## When to use sets
- Ensuring uniqueness
- Fast membership checks
- Performing mathematical set operations

## References
- Differences and applications of list, tuple, set, and dictionary: `https://www.geeksforgeeks.org/python/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/` 