# Topic: Sort Lists, Copy Lists, Join Lists
# Reference: https://www.w3schools.com/python/python_lists_sort.asp and related list pages
# Demonstrate sort(), sorted(), reverse, custom keys, copying (shallow), concatenation and extend.

names = ["Zara", "bob", "Alice", "mike"]
nums = [5, 1, 9, 2, 5, 10]

print("Original names:", names)
print("Original nums:", nums)

# In-place sort (default ASCIIbetical, case-sensitive)
names_case_sensitive = names.copy()
names_case_sensitive.sort()
print("Case-sensitive sort:", names_case_sensitive)

# Case-insensitive sort using key=str.lower
names_case_insensitive = names.copy()
names_case_insensitive.sort(key=str.lower)
print("Case-insensitive sort:", names_case_insensitive)

# Reverse order
nums_desc = nums.copy()
nums_desc.sort(reverse=True)
print("Nums sorted desc:", nums_desc)

# Using sorted() returns a new list and leaves original intact
nums_sorted_new = sorted(nums)
print("sorted(nums) -> new list:", nums_sorted_new)
print("Original nums unchanged:", nums)

# Copying lists (shallow copies)
copy_via_slice = nums[:]
copy_via_list = list(nums)
copy_via_copy = nums.copy()
print("Copies (slice/list()/copy()):", copy_via_slice, copy_via_list, copy_via_copy)

# Join/concatenate
joined_plus = names + ["Nina", "Omar"]
joined_extend = names.copy()
joined_extend.extend(["Nina", "Omar"])
print("Joined via +:", joined_plus)
print("Joined via extend():", joined_extend)

# Pitfall: copying nested lists still shares inner lists (shallow)
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
print("Before shallow modification -> nested:", nested, "shallow:", shallow)
shallow[0][0] = 999  # affects nested[0][0] as well
print("After shallow modification -> nested:", nested, "shallow:", shallow) 