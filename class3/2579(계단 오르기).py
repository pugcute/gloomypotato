import sys

N = int(input())
stairs = []
for _ in range(N):
    num = int(sys.stdin.readline())
    stairs.append(num)


if N == 1:
    print(stairs[0])
elif N == 2:
    print(max(stairs[0] + stairs[1], stairs[1]))
else:
    dp = [stairs[0], max(stairs[0]+stairs[1], stairs[1]), max(stairs[0] + stairs[2], stairs[1] + stairs[2])]

    for i in range(3, N):
        dp.append(max(dp[i-2]+stairs[i], stairs[i-1] + stairs[i] + dp[i-3]))

    print(dp[-1])