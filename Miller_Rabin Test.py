#Miller Rabin Test
def miller_rabin_prime_test(n):
    from math import pow
    if testee == n-1:
        return True
    else:
        testee = pow(testee, 2, n)
    return False
