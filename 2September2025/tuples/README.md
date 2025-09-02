# Python Tuples

Tuples are ordered, immutable sequences. They allow duplicates and can hold mixed types.

- Key properties:
  - Immutable (cannot add/remove/update elements)
  - Ordered
  - Allows duplicates
  - Literal syntax: `( ... )` or comma-separated without brackets; constructor: `tuple()`

## Common operations

```python
coords = (10, 20)
singleton = (42,)  # note trailing comma
x, y = coords      # unpacking
first = coords[0]
length = len(coords)
```

## Typical uses

```python
# 1) Returning multiple values from a function

def divide_with_remainder(a: int, b: int) -> tuple[int, int]:
    return a // b, a % b

q, r = divide_with_remainder(10, 3)  # (3, 1)

# 2) As dictionary keys (tuples are hashable if elements are hashable)
location_to_name = {
    (28.6139, 77.2090): "New Delhi",
    (19.0760, 72.8777): "Mumbai",
}

# 3) Fixed records where mutation should be prevented
rgb = (255, 165, 0)  # Orange
```

## When to use tuples
- Fixed-size, read-only records
- Function returns with multiple values
- Keys in dictionaries when a compound key is needed

## References
- Differences and applications of list, tuple, set, and dictionary: `https://www.geeksforgeeks.org/python/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/` 