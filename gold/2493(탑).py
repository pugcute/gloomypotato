
N = int(input())
towers = list(map(int, input().split()))

stack = []
answer = [0] * N

for i in range(N):
    tower = towers[i]
    tmp = 0
    while stack and stack[-1][1] <= tower:
        stack.pop()
    if stack:
        answer[i] = stack[-1][0]

    stack.append((i+1, tower))

print(*answer)
