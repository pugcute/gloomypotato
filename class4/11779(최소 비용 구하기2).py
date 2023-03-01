import sys
import heapq
from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
prev_node = [0] * (N+1)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])

distance = [10**9] * (N+1)


def dijkstra(start):
    heap = []
    distance[start] = 0
    prev_node[start] = start
    heapq.heappush(heap, (0, start))
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                prev_node[i[0]] = now
                heapq.heappush(heap, (cost, i[0]))


start, end = map(int, input().split())

dijkstra(start)

deq = deque([])
answer = []
deq.append(end)
while deq:
    node = deq.popleft()
    answer.append(node)
    if node == start:
        break
    deq.append(prev_node[node])

print(distance[end])
print(len(answer))
print(*answer[::-1])
