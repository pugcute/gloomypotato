
N = int(input())
matrix = []

answer = 100000000000000
for _ in range(N):
    a, b, c = map(int, input().split())
    matrix.append([a, b, c])

for i in range(3):
    dp = [[10000000000000] * 3 for _ in range(N)]
    dp[0][i] = matrix[0][i]
    for j in range(1, N):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + matrix[j][0]
        dp[j][1] = min(dp[j-1][2], dp[j-1][0]) + matrix[j][1]
        dp[j][2] = min(dp[j-1][1], dp[j-1][0]) + matrix[j][2]
    for k in range(3):
        if i != k:
            answer = min(answer, dp[-1][k])


print(answer)