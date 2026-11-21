n = int(input("Enter how many numbers: "))

largest = 0

for i in range(n):
    num = int(input("Enter a number: "))

    if i == 0 or num > largest:
        largest = num

print("Largest number =", largest)
