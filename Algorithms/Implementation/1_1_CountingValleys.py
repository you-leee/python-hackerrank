# https://www.hackerrank.com/challenges/counting-valleys/problem


def getCounts(n, s):
    level = 0
    count = 0
    for step in s:
        if(step == "U"): level += 1
        else: level -= 1

        if(level == 0 and step == "U"):
            count += 1

    return count

def countingValleys(n, s):
    if(n == 2):
        return 0
    counts = getCounts(n, s)
    return counts

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)