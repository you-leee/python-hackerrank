# return date with the 256th day of the year in Russia
# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

def isLeapYear(year):
    if(year < 1918):
        return (year%4 == 0)
    else:
        return ((year%4 == 0 and year%100 != 0) or (year%400 == 0))

def solve(year):
    # Complete this function
    res_year = year
    res_month = 9
    res_day = 13
    if(year == 1918):
        res_day += 13
    elif(isLeapYear(year)):
        res_day += 1
    print("{:0>2}.{:0>2}.{}".format(res_day, res_month, res_year))

year = int(input().strip())
solve(year)
