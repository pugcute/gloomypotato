from collections import deque

n, k = map(int, input().split())
listA = [i for i in range(1, n+1)]
queue = deque(listA)
answer = []
while queue:
    queue.rotate(-k+1)

    step = queue.popleft()
    answer.append(step)

print('<', end='')
for i in range(len(answer)):
    if i < len(answer) - 1:
        print(answer[i], end=', ')
    else:
        print(answer[i], end='')
print('>', end='')