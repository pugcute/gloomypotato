matrix = []
for _ in range(10):
    tmp = list(input())
    matrix.append(tmp)
answer = 0
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(10):
    if matrix[0][i] == 'O' and matrix[1][i] == 'X':
        matrix[0][i] = 'X'

for i in range(1, 10):
    for j in range(10):
        if matrix[i-1][j] == 'O':
            matrix[i][j] = 'X'
            for k in range(4):
                next_row, next_col = i +dx[k], j + dy[k]
                if 0 <= next_row<10 and 0<= next_col < 10:
                    matrix[next_row][next_col] = 'X'
            answer += 1

for i in range(10):
    for j in range(10):
        if matrix[i][j] == 'O':
            answer = -1
            break
    if answer == -1:
        break
print(answer)