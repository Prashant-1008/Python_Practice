### Python Conditionals

Python uses indentation to define code blocks. Conditional statements control flow based on boolean expressions.

#### if / elif / else
```python
x = 15
if x > 20:
    print("greater than 20")
elif x == 20:
    print("equals 20")
else:
    print("less than 20")
```

#### Comparisons and logical operators
- `==`, `!=`, `<`, `<=`, `>`, `>=`
- `and`, `or`, `not`
- Chained comparisons: `18 <= age < 65`
- Membership/identity: `in`, `not in`, `is`, `is not`
```python
name = "alice"
age = 30
if name and (18 <= age < 65):
    print("eligible")
```

#### Truthiness
Values evaluate to False: `0`, `0.0`, `''`, `[]`, `{}`, `set()`, `None`, `False`. Everything else is True.
```python
items = []
if not items:
    print("no items")
```

#### Ternary expression (conditional expression)
```python
status = "adult" if age >= 18 else "minor"
```

#### match/case (Python 3.10+)
Structured pattern matching for clear multi-branch logic.
```python
command = "start"
match command:
    case "start":
        print("starting…")
    case "stop":
        print("stopping…")
    case _:
        print("unknown command")
```

#### Common pitfalls and tips
- Indentation is syntactic; be consistent.
- Use `is` for identity (`x is None`), not for numeric/string equality.
- Prefer clear conditions; extract complex checks into well-named variables or functions.

See example scripts in this folder for hands-on usage. 