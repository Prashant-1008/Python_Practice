# Problem 1 – Flatten Nested Dict Keys

# Write a function flatten_dict(d, parent_key="", sep=".") that flattens a nested dictionary.
# The nested keys should be joined into a single key using the separator (default ".").

# Example:
# Input: {"a": 1, "b": {"c": 2, "d": {"e": 3}}}
# Output: {"a": 1, "b.c": 2, "b.d.e": 3

import collections
import json # to dump the dictionary to a json string , it is a built-in module taaki humein output "" way me aaye naa ki '' way me

input_dict = {"a": 1, "b": {"c": 2, "d": {"e": 3}}}

res = collections.defaultdict(dict)

def flatten_dict(d, parent_key="", sep="."):
    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flatten_dict(value, new_key, sep=sep)
        else:
            res[new_key] = value

flatten_dict(input_dict)

print("Output:", json.dumps(dict(res)))