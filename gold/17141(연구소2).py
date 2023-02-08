import sys
import copy
from collections import deque
from itertools import combinations


def BFS(graph, virus):
    global answer
    cnt = 0
    for mat in graph:
        cnt = mat.count(0)
        if cnt != 0:
            break
    if cnt == 0:
        answer = 0
    else:
        to_visits = deque(virus)
        while to_visits:
            current_row, current_col = to_visits.popleft()
            for i in range(4):
                next_row, next_col = current_row + dx[i], current_col + dy[i]
                if 0<=next_row<N and 0<=next_col<N and graph[next_row][next_col] == 0:
                    graph[next_row][next_col] = graph[current_row][current_col] + 1
                    to_visits.append([next_row, next_col])

        tmp = 0
        for row in range(N):
            flag = 0
            for col in range(N):
               if graph[row][col] == 0:
                    flag = 1
                    tmp = 0
                    break
               elif graph[row][col] > tmp:
                   tmp = graph[row][col]
            if flag == 1:
                break
        tmp = tmp - 1
        if tmp < answer and tmp > 0:
            answer = tmp

N, K = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
matrix = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)

position_virus = []
answer = 1000000
for row in range(N):
    for col in range(N):
        if matrix[row][col] == 2:
            matrix[row][col] = 0
            position_virus.append([row, col])
        elif matrix[row][col] == 1:
            matrix[row][col] = -1

viruses = list(combinations(position_virus, K))

for virus in viruses:
    tmp_matrix = copy.deepcopy(matrix)
    for vi in virus:
        tmp_matrix[vi[0]][vi[1]] = 1
    BFS(tmp_matrix, virus)

if answer == 1000000:
    answer = -1
print(answer)



