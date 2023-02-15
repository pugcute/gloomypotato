N, K = map(int, input().split())

jewls = []
for _ in range(N):
    weight, val = map(int, input().split())
    jewls.append([weight, val])

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if jewls[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-jewls[i-1][0]] + jewls[i-1][1])

print(dp[N][K])