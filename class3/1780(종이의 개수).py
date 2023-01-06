
import sys
import math
sys.setrecursionlimit(10**8)


def checkCnt(matrix1, count):
    global cnt_0, cnt_1, cnt_2
    for row in range(0, count, count // 3):
        for col in range(0, count, count // 3):
            tmp = [matrix1[i][col:col + count // 3] for i in range(row, row+count // 3)]
            base = tmp[0][0]
            flag = 0
            for row1 in range(count // 3):
                flag = 0
                for col1 in range(count // 3):
                    if base != tmp[row1][col1]:
                        flag = 1
                        break
                    if row1 == count//3 - 1 and col1 == count//3 - 1:
                        if base == 0:
                            cnt_0 += 1
                        elif base == 1:
                            cnt_1 += 1
                        elif base == -1:
                            cnt_2 += 1

                if flag == 1:
                    break
            if flag == 1:
                checkCnt(tmp, count // 3)
    return


N = int(input())
matrix = []
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    matrix.append(tmp)

cnt = N
cnt_0 = 0
cnt_1 = 0
cnt_2 = 0 # -1
base_N = matrix[0][0]
flag_N = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] != base_N:
            flag_N = 1
            break
        if i == N-1 and j == N-1:
            if base_N == 0:
                cnt_0 += 1
            elif base_N == 1:
                cnt_1 += 1
            elif base_N == -1:
                cnt_2 += 1
    if flag_N:
        break

if flag_N:
    checkCnt(matrix, cnt)

print(cnt_2)
print(cnt_0)
print(cnt_1)