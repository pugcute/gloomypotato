
A = input()
B = input()

dp = [[0] * (len(A) + 1) for _ in range(len(B)+1)]

answer = ''
for i in range(1, len(B)+1):
    for j in range(1, len(A)+1):
        if B[i-1] == A[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

A_len = len(A)
B_len = len(B)

while True:
    if A_len == 0 or B_len == 0:
        break
    if dp[B_len][A_len] == dp[B_len-1][A_len]:
        B_len -= 1
    elif dp[B_len][A_len] == dp[B_len][A_len-1]:
        A_len -= 1
    else:
        answer += B[B_len - 1]
        A_len -= 1
        B_len -= 1
print(answer[::-1])
