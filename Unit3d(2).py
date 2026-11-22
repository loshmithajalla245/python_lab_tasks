# Define a function
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Call the function
c = 25
f = celsius_to_fahrenheit(c)

# Display result
print("Temperature in Celsius:", c)
print("Temperature in Fahrenheit:", f)