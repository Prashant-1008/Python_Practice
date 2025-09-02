# Topic: Set Methods — isdisjoint, issubset, issuperset, copy, *_update variants
# Reference: https://www.w3schools.com/python/python_sets_methods.asp

A = {1, 2}
B = {1, 2, 3}
C = {4, 5}

# Relationship checks
is_A_subset_B = A.issubset(B)
is_B_superset_A = B.issuperset(A)
is_B_disjoint_C = B.isdisjoint(C)

print("A:", A)
print("B:", B)
print("C:", C)
print("A.issubset(B):", is_A_subset_B)
print("B.issuperset(A):", is_B_superset_A)
print("B.isdisjoint(C):", is_B_disjoint_C)

# Copy
A_copy = A.copy()
print("A.copy():", A_copy)

# Update variants mutate the set in-place
X = {1, 2, 3}
X.difference_update({2})           # remove 2 from X -> {1,3}
print("After X.difference_update({2}):", X)

Y = {1, 2, 3}
Y.intersection_update({2, 3, 5})   # keep only intersection -> {2,3}
print("After Y.intersection_update({2,3,5}):", Y)

Z = {1, 2, 3}
Z.symmetric_difference_update({2, 3, 4})  # -> {1,4}
print("After Z.symmetric_difference_update({2,3,4}):", Z) 