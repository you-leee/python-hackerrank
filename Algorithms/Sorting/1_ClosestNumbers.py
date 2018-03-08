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


def closestNumbers(arr):
    sorted_arr = quickSort(arr)

    min_diff = 2 * 10 * 10 * 10 * 10 * 10 * 10 * 10
    pairs = []
    for i in range(len(arr) - 1):
        diff = abs(sorted_arr[i] - sorted_arr[i + 1])
        if (diff <= min_diff):

            if (diff < min_diff):
                pairs = []
                min_diff = diff

            pairs.append(sorted_arr[i])
            pairs.append(sorted_arr[i + 1])

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = closestNumbers(arr)
    print (" ".join(map(str, result)))