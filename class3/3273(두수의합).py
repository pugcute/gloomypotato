
N = int(input())
numbers = list(map(int, input().split()))
K = int(input())

numbers.sort()
answer = 0
tmp_idx = 0
for i in range(len(numbers)):
    current = numbers[N-1-i]
    if tmp_idx > N-1-i:
        break
    if current >= K:
        continue
    if current < K:
        for j in range(tmp_idx, N-1-i):
            if current + numbers[j] == K:
                answer += 1
                tmp_idx = j
                break
            elif current + numbers[j] > K:
                break

print(answer)