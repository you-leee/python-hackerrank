# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

def catAndMouse(x, y, z):
    a = abs(z - x)
    b = abs(z - y)
    if(a < b):
        print("Cat A")
    elif(b < a):
        print("Cat B")
    else:
        print("Mouse C")

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        catAndMouse(x, y, z)
