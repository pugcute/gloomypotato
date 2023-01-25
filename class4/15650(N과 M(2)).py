from itertools import combinations

N, M = map(int, input().split())

numbers = [i for i in range(1, N+1)]
lists = list(combinations(numbers, M))

for ans in lists:
    print(*ans)