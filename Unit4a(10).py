students = [
    {"name": "Krishna", "marks": 90},
    {"name": "Ravi", "marks": 75},
    {"name": "Priya", "marks": 85}
]

print("Ascending:")
print(sorted(students, key=lambda x: x["marks"]))

print("Descending:")
print(sorted(students, key=lambda x: x["marks"], reverse=True))