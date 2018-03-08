primes = [2,3,5,7]
sum_primes = sum(primes)

def sumOfPrimes(n):
    temp_sum = sum_primes
    if n >= sum_primes:
        i = len(primes) - 1
        while n > temp_sum:
            temp_sum -= primes[i]
            i -= 1
        return temp_sum

    # Find additional primes
