# Problem 2 – Group by Key in One Line

# You are given a list of key–value pairs. Build a dictionary that groups values by their keys.

# Example:
# Input: [("fruit", "apple"), ("fruit", "mango"), ("veg", "carrot"), ("veg", "peas")]
# Output: {"fruit": ["apple", "mango"], "veg": ["carrot", "peas"]}

# Constraints:

# Use idiomatic Python (defaultdict, setdefault, or dict comprehension).

# Avoid writing explicit nested loops.


from collections import defaultdict
import json

input_dict = [("fruit", "apple"), ("fruit", "mango"), ("veg", "carrot"), ("veg", "peas")]

res = defaultdict(list)
print(res) # defaultdict(<class 'list'>, {}) for empty list
for key, value in input_dict:
    res[key].append(value)

print("Output:", json.dumps(dict(res)))

