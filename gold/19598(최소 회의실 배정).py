import sys
import heapq

N = int(input())
lectures = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    lectures.append([start, end])

lectures.sort(key=lambda x:x[0])

heap = [0]
answer = 1
for lecture in lectures:
    if lecture[0] >= heap[0]:
        heapq.heappop(heap)
    else:
        answer += 1
    heapq.heappush(heap, lecture[1])
print(answer)