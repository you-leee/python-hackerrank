# https://www.hackerrank.com/challenges/electronics-shop/problem


def getMoneySpent(keyboards, drives, s):
    # Complete this function
    max_s = -1
    for keyb in keyboards:
        if(keyb >= s):
            continue
        for drive in drives:
            if(drive >= s):
                continue
            if(drive + keyb) <= s and (drive + keyb) > max_s:
                max_s = drive + keyb

    return max_s

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))

#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)