
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
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and check(i, j):
            matrix[i][j] = 2
            answer += 1

print(answer)


