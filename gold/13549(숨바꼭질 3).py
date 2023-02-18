from collections import deque

N, K = map(int, input().split())

MAX_SIZE = 100001
check_count = [-1] * MAX_SIZE
check_count[N] = 0
to_visits = deque([N])
while to_visits:
    current = to_visits.popleft()
    if current == K:
        break
    if current * 2 < 100001:
        check_count[current * 2] = check_count[current]
        to_visits.append(current * 2)
    for next_val in [current + 1, current - 1]:
        if 0 <= next_val < MAX_SIZE:
            if check_count[next_val] == -1 or check_count[next_val] >= check_count[current] + 1:
                check_count[next_val] = check_count[current] + 1
                to_visits.append(next_val)

print(check_count[K])

