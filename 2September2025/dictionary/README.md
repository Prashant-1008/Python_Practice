# Python Dictionaries

Dictionaries are ordered (Python 3.7+) mappings of keys to values. Keys are unique and must be hashable; values can be any type.

- Key properties:
  - Mutable (add/update/remove)
  - Ordered by insertion (3.7+)
  - Unique keys, no duplicates
  - Literal syntax: `{ key: value, ... }`, constructor: `dict()`

## Common operations

```python
rec = {"id": 1, "name": "Prajjwal", "age": 30}
rec["email"] = "prajjwal@example.com"  # add/update
name = rec["name"]
age = rec.get("age", None)             # safe get with default
exists = "name" in rec
removed = rec.pop("age", None)          # remove key
length = len(rec)
```

## Typical uses

```python
# 1) Represent structured records
user = {
    "id": 101,
    "name": "Aryan",
    "email": "aryan@example.com",
}

# 2) Frequency counting
items = ["apple", "banana", "apple", "orange", "banana", "apple"]
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1

# 3) Fast lookup tables
lookup = {"USD": "United States Dollar", "EUR": "Euro", "JPY": "Japanese Yen"}
full = lookup.get("USD")

# 4) JSON interop
import json
payload = '{"name": "prajjwal", "age": 23, "city": "Prayagraj"}'
data = json.loads(payload)
```

## Grouping by keys

```python
employees = [
    {"name": "prajj", "dept": "HR"},
    {"name": "brij", "dept": "IT"},
    {"name": "kareena", "dept": "HR"},
    {"name": "aryan", "dept": "IT"},
]

by_dept = {}
for emp in employees:
    dept = emp["dept"]
    by_dept.setdefault(dept, []).append(emp["name"])
# {'HR': ['prajj', 'kareena'], 'IT': ['brij', 'aryan']}
```

## When to use dictionaries
- Structured data with named fields
- Constant-time average lookups by key
- Counting, grouping, caching, configuration

## References
- Differences and applications of list, tuple, set, and dictionary: `https://www.geeksforgeeks.org/python/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/` 