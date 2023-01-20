
N, S, M = map(int, input().split())

numbers = list(map(int, input().split()))
dp = [[0] * (M+1) for _ in range(N+1)]

dp[0][S] = 1

for step in range(N):
    for current in range(M+1):
        if dp[step][current] == 1:
            if 0<=current + numbers[step] <= M:
                dp[step+1][current + numbers[step]] = 1
            if 0 <= current - numbers[step] <= M:
                dp[step + 1][current - numbers[step]] = 1
answer = -1
for idx in range(M+1):
    if dp[-1][idx] == 1:
        answer = idx

print(answer)
