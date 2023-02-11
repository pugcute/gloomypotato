import heapq

N, money = map(int, input().split())
flavors = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    flavors.append([a, b, a-b])

flavors.sort(key=lambda x:x[2], reverse=True)

answer = 0
for flavor in flavors:
    if 5000 > money >= 1000 or flavor[0] <= flavor[1]:
        answer += flavor[1]
        money -= 1000
    elif money >= 5000:
        answer += flavor[0]
        money -= 5000
print(answer)
