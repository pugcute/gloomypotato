import heapq
T, N = map(int, input().split())

heap = []
for _ in range(N):
    A, B, C = map(int, input().split())
    heapq.heappush(heap, [-C, A, B])


for i in range(1, T+1):
    if heap:
        priority, pid, time = heapq.heappop(heap)
        time -= 1
        priority += 1
        print(pid)
        if time != 0:
            heapq.heappush(heap, [priority, pid, time])




