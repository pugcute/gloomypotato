from bisect import bisect_left

N, M = map(int, input().split())
trees = list(map(int, input().split()))


trees.sort()
end = trees[-1]
start = 0

while start <= end:
    result = 0
    if start > end:
        break
    mid = (start + end) // 2

    for tree in trees[bisect_left(trees, mid):]:
        if tree > mid:
            result += tree - mid

    if result < M:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)