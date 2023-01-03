from collections import deque
import sys

def BFS(row, col):
    area = 1
    to_visits = deque()
    to_visits.append([row, col])
    metrix[row][col] = 0
    while to_visits:
        current_row, current_col = to_visits.popleft()
        for idx in range(4):
            next_row = current_row + dx[idx]
            next_col = current_col + dy[idx]
            if 0 <= next_row < n and 0 <= next_col < m and metrix[next_row][next_col]:
                to_visits.append([next_row, next_col])
                metrix[next_row][next_col] = 0
                area += 1
    return area



metrix = []
n, m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(n):
    tmp = list(map(int, input().split()))
    metrix.append(tmp)

cnt = 0
answer = 0
for row in range(n):
    for col in range(m):

        if metrix[row][col]:
            cnt += 1
            picture = BFS(row, col)
            if picture > answer:
                answer = picture

print(cnt)

print(answer)