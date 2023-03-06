from bisect import bisect_left, bisect_right
from itertools import combinations

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

left = numbers[:N//2]
right = numbers[N//2:]

left_sum = []
right_sum = []

for i in range(1, N//2+1):
    tmp = list(combinations(left, i))
    for s in tmp:
        left_sum.append(sum(s))

for i in range(1, N - N//2 + 1):
    tmp = list(combinations(right, i))
    for s in tmp:
        right_sum.append(sum(s))

answer = 0
left_sum.sort()
right_sum.sort()
answer += bisect_right(left_sum, K)-bisect_left(left_sum, K)
answer += bisect_right(right_sum, K) - bisect_left(right_sum, K)

for S in left_sum:
    answer += bisect_right(right_sum, K-S) - bisect_left(right_sum, K-S)

print(answer)