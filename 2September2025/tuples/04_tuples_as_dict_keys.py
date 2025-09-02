# Topic: Tuples as Dictionary Keys (hashable if elements are hashable)
# Reference: https://www.w3schools.com/python/python_tuples.asp

# Coordinates (tuple) as keys mapping to a value
location_to_city = {
    (28.6139, 77.2090): "New Delhi",
    (19.0760, 72.8777): "Mumbai",
}

print("Dictionary with tuple keys:", location_to_city)

delhi = location_to_city[(28.6139, 77.2090)]
print("Lookup (28.6139,77.2090):", delhi)

print("All key/value pairs:")
for k, v in location_to_city.items():
    print(" ", k, "->", v) 