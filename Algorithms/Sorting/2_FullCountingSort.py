from collections import defaultdict

def fullCountingSort(count_map):
    counts = sorted(count_map.keys())

    for i in counts:
        e = count_map[i]
        print(" ".join(map(str, e)))



if __name__ == "__main__":
    elems = defaultdict(list)

    n = int(input().strip())
    ignore = n // 2
    for a0 in range(ignore):
        x, s = input().strip().split(' ')
        elems[int(x)].append("-")


    for a0 in range(ignore, n):
        x, s = input().strip().split(' ')
        elems[int(x)].append(str(s))


    fullCountingSort(elems)