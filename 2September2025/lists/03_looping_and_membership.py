# Topic: Loop Lists (for/while), Membership (in/not in), enumerate
# Reference: https://www.w3schools.com/python/python_lists.asp
# Show idiomatic looping and membership checks.

animals = ["cat", "dog", "hamster"]

print("-- For over values --")
for a in animals:
    print("animal:", a)

print("-- For with index via range --")
for i in range(len(animals)):
    print("index:", i, "value:", animals[i])

print("-- enumerate (index, value) --")
for idx, val in enumerate(animals, start=0):
    print("enumerate ->", idx, val)

print("-- while loop --")
i = 0
while i < len(animals):
    print("while ->", i, animals[i])
    i += 1

# Membership tests
has_cat = "cat" in animals
has_bird = "bird" in animals
not_dog = "dog" not in animals

print("Membership -> has_cat:", has_cat, "has_bird:", has_bird, "not_dog:", not_dog) 