# Topic: Tuple Methods (count, index), Membership, Looping
# Reference: https://www.w3schools.com/python/python_tuples_methods.asp

colors = ("red", "green", "blue", "red")

print("Tuple:", colors)

# Methods
num_red = colors.count("red")
idx_green = colors.index("green")
print("count('red') ->", num_red)
print("index('green') ->", idx_green)

# Membership and iteration
has_blue = "blue" in colors
print("Membership -> 'blue' in colors:", has_blue)

print("Looping over tuple:")
for c in colors:
    print(" -", c)
 