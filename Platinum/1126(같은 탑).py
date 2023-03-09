
N = int(input())
towers = list(map(int, input().split()))
dp = [[-1] * 500001 for _ in range(2)]
dp[0][0] = dp[1][0] = 0
towers.sort()

max_len = 0
for i in range(N):
    for j in range(i):
        if dp[0][j] == -1:
            continue
        dp[1][j+towers[i]] = max(dp[1][j + towers[i]], dp[0][j] + towers[i])
        if j < towers[i]:
            dp[1][towers[i] - j] = max(dp[1][towers[i] - j], dp[0][j] + towers[i])
        else:
            dp[1][j - towers[i]] = max(dp[1][j - towers[i]], dp[0][j]);


print(dp[0][:100], dp[1][:100])