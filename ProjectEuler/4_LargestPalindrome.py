def palindrome(n, palindromes):
    max = 10000
    for i in range(0, len(palindromes)):
        if (palindromes[i] >= n):
            return palindromes[i - 1]

    return max


def generatePalindromes():
    palindromes = []
    for i in range(100, 1000, 1):
        for j in range(i, 1000, 1):
            mult = i * j
            if isPalindrome(mult):
                palindromes.append(mult)

    return sorted(palindromes)


def isPalindrome(nr):
    rev = 0
    x = nr
    while x > 0:
        rev = 10 * rev + x % 10
        x = int(x / 10)
    return nr == rev


palindromes = generatePalindromes()
print(palindrome(101102, palindromes))
