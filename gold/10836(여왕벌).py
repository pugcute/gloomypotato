import sys
# 하드코딩도 pypy3로 돌아감, 시간낭비함
N, K = map(int, input().split())
days = [1] * (2 * N - 1)
for _ in range(K):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    for idx in range(a, a+b):
        days[idx] += 1
    for idx in range(a+b, a+b+c):
        days[idx] += 2


for i in range(N-1, -1, -1):
    ans = []
    ans.append(days[i])
    for j in range(N, len(days)):
        ans.append(days[j])
    print(*ans)


