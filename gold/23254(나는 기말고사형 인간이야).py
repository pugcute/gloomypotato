import heapq

N, M = map(int, input().split())

scores = list(map(int, input().split()))
adds = list(map(int, input().split()))

heap = []
for i in range(M):
    if scores[i] + adds[i] > 100:
        adds[i] = 100 - scores[i]
    heapq.heappush(heap, [-adds[i], scores[i]])

time = 24 * N

cnt = 0
while cnt < time:
    add, score = heapq.heappop(heap)
    score -= add
    if score - add > 100:
        add = score - 100
    heapq.heappush(heap, [add, score])
    cnt += 1


answer = 0
for tmp in heap:
    answer += tmp[1]
print(answer)