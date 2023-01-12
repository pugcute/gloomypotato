from collections import deque
def BFS(cnt):
    if cnt > K:
        return False
    if visited[cnt] == True:
        return True
    else:
        current = to_visits.popleft()




N = int(input())
numbers = list(map(int, input().split()))
K = int(input())
visited = [False] * (1000 * 1000 + 1)
numbers.sort()
to_visits = deque(numbers)
cnt = 1
while True:
    if cnt % 2:

    else:
