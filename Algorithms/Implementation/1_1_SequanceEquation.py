def permutationEquation(p, n):
    result = []

    for i in range(1, n+1):
        result.append(p[(p[i])])

    return result

if __name__ == "__main__":
    n = int(input().strip())
    p = dict(zip(list(map(int, input().strip().split(' '))), range(1, n+1)))
    result = permutationEquation(p, n)
    print ("\n".join(map(str, result)))