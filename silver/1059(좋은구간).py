
N = int(input())
numbers = list(map(int, input().split()))
K = int(input())

numbers.sort()

min_val = 0
max_val = 0
for num in numbers:
    if num <= K:
        min_val = num
    if num > K:
        max_val = num
        break


answer = []
for i in range(min_val+1, K+1):
    for j in range(K, max_val):
        if i != j:
            answer.append([i, j])

print(len(answer))