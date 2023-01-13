import sys
from bisect import bisect_left


K, N = map(int, input().split())
pipes = []
for _ in range(K):
    tmp = int(sys.stdin.readline())
    pipes.append(tmp)
pipes.sort()
start = 1
end = pipes[-1]

while start <= end:
    result = 0
    if start > end:
        break
    mid = (start + end) // 2
    for pipe in pipes[bisect_left(pipes, mid):]:
        if mid != 0:
            result += pipe // mid

    if result < N:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)
