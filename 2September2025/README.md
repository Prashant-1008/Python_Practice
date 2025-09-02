# 2 September 2025 — Python Built-in Collections

Today we learned the differences, properties, and practical applications of Python's core collection types: lists, tuples, sets, and dictionaries.

Reference used: `https://www.geeksforgeeks.org/python/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/`

## What we covered
- Lists: ordered, mutable sequences with duplicates
- Tuples: ordered, immutable sequences with duplicates
- Sets: unordered, mutable containers of unique elements
- Dictionaries: ordered (3.7+), mutable mappings of unique keys to values

## Quick comparison

| Type        | Ordered | Mutable | Duplicates | Literal | Primary Use |
|-------------|---------|---------|------------|---------|-------------|
| List        | Yes     | Yes     | Yes        | `[ ]`   | Dynamic arrays; iteration, stacks/queues |
| Tuple       | Yes     | No      | Yes        | `( )`   | Fixed records, multiple returns, dict keys |
| Set         | No      | Yes     | No         | `{ }`   | Uniqueness, membership, set algebra |
| Dictionary  | Yes     | Yes     | Keys: No   | `{k:v}` | Fast lookups, structured records |

Notes:
- `{}` creates an empty dict; use `set()` for an empty set
- Dicts preserve insertion order in Python 3.7+
- Tuples are hashable if their elements are hashable (enables using them as dict keys)

## Learn by examples
- `lists/` — README and `list_examples.py`
- `tuples/` — README and `tuple_examples.py`
- `sets/` — README and `set_examples.py`
- `dictionary/` — README and `dict_examples.py`

## Practice prompts
- Convert a list with duplicates into a set, then back to a list to deduplicate
- Use a tuple as a key in a dict mapping `(row, col)` to a value in a grid
- Count word frequencies from a sentence using a dictionary
- Compute union, intersection, and difference of two sets of user IDs

## Why these data structures
- Lists for flexible, indexable sequences that grow/shrink
- Tuples for safety (immutability) and hashability
- Sets for fast membership and deduplication
- Dictionaries for O(1) average lookups and expressing structured data 