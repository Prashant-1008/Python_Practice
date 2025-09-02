### Python Variables

Variables are names that reference values in memory. Python uses dynamic typing: a name can reference values of any type over time.

#### Creating and assigning
```python
x = 10
name = "Alice"
pi = 3.14159
is_active = True
items = [1, 2, 3]
```

#### Naming and style
- Use lowercase_with_underscores for variables (`snake_case`).
- Start with a letter or `_`; then letters, digits, `_`.
- Avoid built-in names like `list`, `dict`, `str` for your own variables.

#### Basic types
- Numbers: `int`, `float`, `complex`
- Text: `str`
- Booleans: `bool`
- Collections: `list`, `tuple`, `set`, `dict`

#### Type checking and conversion
```python
age = "30"
age = int(age)  # convert string to int
print(type(age) is int)  # True
```

#### Multiple assignment and unpacking
```python
a, b = 1, 2
x, y, z = ["apple", "banana", "cherry"]
first, *middle, last = [1, 2, 3, 4, 5]
```

#### Immutability vs mutability
- Immutable: `int`, `float`, `str`, `tuple` (value cannot change; reassignment binds a new value)
- Mutable: `list`, `dict`, `set` (value can change in place)

#### Scope
- Names defined inside a function are local.
- `global` declares a module-level name; `nonlocal` binds to an outer-but-not-global scope.
```python
counter = 0

def tick():
    global counter
    counter += 1
```

#### F-strings and formatting
```python
name = "Alice"
age = 30
print(f"{name} is {age} years old")
```

#### Useful operations
```python
nums = [1, 2, 3]
nums.append(4)
user = {"name": "Bob", "age": 25}
user["age"] = 26
```

Tips
- Prefer descriptive names.
- Initialize variables close to where they are used.
- Choose appropriate types for your problem and convert explicitly when needed.

See example scripts in this folder for hands-on usage. 