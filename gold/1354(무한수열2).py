

def answer(n):
    # N, P, Q, X, Y
    if n in dp.keys():
        return dp[n]

    if n//P - X >= 0:
        next1 = n // P - X
    else:
        next1 = 0
    if n // Q - Y >= 0:
        next2 = n // Q - Y
    else:
        next2 = 0
    dp[n] = answer(next1) + answer(next2)
    return dp[n]

N, P, Q, X, Y = map(int, input().split())

dp= {}
dp[0] = 1
print(answer(N))