def add(a, b):
    return print(f"The sum of {a} and {b} is {a + b}")

add(1, 2)

def add(a, b, c):
    return print(f"The sum of {a}, {b} and {c} is {a + b + c}")

add(1, 2, 3)

def add(a, b, c, d):
    return print(f"The sum of {a}, {b}, {c} and {d} is {a + b + c + d}")

add(1, 2, 3, 4)

def add(*args):
    return print(f"The sum of {args} is {sum(args)}")

add(1, 2, 3, 4, 5)

def add(**kwargs):
    return print(f"The sum of {kwargs.values()} is {sum(kwargs.values())}")

add(a=1, b=2, c=3, d=4, e=5)

def add(*args, **kwargs):
    return print(f"The sum of {args} and {kwargs.values()} is {sum(args) + sum(kwargs.values())}")

add(1, 2, 3, 4, 5, a=1, b=2, c=3, d=4, e=5)