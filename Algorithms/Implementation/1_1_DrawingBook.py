# Brie’s Drawing teacher asks her class to open their n-page book to page number p.
# Brie can either start turning pages from the front of the book (i.e., page number 1)
#   or from the back of the book (i.e., page number n),
#   and she always turns pages one-by-one (as opposed to skipping through multiple pages at once).
# When she opens the book, page is always on the right side:
# Given and n,p find and print the minimum number of pages Brie must turn in order to arrive at page p.


def solve(n, p):
    if(p <= n//2):
        return (p//2)
    else:
        if(n%2 == 0):
            return ((n - p + 1) // 2)
        else:
            return ((n - p) // 2)


n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)