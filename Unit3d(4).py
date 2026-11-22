
def simple_interest(principal, time, rate=5):
    interest = (principal * time * rate) / 100
    return interest

# Calling with the default rate (5%)
si1 = simple_interest(1000, 2)
print("Simple Interest (Default Rate):", si1)

# Calling with an explicit rate (10%)
si2 = simple_interest(1000, 2, 10)
print("Simple Interest (Explicit Rate):", si2)
