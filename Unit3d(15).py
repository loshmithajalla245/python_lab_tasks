from functools import reduce

a = [1, 2, 3, 4, 5]

print("Map:", list(map(lambda x: x*2, a)))

print("Filter:", list(filter(lambda x: x%2 == 0, a)))

print("Reduce:", reduce(lambda x, y: x+y, a))
