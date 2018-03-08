from collections import defaultdict


def distinctGraphsCount(countries, n):
    counts = []
    explored = [0] * n
    explored_count = 0
    combinations = 0
    singles_count = 0

    for i in range(n):
        if explored[i] == 0:
            if countries[i] == []:
                singles_count += 1
            else:
                count_i = len(dfsUtil(countries, explored, explored_count, i, n))
                for c in range(len(counts) - 1, -1, -1):
                    combinations += (count_i * counts[c])
                counts.append(count_i)

        if explored_count == n:
            break

    combinations += singles_count - 1
    for count in counts:
        combinations += singles_count * count

    return combinations


def dfsUtil(cities, explored, explored_count, v, n):
    queue = [v]
    neighbours = []

    while queue:
        node = queue.pop(0)
        if explored[node] == 0:
            explored[node] = 1
            neighbours.append(node)
            explored_count += 1

            for i in cities[node]:
                if (explored[i] == 0):
                    queue.append(i)

    return neighbours


def journeyToMoon(n, countries):
    combinations = distinctGraphsCount(countries, n)

    return combinations


if __name__ == "__main__":
    n, p = input().strip().split(' ')
    n, p = [int(n), int(p)]

    countries = defaultdict(list)
    for i in range(p):
        c_p = [int(c_temp) for c_temp in input().strip().split(' ')]
        countries[c_p[0]].append(c_p[1])
        countries[c_p[1]].append(c_p[0])
    result = journeyToMoon(n, countries)
    print(result)