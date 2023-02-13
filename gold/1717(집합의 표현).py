import sys
sys.setrecursionlimit(10**8)
n, m = map(int, sys.stdin.readline().split())
values = [i for i in range(n + 1)]


def find_value(x):
    if values[x] != x:
        values[x] = find_value(values[x])
    return values[x]


def union_value(a, b):
    a = find_value(a)
    b = find_value(b)
    if a < b:
        values[b] = a
    else:
        values[a] = b

for _ in range(m):
    command, a, b = map(int, sys.stdin.readline().split())
    if command == 0:
        union_value(a, b)
    else:
        if find_value(a) == find_value(b):
            print("YES")
        else:
            print("NO")