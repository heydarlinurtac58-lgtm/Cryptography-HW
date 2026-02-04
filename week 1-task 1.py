def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

print(gcd(12,28))