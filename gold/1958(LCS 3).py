
A = input()
B = input()
C = input()

dp = [[[0] * (len(A)+1) for _ in range(len(B) + 1)] for _ in range(len(C)+1)]

for i in range(1, len(C)+1):
    for j in range(1, len(B)+1):
        for k in range(1, len(A)+1):
            if C[i-1] == B[j-1] and C[i-1] == A[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[-1][-1][-1])

# for i in range(1, len(B)+1):
#     for j in range(1, len(A)+1):
#         if B[i-1] == A[j-1]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#
# AB = ''
# A_len = len(A)
# B_len = len(B)
# while True:
#     if A_len == 0 or B_len == 0:
#         break
#     if dp[B_len][A_len] == dp[B_len-1][A_len]:
#         B_len -= 1
#     elif dp[B_len][A_len] == dp[B_len][A_len-1]:
#         A_len -= 1
#     else:
#         AB += B[B_len-1]
#         B_len -= 1
#         A_len -= 1
#
# AB = AB[::-1]
# dp1 = [[0] * (len(AB) + 1) for _ in range(len(C) + 1)]
#
# for i in range(1, len(C)+1):
#     for j in range(1, len(AB)+1):
#         if C[i-1] == AB[j-1]:
#             dp1[i][j] = dp1[i-1][j-1] + 1
#         else:
#             dp1[i][j] = max(dp1[i - 1][j], dp1[i][j - 1])
#
# print(dp1[-1][-1])
