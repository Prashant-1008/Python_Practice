## 4 September 2025 – Questions

### Overview
This folder contains three Python problems with clean, idiomatic solutions and double-quoted JSON outputs.

### Environment
- Python 3.8+

### How to Run
```bash
python3 questions/first.py
python3 questions/second.py
python3 questions/third.py
```

### Problem 1 – Flatten Nested Dict Keys
- **Goal**: Flatten nested dict keys using a separator `.`.
- **Approach**: DFS recursion; store results in `collections.defaultdict(dict)`; print with `json.dumps(...)` for double quotes.
- **File**: `questions/first.py`
- **Example Output**:
```text
Output: {"a": 1, "b.c": 2, "b.d.e": 3}
```

### Problem 2 – Group by Key in One Line
- **Goal**: Group list of `(key, value)` pairs by key.
- **Approach**: `collections.defaultdict(list)` with a single pass; print with `json.dumps(...)`.
- **File**: `questions/second.py`
- **Example Output**:
```text
Output: {"fruit": ["apple", "mango"], "veg": ["carrot", "peas"]}
```

### Problem 3 – Dict Key Collapsing with Tuples
- **Goal**: Convert flat dict with tuple keys `(outer, inner)` into a nested dict.
- **Approach**: `collections.defaultdict(dict)`, tuple unpacking in one pass; prints with `json.dumps(...)`.
- **File**: `questions/third.py`
- **Example Output**:
```text
Output: {"A": {"X": 1, "Y": 2}, "B": {"X": 3}}
```

### Notes
- Outputs use double quotes via `json.dumps(...)` for readability and consistency.
- Code favors O(n) single-pass solutions and idiomatic Python constructs (`defaultdict`, recursion, tuple unpacking). 