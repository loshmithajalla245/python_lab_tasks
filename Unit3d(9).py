x = 10  # Global variable

def show():
    x = 20  # Local variable
    print("Local variable:", x)

show()
print("Global variable:", x)