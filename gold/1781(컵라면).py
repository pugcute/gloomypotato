import sys
import heapq

N = int(sys.stdin.readline())

homeworks = []
for _ in range(N):
    day, ramen = map(int, sys.stdin.readline().split())
    homeworks.append([day, ramen])

homeworks.sort(key=lambda x:x[0])
heap = []

for day, ramen in homeworks:
    heapq.heappush(heap, ramen)
    if day < len(heap):
        heapq.heappop(heap)

print(sum(heap))

