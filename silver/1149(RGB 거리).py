N = int(input())
matrix = [[0] * 3 for _ in range(N)]

tmp = []
for _ in range(N):
    a, b, c = map(int, input().split())
    tmp.append((a, b, c))

for i in range(3):
    matrix[0][i] = (tmp[0][i], i)



for i in range(1, N):
    val = 1001
    idx = 0
    for j in range(3):
        val = 1001
        idx = 0
        for k in range(3):
            if matrix[i-1][j][1] != k and tmp[i][k] <= val:
                val = tmp[i][k]
                print(val)
                idx = k
            else:
                continue
        matrix[i][j] = (val+matrix[i-1][j][0], idx)

print(matrix)
