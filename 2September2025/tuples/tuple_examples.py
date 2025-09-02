# Tuple examples: creation, unpacking, usage as dict keys, returns

# Creation
coords = (10, 20)
singleton = (42,)  # must include comma
mixed = (1, "two", 3.0, True)

# Unpacking
x, y = coords
first = coords[0]
length = len(coords)

# Function returning multiple values via a tuple

def min_max(values: list[int]) -> tuple[int, int]:
    return min(values), max(values)

mm = min_max([3, 1, 9, 4])

# Tuple as dictionary keys
edges_to_weight = {
    ("A", "B"): 5,
    ("B", "C"): 7,
}

if __name__ == "__main__":
    print("coords:", coords, "x:", x, "y:", y)
    print("singleton:", singleton, "mixed:", mixed)
    print("first:", first, "length:", length)
    print("min_max:", mm)
    print("edge AB weight:", edges_to_weight[("A", "B")]) 