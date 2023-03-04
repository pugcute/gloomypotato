N = int(input())

for _ in range(N):
    time = int(input())
    cnt_60, cnt_10, cnt_1 = time // 60, (time % 60) // 10, time % 10
    if cnt_1 > 5:
        cnt_10 += 1
        cnt_1 -= 10
    if cnt_10 > 3:
        cnt_60 += 1
        cnt_10 -= 6
    if cnt_10 < 0 and cnt_1 == 5:
        cnt_1 -= 10
        cnt_10 += 1

    answer = []
    answer.append(cnt_60)
    if cnt_10 >= 0:
        answer.append(cnt_10)
        answer.append(0)
    else:
        answer.append(0)
        answer.append(-cnt_10)
    if cnt_1 >= 0:
        answer.append(cnt_1)
        answer.append(0)
    else:
        answer.append(0)
        answer.append(-cnt_1)
    print(*answer)
