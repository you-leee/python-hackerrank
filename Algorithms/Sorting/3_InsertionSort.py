#!/bin/python3

import sys


def insertion_sort(arr):
    steps = 0
    bit = [0] * 10000001
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]

        updatebit(bit, 10000001, num, 1)

        steps += getsum(bit, num)

    return steps


def updatebit(BITTree, n, i, v):
    # index in BITree[] is 1 more than the index in arr[]
    i += 1

    # Traverse all ancestors and add 'val'
    while i <= n:
        # Add 'val' to current node of BI Tree
        BITTree[i] += v

        # Update index to that of parent in update View
        i += i & (-i)


def getsum(BITTree, i):
    s = 0  # initialize result

    # Traverse ancestors of BITree[index]
    while i > 0:
        # Add current element of BITree to sum
        s += BITTree[i]

        # Move index to parent node in getSum View
        i -= i & (-i)
    return s


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = insertion_sort(arr)
        print(result)

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = insertion_sort(arr)
        print(result)
