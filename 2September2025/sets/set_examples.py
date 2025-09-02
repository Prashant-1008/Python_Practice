# Set examples: creation, CRUD, membership, algebra

# Creation
s = {1, 2, 3}
empty_set = set()  # {} would be an empty dict

# CRUD
s.add(4)
s.discard(2)  # safe if absent
removed = None
if 3 in s:
    s.remove(3)  # may raise if absent

# Membership and length
has_one = 1 in s
length = len(s)

# Algebra
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
union = A | B
intersection = A & B
difference = A - B
symdiff = A ^ B

# Deduplication & membership testing
items = ["apple", "banana", "apple", "orange", "banana"]
unique = set(items)

banned = {"knife", "gun", "drugs"}
item = "knife"
prohibited = item in banned

if __name__ == "__main__":
    print("s:", s, "has_one:", has_one, "length:", length)
    print("union:", union, "intersection:", intersection)
    print("difference:", difference, "symdiff:", symdiff)
    print("unique:", unique)
    print("prohibited:", prohibited) 