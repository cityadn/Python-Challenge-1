def simple_prime_test(n):
    "Tests n for primality by checking potential factors"
    from math import sqrt
    for r in range(2,int(sqrt(n))+1):
        if n % r == 0:
            return False
    return True


