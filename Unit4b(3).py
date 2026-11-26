try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter an integer.")
else:
    print("Square:", num ** 2)
finally:
    print("Program finished")