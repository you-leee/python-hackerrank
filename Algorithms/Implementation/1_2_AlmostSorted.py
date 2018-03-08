def almostSorted(A, n):
    if n == 1:
        return "yes"

    if n == 2:
        return ("yes\nswap 1 2")

    s1, s2 = -1, -1
    canSwap, canReverse = True, True
    sorted = True
    r1, r2 = -1, -1
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            sorted = False

            # swap
            if s1 == -1:
                s1 = i
            elif (s1 != -1 and s2 == -1):
                s2 = i + 1
            else:
                canSwap = False

            # reverse
            if r1 == -1:
                r1 = i
                r2 = i + 1
            elif (r1 != -1 and r2 == i):
                r2 = i + 1
            else:
                canReverse = False

    if sorted:
        return "yes"

    if (canSwap):
        # check swapping
        if(s2 == -1):
            s2 = s1 + 1
        if(s2 == (n-1)):
            if(s1 == 0):
                return("yes\nswap {} {}".format(s1 + 1, s1 + 2))
            elif(checkBefore(A, s1, s2)):
                return ("yes\nswap {} {}".format(s1 + 1, s2 + 1))
        elif(s1 == 0):
            if(checkAfter(A, s1, s2)):
                return("yes\nswap {} {}".format(s1 + 1, s2 + 1))
        elif(checkBefore(A, s1, s2) and checkAfter(A, s1, s2)):
            return ("yes\nswap {} {}".format(s1 + 1, s2 + 1))
    if (canReverse):
        # check reversing
        if (r2 == (n - 1)):
            if(r1 == 0):
                return ("yes\nreverse {} {}".format(r1 + 1, r2 + 1))
            elif(checkBefore(A, r1, r2)):
                return ("yes\nreverse {} {}".format(r1 + 1, r2 + 1))
        elif(r1 == 0):
            if(checkAfter(A, r1, r2)):
                return ("yes\nreverse {} {}".format(r1 + 1, r2 + 1))
        else:
            if(checkBefore(A, r1, r2) and checkAfter(A, r1, r2)):
                return ("yes\nreverse {} {}".format(r1 + 1, r2 + 1))

    return ("no")

def checkBefore(A, i, j):
    return A[i - 1] < A[j]

def checkAfter(A, i, j):
    return A[i] < A[j + 1]

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(almostSorted(arr, n))
