import copy

def check(row, col):
    checker = 1
    for i in range(N+1):
        next_row, next_col = row + i, col + i
        if 0<=next_row< N and 0<=next_col<N and matrix[next_row][next_col] in [0, 1]:
            continue
        elif 0<=next_row< N and 0<=next_col<N and matrix[next_row][next_col] == 2:
            checker = 0
            break

    for i in range(N + 1):
        next_row, next_col = row + i, col - i
        if 0 <= next_row < N and 0 <= next_col < N and matrix[next_row][next_col] in [0, 1]:
            continue
        elif 0 <= next_row < N and 0 <= next_col < N and matrix[next_row][next_col] == 2:
            checker = 0
            break

    for i in range(N + 1):
        next_row, next_col = row - i, col + i
        if 0 <= next_row < N and 0 <= next_col < N and matrix[next_row][next_col] in [0, 1]:
            continue
        elif 0 <= next_row < N and 0 <= next_col < N and matrix[next_row][next_col] == 2:
            checker = 0
            break


    for i in range(N + 1):
        next_row, next_col = row - i, col - i
        if 0 <= next_row < N and 0 <= next_col < N and matrix[next_row][next_col] in [0, 1]:
            continue
        elif 0 <= next_row < N and 0 <= next_col < N and matrix[next_row][next_col] == 2:
            checker = 0
            break
    return checker


def check1(row, col):
    checker = 1
    for i in range(N+1):
        next_row, next_col = row + i, col + i
        if 0<=next_row< N and 0<=next_col<N and matrix1[next_row][next_col] in [0, 1]:
            continue
        elif 0<=next_row< N and 0<=next_col<N and matrix1[next_row][next_col] == 2:
            checker = 0
            break

    for i in range(N + 1):
        next_row, next_col = row + i, col - i
        if 0 <= next_row < N and 0 <= next_col < N and matrix1[next_row][next_col] in [0, 1]:
            continue
        elif 0 <= next_row < N and 0 <= next_col < N and matrix1[next_row][next_col] == 2:
            checker = 0
            break

    for i in range(N + 1):
        next_row, next_col = row - i, col + i
        if 0 <= next_row < N and 0 <= next_col < N and matrix1[next_row][next_col] in [0, 1]:
            continue
        elif 0 <= next_row < N and 0 <= next_col < N and matrix1[next_row][next_col] == 2:
            checker = 0
            break


    for i in range(N + 1):
        next_row, next_col = row - i, col - i
        if 0 <= next_row < N and 0 <= next_col < N and matrix1[next_row][next_col] in [0, 1]:
            continue
        elif 0 <= next_row < N and 0 <= next_col < N and matrix1[next_row][next_col] == 2:
            checker = 0
            break
    return checker

def check2(row, col):
    checker = 1
    for i in range(N+1):
        next_row, next_col = row + i, col + i
        if 0<=next_row< N and 0<=next_col<N and matrix2[next_row][next_col] in [0, 1]:
            continue
        elif 0<=next_row< N and 0<=next_col<N and matrix2[next_row][next_col] == 2:
            checker = 0
            break

    for i in range(N + 1):
        next_row, next_col = row + i, col - i
        if 0 <= next_row < N and 0 <= next_col < N and matrix2[next_row][next_col] in [0, 1]:
            continue
        elif 0 <= next_row < N and 0 <= next_col < N and matrix2[next_row][next_col] == 2:
            checker = 0
            break

    for i in range(N + 1):
        next_row, next_col = row - i, col + i
        if 0 <= next_row < N and 0 <= next_col < N and matrix2[next_row][next_col] in [0, 1]:
            continue
        elif 0 <= next_row < N and 0 <= next_col < N and matrix2[next_row][next_col] == 2:
            checker = 0
            break


    for i in range(N + 1):
        next_row, next_col = row - i, col - i
        if 0 <= next_row < N and 0 <= next_col < N and matrix2[next_row][next_col] in [0, 1]:
            continue
        elif 0 <= next_row < N and 0 <= next_col < N and matrix2[next_row][next_col] == 2:
            checker = 0
            break
    return checker

def check3(row, col):
    checker = 1
    for i in range(N+1):
        next_row, next_col = row + i, col + i
        if 0<=next_row< N and 0<=next_col<N and matrix3[next_row][next_col] in [0, 1]:
            continue
        elif 0<=next_row< N and 0<=next_col<N and matrix3[next_row][next_col] == 2:
            checker = 0
            break

    for i in range(N + 1):
        next_row, next_col = row + i, col - i
        if 0 <= next_row < N and 0 <= next_col < N and matrix3[next_row][next_col] in [0, 1]:
            continue
        elif 0 <= next_row < N and 0 <= next_col < N and matrix3[next_row][next_col] == 2:
            checker = 0
            break

    for i in range(N + 1):
        next_row, next_col = row - i, col + i
        if 0 <= next_row < N and 0 <= next_col < N and matrix3[next_row][next_col] in [0, 1]:
            continue
        elif 0 <= next_row < N and 0 <= next_col < N and matrix3[next_row][next_col] == 2:
            checker = 0
            break


    for i in range(N + 1):
        next_row, next_col = row - i, col - i
        if 0 <= next_row < N and 0 <= next_col < N and matrix3[next_row][next_col] in [0, 1]:
            continue
        elif 0 <= next_row < N and 0 <= next_col < N and matrix3[next_row][next_col] == 2:
            checker = 0
            break
    return checker
# def get_bishop(row, col):
#     for i in range(N+1):
#         next_row, next_col = row + i, col + i
#         if 0<=next_row< N and 0<=next_col<N and matrix[next_row][next_col] == 1:
#             matrix[next_row][next_col] = 2
#
#
#     for i in range(N + 1):
#         next_row, next_col = row + i, col - i
#         # print(next_row, next_col)
#         if 0 <= next_row < N and 0 <= next_col < N and matrix[next_row][next_col] == 1:
#             matrix[next_row][next_col] = 2
#
#
#     return

N = int(input())
matrix = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)

answer = 0
matrix1 = copy.deepcopy(matrix)
matrix2 = copy.deepcopy(matrix)
matrix3 = copy.deepcopy(matrix)
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and check(i, j):
            matrix[i][j] = 2
            answer += 1

answer1 = 0
for i in range(N-1, -1, -1):
    for j in range(N):
        if matrix1[i][j] == 1 and check1(i, j):
            matrix1[i][j] = 2
            answer1 += 1

answer2 = 0
for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        if matrix2[i][j] == 1 and check2(i, j):
            matrix2[i][j] = 2
            answer2 += 1
answer3 = 0
for i in range(N):
    for j in range(N-1, -1, -1):
        if matrix3[i][j] == 1 and check3(i, j):
            matrix3[i][j] = 2
            answer3 += 1

print(max(answer, answer1, answer2, answer3))


