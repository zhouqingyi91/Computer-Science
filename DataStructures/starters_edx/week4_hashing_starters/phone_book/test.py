import random


def _hash(a, b, x, p, m):
    h = ((a * x + b) % p) % m
    return h


# print(_hash(34, 2, 1482567, 10000019, 1000))
# print((1482567 * 34 + 6) % 10000019)

print(random.randint())
