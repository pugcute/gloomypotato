import sys
from collections import deque
sys.setrecursionlimit(10**8)

def BFS():
    while tomatos:
        current_row, current_col = tomatos.popleft()
        for i in range(4):
            next_row, next_col = current_row + dx[i], current_col + dy[i]
            if 0 <= next_row < row and 0 <= next_col < col and matrix[next_row][next_col] == 0:
                matrix[next_row][next_col] = matrix[current_row][current_col] + 1
                tomatos.append([next_row, next_col])


col, row = map(int, input().split())
matrix = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(row):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)

tomatos = deque()
for i in range(row):
    for j in range(col):
        if matrix[i][j] == 1:
            tomatos.append([i, j])

BFS()
answer = 1
for i in range(row):
    for j in range(col):
        if answer < matrix[i][j]:
            answer = matrix[i][j]
        if matrix[i][j] == 0:
            answer = 0
            break
    if answer == 0:
        break
print(answer-1)
