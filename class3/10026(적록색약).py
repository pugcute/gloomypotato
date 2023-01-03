import sys
sys.setrecursionlimit(10**8)
import copy

def DFS(x, y, color, flag):
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    if 0 <= x < N and 0 <= y < N and not flag and matrix[x][y] == color:
        matrix[x][y] = 1
        DFS(x+1, y, color, flag)
        DFS(x-1, y, color, flag)
        DFS(x, y+1, color, flag)
        DFS(x, y-1, color, flag)
    if 0 <= x < N and 0 <= y < N and flag and blind_matrix[x][y] == color:
        blind_matrix[x][y] = 1
        DFS(x + 1, y, color, flag)
        DFS(x - 1, y, color, flag)
        DFS(x, y + 1, color, flag)
        DFS(x, y - 1, color, flag)
    return



N = int(input())
matrix = []
for _ in range(N):
    tmp = list(input())
    matrix.append(tmp)

blind_matrix = copy.deepcopy(matrix)
for row in range(N):
    for col in range(N):
        if blind_matrix[row][col] == 'G':
            blind_matrix[row][col] = 'R'

answer = 0
for row in range(N):
    for col in range(N):
        if matrix[row][col] in ['G', 'R', 'B']:
            DFS(row, col, matrix[row][col], 0)
            answer += 1

blind_answer = 0
for row in range(N):
    for col in range(N):
        if blind_matrix[row][col] in ['G', 'R', 'B']:
            DFS(row, col, blind_matrix[row][col], 1)
            blind_answer += 1


print(answer, blind_answer)
