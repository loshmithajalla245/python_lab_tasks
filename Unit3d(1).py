# Define a function
def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

# Get values
l = 10
b = 5

# Call the function
a, p = rectangle(l, b)

# Display results
print("Area of rectangle:", a)
print("Perimeter of rectangle:", p)