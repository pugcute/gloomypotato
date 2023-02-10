import heapq

N = int(input())
lectures = []
for _ in range(N):
    idx, start, end = map(int, input().split())
    lectures.append([start, end, idx])

lectures.sort(key=lambda x:x[0])
heap = []
rooms = [0] * (N + 1)

answer = 0
for lecture in lectures:
    if heap and heap[0][0] <= lecture[0]:
        rooms[lecture[2]] = rooms[heap[0][2]]
        heapq.heappop(heap)
    else:
        answer += 1
        rooms[lecture[2]] = answer
    heapq.heappush(heap, [lecture[1], lecture[0], lecture[2]])

print(max(rooms))
for ans in rooms[1:]:
   print(ans)