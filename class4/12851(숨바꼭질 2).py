from collections import deque

N, X = map(int, input().split())
MAX_SIZE = 100001

to_visits = deque([N])


answer = 0
check_count = [-1] * MAX_SIZE
check_count[N] = 0
while to_visits:
    current = to_visits.popleft()
    if current == X:
        answer += 1
    for next_val in [current * 2, current + 1, current - 1]:
        if 0 <= next_val < MAX_SIZE:
            if check_count[next_val] == -1 or check_count[next_val] >= check_count[current] + 1:
                check_count[next_val] = check_count[current] + 1
                to_visits.append(next_val)

print(check_count[X])
print(answer)