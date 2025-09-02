# Topic: Membership (in), Union, Intersection, Difference, Symmetric Difference
# Reference: https://www.w3schools.com/python/python_sets.asp

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A:", A)
print("B:", B)

# Membership
has_three = 3 in A
print("Membership -> 3 in A:", has_three)

# Set algebra
union = A | B            # elements in A or B
intersection = A & B     # elements common to A and B
difference = A - B       # elements in A but not in B
symdiff = A ^ B          # elements in A or B but not both

print("Union (A | B):", union)
print("Intersection (A & B):", intersection)
print("Difference (A - B):", difference)
print("Symmetric difference (A ^ B):", symdiff) 