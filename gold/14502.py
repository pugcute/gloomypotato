import sys
import copy
from collections import deque
from itertools import combinations

def BFS(graph, tmp_walls, to_visits):
    for tmp_wall in tmp_walls:
        tr, tc = tmp_wall
        graph[tr][tc] = 1

    while to_visits:
        current_row, current_col = to_visits.popleft()
        for i in range(4):
            next_row, next_col = current_row + dx[i], current_col + dy[i]
            if 0 > next_row or 0 > next_col or next_row >= row or next_col >= col:
                continue
            if 0<=next_row<row and 0<=next_col<col and graph[next_row][next_col] == 0:
                graph[next_row][next_col] = 2
                to_visits.append([next_row, next_col])
    cnt = 0
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 0:
                cnt += 1

    return cnt





row, col = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
matrix = []
non_block = []
for _ in range(row):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)

viruses = deque()

for i in range(row):
    for j in range(col):
        if matrix[i][j] == 0:
            non_block.append((i, j))
        elif matrix[i][j] == 2:
            viruses.append([i, j])

walls = list(combinations(non_block, 3))

answer = 0
for wall in walls:
    tmp_matrix = copy.deepcopy(matrix)
    tmp_virus = copy.deepcopy(viruses)
    tmp = BFS(tmp_matrix, wall, tmp_virus)
    if tmp > answer:
        answer = tmp

print(answer)