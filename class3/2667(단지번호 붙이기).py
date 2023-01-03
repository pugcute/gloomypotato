import sys
sys.setrecursionlimit(10**8)

def DFS(row, col):
    global tmp_answer
    to_visits = [[row, col]]
    matrix[row][col] = 0
    while to_visits:
        current_row, current_col = to_visits.pop()
        for i in range(4):
            next_row, next_col = current_row + dx[i], current_col + dy[i]
            if 0<=next_row < n and 0<= next_col < n and matrix[next_row][next_col] == 1:
                to_visits.append([next_row, next_col])
                tmp_answer += 1
                matrix[next_row][next_col] = 0


n = int(input())
matrix = []
for _ in range(n):
    tmp = list(map(int, input()))
    matrix.append(tmp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
answer_list = []
for row in range(n):
    for col in range(n):
        tmp_answer = 1
        if matrix[row][col] == 1:
            DFS(row, col)
            answer_list.append(tmp_answer)
            answer += 1
answer_list.sort()
print(answer)
for ans in answer_list:
    print(ans)