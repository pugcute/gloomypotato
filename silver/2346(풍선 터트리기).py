from collections import deque

N = int(input())
deq = deque(enumerate(map(int, input().split()), start=1))


for i in range(N):
    current = deq.popleft()
    print(current[0], end=' ')
    if current[1] > 0:
        deq.rotate(-current[1]+1)
    else:
        deq.rotate(-current[1])




#
# current_idx = 1
# while balls:
#     tmp = balls[0]
#     if tmp > 0:
#         balls.rotate(tmp)
#         next_idx = (current_idx + tmp + len(balls)) % len(balls)
#         balls.popleft()
#
#     else:
#         balls.rotate(tmp)
#         next_idx = (current_idx + tmp + len(balls)) % len(balls)
#         balls.popleft()
#     print(next_idx)

