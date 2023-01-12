N = int(input())

ropes = []
for _ in range(N):
    tmp = int(input())
    ropes.append(tmp)

ropes.sort(reverse=True)

answer = 0
for idx in range(N):
    if answer < (idx + 1) * ropes[idx]:
        answer = (idx + 1) * ropes[idx]
print(answer)