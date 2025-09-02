# Python Lists

Lists are dynamic, ordered, and mutable sequences. They allow duplicates and can hold mixed types.

- Key properties:
  - Mutable (can add/remove/update)
  - Ordered (preserves insertion order)
  - Allows duplicates
  - Literal syntax: `[ ... ]`, constructor: `list()`

## Common operations

```python
nums = [23, 45, 12, 67, 34]
nums.append(89)           # add at end
nums.insert(1, 99)        # insert at index
nums.remove(45)           # remove by value (first match)
value = nums.pop()        # pop last; use pop(i) for index
nums[0] = -1              # update
exists = 34 in nums       # membership test
length = len(nums)
```

## Iteration and processing

```python
nums = [1, 2, 3, 4, 5]
# aggregate
total = sum(nums)
# transform
squares = [n * n for n in nums]
# filter
odds = [n for n in nums if n % 2 == 1]
```

## Stacks and queues with lists

```python
# Stack (LIFO)
stack = []
stack.append('a')
stack.append('b')
last = stack.pop()  # 'b'

# Queue (FIFO) — pop(0) is O(n); for real queues prefer collections.deque
queue = []
queue.append('first')
queue.append('second')
front = queue.pop(0)  # 'first'
```

## Nested lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
diagonal = [matrix[i][i] for i in range(len(matrix))]  # [1, 5, 9]
```

## When to use lists
- Collecting an ordered sequence of items
- You need to frequently add/remove/update
- You want simple, indexable, growable arrays

## References
- Differences and applications of list, tuple, set, and dictionary: `https://www.geeksforgeeks.org/python/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/` 