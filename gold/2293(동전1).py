import sys

n, k = map(int, input().split())
coins = []
dp = [1] + [0 for _ in range(k)]
for _ in range(n):
    coin = int(sys.stdin.readline())
    coins.append(coin)


for coin in coins:
    for i in range(1, k+1):
        if i - coin >= 0:
            dp[i] += dp[i-coin]


print(dp[k])
