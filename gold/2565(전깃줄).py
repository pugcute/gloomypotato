N = int(input())
matrix = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)

matrix.sort(key=lambda x:x[0])
dp = [0] * N
for i in range(N):
    dp[i] = 1
    for j in range(i):
        if matrix[i][1] > matrix[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N-max(dp))