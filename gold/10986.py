N, M = map(int, input().split())
numbers = list(map(int, input().split()))

remainders = [0 for _ in range(M)]
remainders[0] = 1

total = 0
for i in range(N):
    total += numbers[i]
    tmp = total % M
    remainders[tmp] += 1

answer = 0
for val in remainders:
    answer += val * (val - 1) // 2

print(answer)