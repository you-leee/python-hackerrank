# A flock of n birds is flying across the continent.
# Each bird has a type, and the different types are designated by the ID numbers 1, 2, 3, 4, and 5.

# Given an array of n integers where each integer describes the type of a bird in the flock,
#   find and print the type number of the most common bird.
# If two or more types of birds are equally common, choose the type with the smallest ID number.

import sys

def migratoryBirds(n, ar):
    counts = [0,0,0,0,0,0]
    for i in range(n):
        counts[ar[i]] += 1

    return counts.index(max(counts))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)