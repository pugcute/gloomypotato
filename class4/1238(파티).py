import heapq
import copy
def dijkstra(s, distance):
    heap = []
    distance[s] = 0
    heapq.heappush(heap, (0, s))
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
    return distance

V, E, S = map(int, input().split())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

distance = [10 ** 9] * (V+1)

distances = [[] for _ in range(V+1)]

for i in range(1, V+1):
    tmp = dijkstra(i, copy.deepcopy(distance))
    distances[i] = tmp

answer = 0
target = distances[S]

for i in range(1, V+1):
    tmp_answer = distances[i][S] + target[i]
    answer = max(answer, tmp_answer)
print(answer)


