# Topic: Change List Items, Add Items (append/insert/extend), Remove Items (remove/pop/del/clear)
# Reference: https://www.w3schools.com/python/python_lists.asp
# This file mutates lists to show differences in operations and their effects.

nums = [10, 20, 30, 40, 50]
print(nums)

# Change item by index
nums[1] = 21  # replace 20 with 21
print("Change item by index : ", nums)

# Change a range (slice assignment)
nums[2:4] = [31, 41]  # replace elements at indices 2 and 3
print("Change a range (slice assignment) :", nums)

# Insert does not replace, it shifts the list to the right from the index
nums.insert(1, 15)  # insert 15 at index 1
print("Insert Operation : ", nums)

# Append adds to the end
nums.append(60)
print("Append Operation : ", nums)

# Extend merges another iterable, element by element
nums.extend([70, 80])
print("Extend Operation : ", nums)

# Remove by value (first matching value)
if 31 in nums:
    nums.remove(31)
    print("Remove by value (31) : ", nums)
else:
    print("Value 31 not found, skipping remove")

# Pop removes by index (default is last) and returns the removed element
popped_last = nums.pop()
print("Pop last ->", popped_last, "List:", nums)

popped_first = nums.pop(0)
print("Pop index 0 ->", popped_first, "List:", nums)

# del can delete by index or slice; here delete the item currently at index 0
# Caution: del does not return the removed element
if len(nums) > 0:
    print("Before del index 0:", nums)
    del nums[0]
    print("After del index 0:", nums)

# clear empties the list in-place
copy_before_clear = nums.copy()
nums.clear()
print("Copy before clear:", copy_before_clear)
print("After clear:", nums)

if __name__ == "__main__":
    print("copy_before_clear:", copy_before_clear)
    print("popped_last:", popped_last, "popped_first:", popped_first)
    print("after_clear nums:", nums) 