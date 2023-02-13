import copy

N, M = map(int, input().split())
seats = list(map(int, input().split()))

dict_seats = {}
answer = []
start = []
for i in range(N):
    dict_seats[i+1] = seats[i]
    answer.append(i+1)
    start.append(i+1)

answers = [start]
cnt = 1
for i in range(1, 2*N):
    for j in range(N):
        answer[j] = dict_seats[answer[j]]
    if start == answer:
        break
    else:
        answers.append(copy.deepcopy(answer))
        cnt += 1

print(*answers[M % cnt])

