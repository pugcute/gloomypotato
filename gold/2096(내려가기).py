N = int(input())
matrix = []
# max_matrix = [[0] * N for _ in range(N)]
dp = [0] * 3

for _ in range(N):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)

for i in range(3):
    dp[i] = matrix[0][i]

answer = 0
answer1 = 0
for i in range(1, N):
    tmp = max(dp[0], dp[1]) + matrix[i][0]
    tmp1 = max(dp[0], dp[1], dp[2]) + matrix[i][1]
    tmp2 = max(dp[1], dp[2]) + matrix[i][2]
    dp[0] = tmp
    dp[1] = tmp1
    dp[2] = tmp2
answer = max(dp)

for i in range(3):
    dp[i] = matrix[0][i]

for i in range(1, N):
    tmp = min(dp[0], dp[1]) + matrix[i][0]
    tmp1 = min(dp[0], dp[1], dp[2]) + matrix[i][1]
    tmp2 = min(dp[1], dp[2]) + matrix[i][2]
    dp[0] = tmp
    dp[1] = tmp1
    dp[2] = tmp2
answer1 = min(dp)
print(answer, answer1)
# for i in range(3):
#     max_matrix[0][i] = matrix[0][i]
#
# answer = 0
# answer1 = 0
# for i in range(1, N):
#     max_matrix[i][0] = max(max_matrix[i-1][0], max_matrix[i-1][1]) + matrix[i][0]
#     max_matrix[i][1] = max(max_matrix[i-1][0], max_matrix[i-1][1], max_matrix[i-1][2]) + matrix[i][1]
#     max_matrix[i][2] = max(max_matrix[i - 1][1], max_matrix[i - 1][2]) + matrix[i][2]
# answer = max(max_matrix[-1])
#
# for i in range(1, N):
#     max_matrix[i][0] = min(max_matrix[i - 1][0], max_matrix[i - 1][1]) + matrix[i][0]
#     max_matrix[i][1] = min(max_matrix[i - 1][0], max_matrix[i - 1][1], max_matrix[i - 1][2]) + matrix[i][1]
#     max_matrix[i][2] = min(max_matrix[i - 1][1], max_matrix[i - 1][2]) + matrix[i][2]
#
# answer1 = min(max_matrix[-1])
# print(answer, answer1)