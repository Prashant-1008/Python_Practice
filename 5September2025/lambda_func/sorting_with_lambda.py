students = [
    {"name": "Alice", "age": 24, "score": 88},
    {"name": "Bob", "age": 22, "score": 95},
    {"name": "Charlie", "age": 23, "score": 78},
]

by_age = sorted(students, key=lambda s: s["age"]) 
by_score_desc = sorted(students, key=lambda s: s["score"], reverse=True)
by_name = sorted(students, key=lambda s: s["name"].lower())

if __name__ == "__main__":
    print("by_age:", by_age)
    print("by_score_desc:", by_score_desc)
    print("by_name:", by_name) 