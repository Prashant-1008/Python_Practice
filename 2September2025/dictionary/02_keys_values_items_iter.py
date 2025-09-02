# Topic: keys(), values(), items(), Iteration, Membership
# Reference: https://www.w3schools.com/python/python_dictionaries.asp

user = {"id": 101, "name": "Aryan", "role": "admin"}

# Retrieve views (cast to list for a snapshot)
keys_view = list(user.keys())
values_view = list(user.values())
items_view = list(user.items())

print("keys():", keys_view)
print("values():", values_view)
print("items():", items_view)

print("-- Iterate keys --")
for k in user:
    print("key:", k)

print("-- Iterate items --")
for k, v in user.items():
    print("item:", k, v)

# Membership checks look into keys by default
has_id = "id" in user
has_email = "email" in user
print("Membership -> 'id' in user:", has_id, "; 'email' in user:", has_email) 