T = int(input())
for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    sums = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        sums[i] = sums[i - 1] + numbers[i-1]
    dp = [[0 for i in range(N + 1)] for _ in range(N + 1)]
    for i in range(2, N + 1):
        for j in range(1, N + 2 - i):
            dp[j][j + i - 1] = min([dp[j][j + k] + dp[j + k + 1][j + i - 1] for k in range(i - 1)]) + (
                    sums[j + i - 1] - sums[j - 1])

    print(dp[1][N])
