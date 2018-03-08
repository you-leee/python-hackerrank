# https://www.hackerrank.com/challenges/append-and-delete/problem

def appendAndDelete(s, t, k):
    s_len = len(s)
    t_len = len(t)
    if (s_len + t_len) <= k:
        return "Yes"

    # Find number of letters in common subsequence from begin of str
    for i in range(min(s_len, t_len)):
        steps_required = s_len + t_len - (i * 2)
        if steps_required == k:
            return "Yes"
        elif steps_required < k:
            return "No"
        if (s[i] != t[i]):
            break

    return "No"



if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)