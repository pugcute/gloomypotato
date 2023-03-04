

N = int(input())
M = int(input())

route1 = []
route2 = []

for i in range(M):
    start, end = map(int, input().split())

    if start > end:
        route1.append([start-N, end, i+1])
        route2.append([start, end+N, i+1])
    else:

        route1.append([start, end, i+1])
        route2.append([start, end, i+1])

route1.sort(key=lambda x:(x[0], -x[1]))
route2.sort(key=lambda x:(x[0], -x[1]))

remove_list = []

checker = [1] * (M+1)
state = route1[0]

for i in range(1, M):
    if state[1] >= route1[i][1]:
        remove_list.append(route1[i][2])
        checker[route1[i][2]] = 0
    elif state[1] < route1[i][1]:
        state = route1[i]

state = route2[0]

for i in range(1, M):
    if state[1] >= route2[i][1]:
        remove_list.append(route2[i][2])
        checker[route2[i][2]] = 0
    elif state[1] < route2[i][1]:
        state = route2[i]

answer = []
for i in range(1, M+1):
    if checker[i] > 0:
        answer.append(i)

print(*answer)