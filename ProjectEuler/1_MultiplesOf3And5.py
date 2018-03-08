from itertools import chain

p1 = [0, 3, 5, 6, 9]
p2 = [0, 2, 5, 8]
p3 = [0, 1, 4, 5, 7]
ps = [23, 15, 17]
psum = sum(ps)


def sumOfMultiples_1(num):
    return sum(set(chain(range(0, num, 3), range(0, num, 5))))


def sumOfMultiples(num):
    k1 = (num - 1) // 3
    k2 = (num - 1) // 5
    k3 = (num - 1) // 15
    return 3 * k1 * (k1 + 1) // 2 + 5 * k2 * (k2 + 1) // 2 - 15 * k3 * (k3 + 1) // 2


print(sumOfMultiples(100))
