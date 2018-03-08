primes = [2,3,5,7]

def nth_prime(n):
    l = len(primes)
    if n <= l:
        return primes[n-1]
    i = primes[l-1] + 2
    while len(primes) < n:
        while not is_prime(i):
            i += 2
        primes.append(i)

    return primes[n-1]

def is_prime(n):
    for p in primes:
        if n % p == 0:
            return False
    return True


print(nth_prime(3))
print(nth_prime(5))
print(nth_prime(10))



