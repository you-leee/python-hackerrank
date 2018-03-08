# https://www.hackerrank.com/challenges/queens-attack-2/problem

def movesNum(n, r_q, c_q):
    center = ((n + 1) / 2)
    diff_from_center = max(abs(center - r_q), abs(center - c_q))
    moves = ((n - 1) * 4) - (2 * diff_from_center)

    return moves


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    r_q, c_q = input().strip().split(' ')
    r_q, c_q = [int(r_q), int(c_q)]

    moves = movesNum(n, r_q, c_q)
    for obstacles_i in range(k):
        o = [int(obstacles_temp) for obstacles_temp in input().strip().split(' ')]
        if (o[1] == c_q):  # up-down
            moves -= c_q - abs(c_q - o[1])
        elif (o[0] == r_q):  # left-right
            moves -= r_q - abs(r_q - o[0])
        elif (abs(o[0] - r_q) == abs(o[1] - c_q)):  # diagonals
            moves -= abs(r_q - o[0])
    print(moves)
