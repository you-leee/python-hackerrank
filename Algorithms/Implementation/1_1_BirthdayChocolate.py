# Lily has a chocolate bar consisting of a row of n squares where each square has an integer written on it.
# She wants to share it with Ron for his birthday, which falls on month m and day d.
# Lily wants to give Ron a piece of chocolate only if it contains m consecutive squares whose integers sum to d.

# Given m, d, and the sequence of integers written on each square of Lily's chocolate bar,
#   how many different ways can Lily break off a piece of chocolate to give to Ron?

import sys

def solve(n, s, d, m):
    count = 0

    c_sum = sum(s[0:m])
    if(c_sum == d):
        count += 1
    for i in range(1, n - m + 1):
        c_sum = c_sum - s[i - 1] + s[i + m - 1]
        if (c_sum == d):
            count += 1

    return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)