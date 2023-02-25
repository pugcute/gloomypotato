N, M, R = map(int, input().split())

nodes = list(map(int, input().split()))

graph = [[10**9] * (1+N) for _ in range(1+N)]

for _ in range(R):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])
    graph[b][a] = min(c, graph[a][b])


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for i in range(1, N+1):
    tmp = 0
    for j in range(1, N+1):
        if graph[i][j] <= M:
            tmp += nodes[j-1]
    answer = max(answer, tmp)

print(answer)