import sys

N, M = map(int, input().split())
dateset = {}
answer = []

for _ in range(N):
    problem = sys.stdin.readline().rstrip()
    dateset[problem] = 1

for _ in range(M):
    problem = sys.stdin.readline().rstrip()
    if problem in dateset.keys():
        answer.append(problem)

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)