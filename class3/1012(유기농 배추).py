import sys
sys.setrecursionlimit(10**8)

def DFS(x, y):
    if x < 0 or x>= row or y >= col or y< 0:
        return
    if 0 <=x < row and 0 <= y < col and matrix[x][y] == 1:
        matrix[x][y] = 0
        DFS(x+1, y)
        DFS(x-1, y)
        DFS(x, y+1)
        DFS(x, y-1)
    return


N = int(input())
for _ in range(N):
    col, row, num = map(int, input().split())
    matrix = [[0] * col for _ in range(row)]
    for _ in range(num):
        tmp_col, tmp_row = map(int, input().split())
        matrix[tmp_row][tmp_col] = 1
    answer = 0
    for current_row in range(row):
        for current_col in range(col):
            if matrix[current_row][current_col]:
                DFS(current_row, current_col)
                answer += 1
    print(answer)