import sys
from collections import deque
sys.setrecursionlimit(10**8)

def BFS(start_row, start_col):
    to_visits = deque()
    start = [start_row, start_col]

    to_visits.append(start)
    while to_visits:
        current_row, current_col = to_visits.popleft()
        for i in range(4):
            next_row, next_col = current_row + dx[i], current_col+dy[i]
            if next_row < 0 or next_row >= row or next_col < 0 or next_col >= col:
                continue
            if 0 <= next_row < row and 0 <= next_col < col and matrix[next_row][next_col] == 1:
                matrix[next_row][next_col] += matrix[current_row][current_col]
                to_visits.append([next_row, next_col])

row, col = map(int, input().split())
matrix = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(row):
    tmp = list(map(int, input()))
    matrix.append(tmp)

BFS(0, 0)
print(matrix[row-1][col-1])

