
N = int(input())
homeworks = []
for _ in range(N):
    deadline, score = map(int, input().split())
    homeworks.append([deadline, score])

answer = 0
homeworks.sort()

stack = []
for day in range(N, 0, -1):
    while homeworks and homeworks[-1][0] >= day:
        stack.append(homeworks.pop()[1])
    if stack:
        stack.sort()
        answer += stack.pop()

print(answer)