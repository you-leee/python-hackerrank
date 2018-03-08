def larrysArray(A, n):
    perms = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                perms += 1

    if perms%2 == 0:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        A = list(map(int, input().strip().split(' ')))
        result = larrysArray(A, n)
        print(result)