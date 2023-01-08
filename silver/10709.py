from collections import deque


def BFS():
    while clouds:
        current_row, current_col = clouds.popleft()
        next_col = current_col + 1
        if next_col < M and matrix[current_row][next_col] != 0:
            matrix[current_row][next_col] = matrix[current_row][current_col] + 1
            clouds.append([current_row, next_col])

    return

N, M = map(int, input().split())
matrix = []
clouds = deque()
for row in range(N):
    str_row = input()
    row_list = []
    for idx, val in enumerate(str_row):
        if val == 'c':
            row_list.append(0)
            clouds.append([row, idx])
        else:
            row_list.append(-1)
    matrix.append(row_list)
BFS()
for ans in matrix:
    print(' '.join(list(map(str, ans))))