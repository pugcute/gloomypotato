import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jewl = []
bags = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    jewl.append([M, V])
for _ in range(K):
    M = int(sys.stdin.readline())
    bags.append(M)

jewl.sort()
bags.sort()
heap = []
answer = 0
for bag in bags:
    while jewl and jewl[0][0] <= bag:
        heapq.heappush(heap, -jewl[0][1])
        heapq.heappop(jewl)
    if heap:
        answer -= heapq.heappop(heap)
print(answer)

