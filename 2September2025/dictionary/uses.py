# Uses of Python Dictionaries — Demonstrations
# Reference: https://www.geeksforgeeks.org/python/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/
# Notes:
# - Dictionaries map unique keys to values; ordered since Python 3.7; mutable.
# - Common applications: representing records, frequency counting, fast lookups,
#   JSON interop, and grouping by keys.

print("--- 1) Database Record Representation ---")
rec = {
    'id': 1,
    'name': 'Prajjwal',
    'email': 'prajjwal@example.com',
    'age': 30
}
print("rec['name'] ->", rec['name'])

print("--- 2) Counting Frequency of Elements ---")
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1
print("frequency:", freq)

print("--- 3) Fast Lookup Tables ---")
lookup = {
    'USD': 'United States Dollar',
    'EUR': 'Euro',
    'JPY': 'Japanese Yen'
}
print("lookup.get('USD') ->", lookup.get('USD'))

print("--- 4) Storing and Accessing JSON Data ---")
import json
payload = '{"name": "prajjwal", "age": 23, "city": "Prayagraj"}'
data = json.loads(payload)
print("data['name'] ->", data['name'])

print("--- 5) Grouping Data by Keys ---")
emps = [
    {'name': 'prajj', 'dept': 'HR'},
    {'name': 'brij', 'dept': 'IT'},
    {'name': 'kareena', 'dept': 'HR'},
    {'name': 'aryan', 'dept': 'IT'}
]
by_dept = {}
for emp in emps:
    by_dept.setdefault(emp['dept'], []).append(emp['name'])
print("grouped by dept:", by_dept) 