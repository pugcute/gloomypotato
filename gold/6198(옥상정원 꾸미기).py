import sys

N = int(input())
buildings = []
for _ in range(N):
    tmp = int(sys.stdin.readline())
    buildings.append(tmp)

stack = []

answer = 0
for building in buildings:
    while stack and stack[-1] <= building:
        stack.pop()
    stack.append(building)
    answer += len(stack) - 1


print(answer)