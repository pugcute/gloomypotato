import sys
sys.setrecursionlimit(10**9)
N, M = map(int, input().split())

dp = [[10**9] * 10001 for _ in range(101)]

def get_count(x, y):
    if x > y:
        return get_count(y, x)
    if y % x == 0:
        return int(y / x)
    checker = y / x
    ret = 10 ** 9
    if checker >= 3:
        ret = min(ret, get_count(x, y - x) + 1)
    else:
        for i in range(1, int(x / 2) + 1):
            ret = min(ret, get_count(x - i, y) + get_count(i, y))
        for j in range(1, int(y // 2) + 1):
            ret = min(ret, get_count(x, y - j) + get_count(x, j))

    return ret

print(get_count(min(N, M), max(N, M)))