primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

def max_k_prime(n, prime):
    i = 2
    while n >= prime ** i:
        i += 1

    return prime ** (i - 1)


def sum_prime_power(n):
    sum = 1
    for p in primes:
        if p > n:
            break
        sum *= max_k_prime(n, p)
    return sum

print(sum_prime_power(10))
