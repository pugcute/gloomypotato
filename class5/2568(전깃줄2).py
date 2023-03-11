from bisect import bisect_left

N = int(input())
matrix = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)
matrix.sort()
dp, idx, answer = [], [], []

for mat in matrix:
    current = bisect_left(idx, mat[1])

    if len(idx) != current:
        idx[current] = mat[1]
    else:
        idx.append(mat[1])

    dp.append(current + 1)


m = len(idx)
print(len(matrix) - m)
for i in range(len(dp) - 1, -1, -1):
    if dp[i] == m:
        m -= 1
    else:
        answer.append(matrix[i][0])

for ans in answer[::-1]:
    print(ans)