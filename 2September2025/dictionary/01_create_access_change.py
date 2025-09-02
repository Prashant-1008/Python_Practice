# Topic: Create Dicts, Access Items, get(), Change/Add Items, Remove (pop/popitem/del/clear)
# Reference: https://www.w3schools.com/python/python_dictionaries.asp

person = {
    "name": "Prajjwal",
    "age": 23,
    "city": "Prayagraj",
}
print("Original:", person)

# Access items
name = person["name"]
age = person.get("age", 0)  # get with default if key missing
print("Access -> name:", name, "age via get():", age)

# Add/change items
person["email"] = "prajjwal@example.com"  # add new key
person["age"] = 24                         # change value
print("After add/change:", person)

# Remove operations
popped_age = person.pop("age", None)  # remove by key, optionally with default
print("pop('age') ->", popped_age, "| person:", person)

last_pair = person.popitem()           # remove and return the last inserted (key, value) pair
print("popitem() ->", last_pair, "| person:", person)

# Delete by key (if exists)
if "email" in person:
    del person["email"]
    print("del person['email'] ->", person)

# Clear all items
copy_before_clear = person.copy()
person.clear()
print("Copy before clear:", copy_before_clear)
print("After clear:", person) 