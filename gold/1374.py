import sys
import heapq

N = int(input())
lectures = []
for _ in range(N):
    a, start, end = map(int, input().split())
    lectures.append([start, end])

heap = [0]

lectures.sort(key=lambda x:x[0])
answer = 1
for lecture in lectures:
    if heap[0] <= lecture[0]:
        heapq.heappop(heap)
    else:
        answer += 1
    heapq.heappush(heap, lecture[1])
print(answer)