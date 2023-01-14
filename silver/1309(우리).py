N = int(input())

dp = [1, 3]
for i in range(2, N+1):
    dp.append((2 * dp[i-1] + dp[i-2]) % 9901)

print(dp[N])
