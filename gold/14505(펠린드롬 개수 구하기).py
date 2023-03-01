
S = input()

dp = [[0] * 31 for _ in range(31)]

len_S = len(S)
for i in range(len_S):
    dp[i][i] = 1
    if (i+1 < len_S) and S[i] == S[i+1]:
        dp[i][i+1] = 3
    elif i+1 < len_S:
        dp[i][i+1] = 2

for i in range(2, len_S):
    for j in range(len_S):
        k = j + i
        if k >= len_S:
            break
        if S[j] == S[k]:
            dp[j][k] = dp[j + 1][k] + dp[j][k-1] + 1
        else:
            dp[j][k] = dp[j + 1][k] + dp[j][k - 1] - dp[j + 1][k - 1]

print(dp[0][len_S - 1])