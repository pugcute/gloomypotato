import sys

N = int(input())
numbers = list(map(int, input().split()))

dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(1, N):
    if numbers[i-1] == numbers[i]:
        dp[i-1][i] = 1


for cnt in range(N-2):
    for start_a in range(N - 2 - cnt):
        end_a = start_a + 2 + cnt
        if numbers[start_a] == numbers[end_a] and dp[start_a + 1][end_a - 1]:
            dp[start_a][end_a] = 1

M = int(input())
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(dp[start-1][end-1])