import sys
sys.setrecursionlimit(10**9)

def DFS(current_row, current_col, cnt):
    global answer
    if cnt > K:
        return
    if current_row == 0 and current_col == col - 1 and cnt == K:
        answer += 1
        return
    matrix[current_row][current_col] = 1
    for i in range(4):
        next_row, next_col = current_row + dx[i], current_col + dy[i]
        if 0<=next_row<row and 0<=next_col < col and matrix[next_row][next_col] == '.':
            DFS(next_row, next_col, cnt+1)
            matrix[next_row][next_col] = '.'


matrix = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
row, col, K = map(int, input().split())
for _ in range(row):
    tmp = list(input())
    matrix.append(tmp)

DFS(row-1, 0, 1)
print(answer)

