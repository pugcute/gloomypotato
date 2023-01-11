import heapq

heap = []
points = [[0, 3, 7], [1, 0, 9], [1, 5, 8], [3, 0, 6]]

for point in points:
    tmp = [point[1], point[0], point[2]]
    print(tmp)
    heapq.heappush(heap, tmp)

heap.sort(key=lambda x:x[0])
print(heap)
