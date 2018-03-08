def countingSort(arr):
    result = [0]*100
    for a in arr:
        result[a] += 1

    return result

def printResult(counts):
    for i, c in enumerate(counts):
        if(c != 0):
            print(" ".join(map(str, [i] *c)), end=" ")

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    printResult(result)
