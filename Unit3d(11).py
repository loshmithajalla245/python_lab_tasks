balance = 1000

def deposit(amount):
    global balance
    balance += amount

def local():
    balance = 500
    balance += 200
    print("Local balance:", balance)

deposit(500)
print("Global balance:", balance)

local()
print("Final balance:", balance)