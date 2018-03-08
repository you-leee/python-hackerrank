def generate_sum_of_squares():
    n = 10**4
    sos = [0, 1]
    for i in range(2,n+1):
        sos.append(sos[i-1] + i ** 2)

    return sos

def square_of_sums(n):
    return (n*(n+1)//2) ** 2

sos = generate_sum_of_squares()
print(square_of_sums(10) - sos[10])