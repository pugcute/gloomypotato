N = int(input())
numbers = []
for _ in range(N):
    tmp = int(input())
    numbers.append(tmp)

dp = [0] * N

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N-max(dp))