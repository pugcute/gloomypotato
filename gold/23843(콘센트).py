import heapq
N, M = map(int, input().split())

times = list(map(int, input().split()))
plug = []

times.sort(reverse=True)

for time in times:
    if len(plug) < M:
        heapq.heappush(plug, time)
    else:
        tmp = heapq.heappop(plug)
        tmp += time
        heapq.heappush(plug, tmp)

print(max(plug))

