import sys
from collections import deque


def BFS():
    cnt = 0
    while to_visits:
        current_row, current_col = to_visits.popleft()
        for idx in range(4):
            next_row, next_col = current_row + dx[idx], current_col + dy[idx]
            if 0<=next_row < N and 0<=next_col < M and matrix[next_row][next_col] not in ['X', 'I']:
                if matrix[next_row][next_col] == 'P':
                    cnt += 1
                to_visits.append([next_row, next_col])
                matrix[next_row][next_col] = 'I'
    return cnt



N, M = map(int, input().split())
matrix = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(N):
    tmp = list(input())
    matrix.append(tmp)

to_visits = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'I':
            to_visits.append([i, j])

answer = BFS()
if answer == 0:
    print('TT')
else:
    print(answer)