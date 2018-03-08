from collections import defaultdict

def distinctGraphsCount(cities, n):
    counts = []
    explored = [0]*n
    explored_count = 0
    for i in range(n):
        if explored[i] == 0:
            counts.append(dfsUtil(cities, explored,explored_count, i, n))
        if explored_count == n:
            break

    return counts

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
                if(explored[i] == 0):
                    queue.append(i)

    return neighbours

def roadsAndLibraries(n, c_lib, c_road, cities):
    if(c_lib <= c_road):
        return n*c_lib

    cost = 0
    distintCounts = distinctGraphsCount(cities, n)
    for count in distintCounts:
        cost += (c_lib + ((len(count) - 1)*c_road))

    return cost

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m, c_lib, c_road = input().strip().split(' ')
        n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]

        cities = defaultdict(list)
        for cities_i in range(m):
           cities_t = [int(cities_temp) - 1 for cities_temp in input().strip().split(' ')]
           cities[cities_t[0]].append(cities_t[1])
           cities[cities_t[1]].append(cities_t[0])
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(result)