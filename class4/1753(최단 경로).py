import heapq

def dijkstra(a):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

V, E = map(int, input().split())

start = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

distance = [10 ** 9] * (V+1)

dijkstra(start)

for dist in distance[1:]:
    if dist == 10 ** 9:
        print('INF')
    else:
        print(dist)
