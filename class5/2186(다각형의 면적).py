N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

area = 0
for i in range(N):
    area += (X[i] * Y[(i + 1) % N]) - (X[(i+1) % N] * Y[i])

area = abs(area)
print(round(area / 2, 2))