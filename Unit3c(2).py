# Create a set
A = {10, 20, 30, 40}

print("Original Set:", A)

# Membership testing
print("Is 20 present?", 20 in A)
print("Is 50 present?", 50 in A)

# Add an element
A.add(50)
print("After add:", A)

# Remove an element
A.remove(30)
print("After remove:", A)

# Discard an element
A.discard(60)
print("After discard:", A)