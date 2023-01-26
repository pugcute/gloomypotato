

def answer(n):
    if n in dp.keys():
        return dp[n]
    dp[n] = answer(n//P) + answer(n//Q)
    return dp[n]


N, P, Q = map(int, input().split())

dp = {}

dp[0] = 1

print(answer(N))