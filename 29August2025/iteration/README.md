### Python Iteration

Iteration lets you repeat actions over sequences or while conditions hold.

#### for loops (iterate over any iterable)
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

#### while loops (repeat until condition becomes False)
```python
count = 0
while count < 3:
    print(count)
    count += 1
```

#### break, continue, pass
```python
for x in [0, 1, 2, 3]:
    if x == 1:
        continue  # skip 1
    if x == 3:
        break     # stop at 3
    pass          # no-op placeholder
    print(x)      # prints 0, 2
```

#### range()
```python
for i in range(5):      # 0..4
    print(i)
for i in range(2, 7):   # 2..6
    print(i)
for i in range(10, 0, -2):  # 10, 8, 6, 4, 2
    print(i)
```

#### enumerate() (index + value)
```python
for idx, fruit in enumerate(fruits, start=1):
    print(idx, fruit)
```

#### zip() (iterate in parallel)
```python
names = ["red", "big", "tasty"]
things = ["apple", "banana", "cherry"]
for name, thing in zip(names, things):
    print(name, thing)
```

#### Nested loops
```python
adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for adj in adjectives:
    for fruit in fruits:
        print(adj, fruit)
```

#### Iteration tips
- Prefer iterating directly over items, not indices, unless you truly need the index.
- Use `enumerate` for indices, `zip` for parallel iteration.
- Avoid modifying a list while iterating over it; iterate over a copy or build a new list.
- Comprehensions offer concise transformations: `[x*x for x in range(5) if x % 2 == 0]`.

See example scripts in this folder for practical demonstrations. 