import heapq

def dijkstra(s):
    heap = []
    distance = [10**9] * (V+1)
    distance[s] = 0
    heapq.heappush(heap, (0, s))
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
    return distance

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

node1, node2 = map(int, input().split())
distance_1 = dijkstra(1)
distance_node1 = dijkstra(node1)
distance_node2 = dijkstra(node2)

dist1 = distance_1[node1] + distance_node1[node2] + distance_node2[V]
dist2 = distance_1[node2] + distance_node2[node1] + distance_node1[V]

answer = min(dist1, dist2)

if answer >= 10 ** 9:
    answer = -1
print(answer)