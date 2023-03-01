def get_sum(a):
    b_sum = 0
    for i in range(N - 1):
        for j in range(M - 1):
            b_sum += a[i][j] + a[i + 1][j] + a[i + 1][j + 1] + a[i][j + 1]
    return b_sum

def get_b(x, y, check_row):
    b = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            b[i][j] = matrix[i][j]
    if check_row:
        for c in range(M):
            b[x][c], b[y][c] = matrix[y][c], matrix[x][c]
    else:
        for r in range(N):
            b[r][x], b[r][y] = matrix[r][y], matrix[r][x]
    return b

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)
rows_sum = [0] * N
cols_sum = [0] * M
r_min = float('inf')
c_min = float('inf')

min_col, min_row = -1, -1
answer = get_sum(matrix)

for i in range(N):
    for j in range(M):
        rows_sum[i] += matrix[i][j]
        cols_sum[j] += matrix[i][j]


for r in range(1, N - 1):
    tr = rows_sum[r] * 4
    tr -= 2 * (matrix[r][0] + matrix[r][M - 1])
    if r_min > tr:
        r_min = tr
        min_row = r

for c in range(1, M - 1):
    tc = cols_sum[c] * 4
    tc -= 2 * (matrix[0][c] + matrix[N - 1][c])
    if c_min > tc:
        c_min = tc
        min_col = c

if min_row > 0:
    b = get_b(0, min_row, 1)
    answer = max(answer, get_sum(b))
    b = get_b(N - 1, min_row, 1)
    answer = max(answer, get_sum(b))


if min_col > 0:
    b = get_b(0, min_col, 0)
    answer = max(answer, get_sum(b))
    b = get_b(M - 1, min_col, 0)
    answer = max(answer, get_sum(b))

print(answer)