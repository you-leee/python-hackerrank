def special_pythagorean(n):
    max_mult = -1
    for a in range(1, n // 3 + 1):
        b = (n ** 2 - (2 * n * a)) // ((n - a) * 2)
        c = n - a - b
        if c ** 2 == a ** 2 + b ** 2:
            temp_mult = a * b * c
            if temp_mult > max_mult:
                max_mult = temp_mult

    return max_mult


print(special_pythagorean(12))
