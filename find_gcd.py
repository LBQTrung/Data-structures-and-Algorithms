def calc_gcd(a , b):
    if (b == 0):
        return a
    return calc_gcd(b , a%b)
print(calc_gcd(12, 10))