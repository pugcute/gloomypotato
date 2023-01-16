
N = int(input())
numbers = list(map(int, input().split()))
dp = [0] * N
array = [[] for _ in range(N)]

for i in range(N):
    dp[i] = 1
    array[i].append(numbers[i])
    tmp = []
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            if len(tmp) < len(array[j]):
                tmp = array[j]
    array[i].extend(tmp)

print(max(dp))
idx = dp.index(max(dp))

print(*sorted(array[idx]))
