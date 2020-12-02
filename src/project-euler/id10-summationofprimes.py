import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes_below(max):
    total = 0
    for i in range(max):
        if is_prime(i):
            total += i
    return total

print(sum_of_primes_below(2000000))





# [Sieve Example]
# def sumPrimes(n):
#     sum, sieve = 0, [True] * n
#     for p in range(2, n):
#         if sieve[p]:
#             sum += p
#             for i in range(p*p, n, p):
#                 sieve[i] = False
#     return sum
#
# print sumPrimes(2000000)

