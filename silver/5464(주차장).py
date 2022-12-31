import sys
from collections import deque

N, M = map(int, input().split())

stops = [False] * N
stops_expense = []
cars_expense = []
cars_dict = {}
for _ in range(N):
    stop = int(sys.stdin.readline().rstrip())
    stops_expense.append(stop)

for _ in range(M):
    car = int(sys.stdin.readline().rstrip())
    cars_expense.append(car)

tmp_stops = deque()
for _ in range(2*M):
    step = int(sys.stdin.readline().rstrip())
    if step-1 >= 0:
        for idx in range(N):
            if stops[idx] is False:
                stops[idx] = True
                cars_dict[step-1] = idx
                break
            elif idx == N-1 and stops[idx] is True:
                tmp_stops.append(step-1)

    else:
        if len(tmp_stops) == 0:
            stops[cars_dict[-1 * step-1]] = False
        else:

            stops[cars_dict[-1 * step - 1]] = False
            stops[cars_dict[-1 * step - 1]] = True
            tmp_stop = tmp_stops.popleft()
            cars_dict[tmp_stop] = cars_dict[-step - 1]

answer = 0

for key, val in cars_dict.items():
    answer += cars_expense[key] * stops_expense[val]

print(answer)


