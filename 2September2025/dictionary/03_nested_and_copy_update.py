# Topic: Nested Dictionaries, Copy (shallow), update(), setdefault()
# Reference: https://www.w3schools.com/python/python_dictionaries.asp and methods page

# Nested dictionaries model hierarchical data
students = {
    1: {"name": "Prajj", "scores": {"math": 90, "science": 88}},
    2: {"name": "Brij", "scores": {"math": 78, "science": 85}},
}

print("Original students:", students)

# Shallow copy: inner dicts are shared
students_copy = students.copy()
print("Shallow copy before change:", students_copy)
students_copy[1]["scores"]["math"] = 99  # also affects students[1]["scores"]["math"]
print("After modifying shallow copy math score ->")
print("students:", students)
print("students_copy:", students_copy)

# Proper deep copy when needed
import copy
students_deep = copy.deepcopy(students)
students_deep[2]["scores"]["science"] = 100  # does not affect original
print("Deep copy after change ->")
print("students (original):", students)
print("students_deep:", students_deep)

# update() merges another mapping into the dict
profile = {"name": "Kareena", "role": "user"}
print("Profile before update:", profile)
profile.update({"role": "moderator", "active": True})
print("Profile after update:", profile)

# setdefault() returns existing value or inserts default then returns it
prefs = {"theme": "dark"}
print("Prefs before setdefault:", prefs)
lang = prefs.setdefault("lang", "en")  # adds 'lang': 'en' if missing
print("setdefault('lang','en') ->", lang)
print("Prefs after setdefault:", prefs) 