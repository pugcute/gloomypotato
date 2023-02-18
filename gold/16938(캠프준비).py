from itertools import combinations
N, L, R, X = map(int, input().split())
scores = list(map(int, input().split()))

answer = 0
for i in range(2, N+1):
    lists = list(combinations(scores, i))
    for tmp in lists:
        if L <= sum(tmp) <= R:
            if max(tmp) - min(tmp) >= X:
                answer += 1
print(answer)