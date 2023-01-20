from itertools import combinations

N, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

answer = 0
for i in range(1, N+1):
    tmp_list = list(combinations(numbers, i))
    for tmp in tmp_list:
        if sum(tmp) == k:
            answer += 1
print(answer)
