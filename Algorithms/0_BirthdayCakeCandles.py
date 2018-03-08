# You are in-charge of the cake for the birthday and have decided the cake will have one candle for each year of her age.
# When she blows out the candles, she’ll only be able to blow out the tallest ones.
# Your task is to find out how many candles she can successfully blow out.

# For example, if your niece is turning 4 years old, and the cake will have candles of height 3, 2, 1, 3,
#   she will be able to blow out candles successfully, since the tallest candle is of height and there are such candles.


import sys

def birthdayCakeCandles(n, ar):
    max = ar[0]
    max_count = 1
    for i in range(1, n):
        if(ar[i] == max):
            max_count += 1
        elif(ar[i] > max):
            max = ar[i]
            max_count = 1

    return max_count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)