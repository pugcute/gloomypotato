import sys

N, K = map(int, sys.stdin.readline().split())

jewls = []

for _ in range(N):
    wei, val, cnt = map(int, sys.stdin.readline().split())
    idx = 1
    while cnt > 0:
        tmp = min(idx, cnt)
        jewls.append((wei * tmp, val * tmp))
        idx *= 2
        cnt -= tmp

total_N = len(jewls)
dp = [[0] * (K+1) for _ in range(total_N+1)]

for i in range(1, total_N + 1):
    for j in range(1, K+1):
        if jewls[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-jewls[i-1][0]] + jewls[i-1][1])

print(dp[total_N][K])