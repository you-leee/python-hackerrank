from collections import defaultdict

def bigSorting(len_map):
    lens = sorted(len_map.keys())

    for i in lens:
        e = len_map[i]
        e.sort()
        print("\n".join(map(str, e)))



if __name__ == "__main__":
    n = int(input().strip())
    arr = []

    len_map = defaultdict(list)

    for arr_i in range(n):
       arr_t = str(input().strip())
       len_map[len(arr_t)].append(arr_t)

    bigSorting(len_map)
