# Problem 3 – Dict Key Collapsing with Tuples

# You are given a dictionary whose keys are tuples of the form (outer_key, inner_key).
# Restructure it into a nested dictionary.

# Example:
# Input: {("A", "X"): 1, ("A", "Y"): 2, ("B", "X"): 3}
# Output: {"A": {"X": 1, "Y": 2}, "B": {"X": 3}}

# Hint:

# Think about tuple unpacking (for outer, inner in d).

# Consider using defaultdict(dict) for cleaner code.

import collections
import json

input_dict = {("A", "X"): 1, ("A", "Y"): 2, ("B", "X"): 3}


def collapse_tuple_keys(flat_dict, /):   # / is a positional-only parameter
    res = collections.defaultdict(dict)
    for (outer_key, inner_key), value in flat_dict.items():
        res[outer_key][inner_key] = value
    return res


res = collapse_tuple_keys(input_dict)
print("Output:", json.dumps(dict(res)))