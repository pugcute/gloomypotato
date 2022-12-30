import sys

n, money = list(map(int, input().split()))
coins = []
answer = 0
for i in range(n):
    coin = int(sys.stdin.readline())
    coins.append(coin)

coins.sort(reverse=True)

for coin in coins:
    if money // coin > 0:
        answer += money // coin
        money = money % coin
print(answer)