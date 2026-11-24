student = {"name": "Krishna", "age": 20, "course": "Python"}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Get:", student.get("name"))

student.update({"age": 21})
print("Updated:", student)

student.pop("course")
print("After pop:", student)