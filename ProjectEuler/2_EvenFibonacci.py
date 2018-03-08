def fibonacci(n, a, b, fiter):
    if b < n:
        if fiter % 3 == 0:
            return b + fibonacci(n, b, a + b, fiter + 1)
        else:
            return fibonacci(n, b, a + b, fiter + 1)
    else:
        return 0

s = fibonacci(10, 1, 1, 2)
print(s)
