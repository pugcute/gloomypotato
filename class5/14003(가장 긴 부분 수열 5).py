from bisect import bisect_left


N = int(input())
numbers = list(map(int, input().split()))

dp = []
idx = []

for num in numbers:
    current = bisect_left(dp, num)
    if len(dp) != current:
        dp[current] = num
    else:
        dp.append(num)
    idx.append(current + 1)


m = len(dp)
answer = []
print(m)
for i in range(len(idx) - 1, -1, -1):
    if idx[i] == m:
        answer.append(numbers[i])
        m -= 1
    else:
        continue

print(*sorted(answer, reverse=False))