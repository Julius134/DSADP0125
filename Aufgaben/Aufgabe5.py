from math import sqrt

def is_prime(n):
    return all(n % i != 0 for i in range(2, (int(sqrt(n))+1)))
    
primes = []

for i in range(1, 1001):
    if is_prime(i):
        primes.append(i)

print(primes)