import sys

n, k = map(int, input().split())
coins = []
dp = [0] + [10001 for _ in range(10000)]
for _ in range(n):
    coin = int(sys.stdin.readline())
    coins.append(coin)

for coin in coins:
    for j in range(coin, 10001):
        if dp[j - coin] != 10001:
            dp[j] = min(dp[j], dp[j-coin] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
