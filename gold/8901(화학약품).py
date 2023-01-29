import sys


N = int(input())
for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    AB_cost, BC_cost, CA_cost = map(int, sys.stdin.readline().split())
    answer = 0
    for i in range(min(a, b)+1):
        j = min(b-i, c)
        k = min(a-i, c-j)
        answer = max(answer, AB_cost * i + BC_cost * j + CA_cost * k)
        k = min(a-i, c)
        j = min(c-k, b-i)
        answer = max(answer, AB_cost * i + BC_cost * j + CA_cost * k)

    print(answer)