# Topic: List Comprehension (expressions, filtering), conditional expressions
# Reference: https://www.w3schools.com/python/python_lists_comprehension.asp (concept aligns with list page subsections)
# Compact yet readable list comprehensions. Prefer clarity over cleverness.

nums = [1, 2, 3, 4, 5, 6]

# Basic transform: square each number
squares = [n * n for n in nums]

# Filter: keep only even numbers
only_even = [n for n in nums if n % 2 == 0]

# Transform + filter: square only if even
even_squares = [n * n for n in nums if n % 2 == 0]

# Conditional expression inside comprehension: label even/odd
labels = ["even" if n % 2 == 0 else "odd" for n in nums]

# From string to list of uppercase words (split -> map -> filter non-empty)
sentence = "  Learn Python lists quickly  "
words_upper = [w.upper() for w in sentence.split() if w]

print("nums:", nums)
print("Squares:", squares)
print("Only even:", only_even)
print("Even squares:", even_squares)
print("Labels (even/odd):", labels)
print("Words upper:", words_upper) 