

dp = [[0 for _ in range(31)] for _ in range(31) ]

for h in range(1,31):
    dp[0][h] = 1

for w in range(1,31):
    for h in range(30):
        if h == 0:
            dp[w][h] = dp[w-1][h+1]
        else:
            dp[w][h] = dp[w-1][h+1] + dp[w][h-1]

while True:
    tmp = int(input())
    if tmp == 0:
        break
    else:
        print(dp[tmp][0])