N = int(input())
numbers = list(map(int, input().split()))
numbers_reverse = numbers[::-1]
dp = [0] * N
dp1 = [0] * N

for i in range(N):
    dp[i] = 1
    dp1[i] = 1
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[j]+1, dp[i])
    for j in range(i):
        if numbers_reverse[j] < numbers_reverse[i]:
            dp1[i] = max(dp1[j] + 1, dp1[i])

answer = [0] * N

for i in range(N):
    answer[i] = dp[i] + dp1[N-1-i] - 1

print(max(answer))