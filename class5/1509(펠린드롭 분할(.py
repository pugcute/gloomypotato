

words = input()
len_words = len(words)


dp = [10 ** 9 for _ in range(len_words + 1)]
dp[-1] = 0
check_p = [[0 for _ in range(len_words)] for _ in range(len_words)]


for i in range(len_words):
    check_p[i][i] = 1

for i in range(1, len_words):
    if words[i - 1] == words[i]:
        check_p[i - 1][i] = 1

for i in range(3, len_words + 1):
    for start_p in range(len_words - i + 1):
        end_p = start_p + i - 1
        if words[start_p] == words[end_p] and check_p[start_p + 1][end_p - 1]:
            check_p[start_p][end_p] = 1

for end_p in range(len_words):
    for start_p in range(end_p + 1):
        if check_p[start_p][end_p]:
            dp[end_p] = min(dp[end_p], dp[start_p - 1] + 1)
        else:
            dp[end_p] = min(dp[end_p], dp[end_p - 1] + 1)

print(dp[len_words - 1])