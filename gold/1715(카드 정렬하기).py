import sys
import heapq

N = int(input())
heap = []
for _ in range(N):
    tmp = int(sys.stdin.readline())
    heapq.heappush(heap, tmp)

answer = 0
if len(heap) <= 1:
    answer = 0
else:
    while len(heap) > 1:
        tmp1 = heapq.heappop(heap)
        tmp2 = heapq.heappop(heap)
        sum1 = tmp1 + tmp2
        answer += sum1
        heapq.heappush(heap, sum1)

print(answer)