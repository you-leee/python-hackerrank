import operator
import functools
from heapq import heappush, heappop


def largest_product_series(N, K, nums):
    digits = [int(d) for d in nums]
    if N == K:
        return functools.reduce(operator.mul, digits, 1)

    if K == 1:
        return max(digits)

    seq_max = 0

    for si in range(0, N - K + 1):
        temp_max = 1
        for i in range(si, K + si):
            temp_max *= digits[i]
        if temp_max > seq_max:
            seq_max = temp_max

    return seq_max


asd = largest_product_series(5, 2, "10345")
print(asd)

