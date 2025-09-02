# Topic: Create Sets, Add Items, Remove Items (remove/discard/pop/clear)
# Reference: https://www.w3schools.com/python/python_sets.asp
# Sets are unordered, unindexed, unique elements only.

s = {"apple", "banana", "cherry"}
empty_set = set()  # {} would be an empty dict
print("Initial set:", s)

# Add single item
s.add("date")
print("After add('date'):", s)

# Add multiple items from an iterable
s.update(["elderberry", "fig", "grape"])  # order of insertion is not preserved for display
print("After update([...]):", s)

# Remove by value (raises KeyError if missing)
if "banana" in s:
    s.remove("banana")
    print("After remove('banana'):", s)
else:
    print("'banana' not in set; skipping remove")

# Discard by value (safe if missing)
s.discard("kiwi")  # no error even if it is not present
print("After discard('kiwi'):", s)

# Pop removes and returns an arbitrary element (not the 'last')
popped = None
if s:
    popped = s.pop()
print("pop() returned:", popped, "| set now:", s)

# Clear removes all items
copy_before_clear = s.copy()
s.clear()
print("Copy before clear:", copy_before_clear)
print("After clear:", s) 