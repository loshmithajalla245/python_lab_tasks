dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

result = dict1.copy()
result.update(dict2)

print("Merged Dictionary:", result)
print("Original Dictionary:", dict1)