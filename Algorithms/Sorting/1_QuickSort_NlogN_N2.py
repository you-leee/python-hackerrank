def quickSort(arr):
    n_elems = len(arr)

    if(n_elems == 0):
        return []
    if(n_elems == 1):
        return arr

    pivot = arr[n_elems//2]
    left = []
    equal = []
    right = []
    for a in arr:
        if(a < pivot):
            left.append(a)
        elif(a == pivot):
            equal.append(a)
        else:
            right.append(a)

    return quickSort(left) + equal + quickSort(right)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = quickSort(arr)
    print (" ".join(map(str, result)))