# Dict examples: CRUD, lookup, frequency, JSON, grouping

# Creation
rec = {"id": 1, "name": "Prajjwal", "age": 30}

# CRUD operations
rec["email"] = "prajjwal@example.com"  # add/update
name = rec["name"]
age = rec.get("age")
exists = "name" in rec
removed_age = rec.pop("age", None)
length = len(rec)

# Frequency counting
items = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency = {}
for item in items:
    frequency[item] = frequency.get(item, 0) + 1

# Lookup table
lookup = {"USD": "United States Dollar", "EUR": "Euro", "JPY": "Japanese Yen"}
full_usd = lookup.get("USD")

# JSON interop
import json
payload = '{"name": "prajjwal", "age": 23, "city": "Prayagraj"}'
data = json.loads(payload)

# Grouping
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

if __name__ == "__main__":
    print("rec:", rec)
    print("exists name:", exists, "length:", length)
    print("frequency:", frequency)
    print("lookup USD:", full_usd)
    print("json name:", data["name"])
    print("grouped:", by_dept) 