# Define a function
def calculate_marks(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

# Call the function
a, b, c = 80, 90, 70
total, average = calculate_marks(a, b, c)

# Display results
print("Total Marks:", total)
print("Average Marks:", average)