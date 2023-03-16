matrix = []
for i in range(10):
    tmp = list(input())
    for j in range(10):
        if tmp[j] == 'O':
            tmp[j] = True
            continue
        tmp[j] = False
    matrix.append(tmp)

dx = [1, -1, 0, 0, 0]
dy = [0, 0, 0, 1, -1]
answer = 10**9
for f in range(1 << 10):
    tmp = []
    for i in range(10):
        tmp.append(matrix[i][:])
    cnt = 0

    for i in range(10):
        if f & (1 << i):
            cnt += 1
            for k in range(5):
                nx, ny = i + dx[k], 0 + dy[k]
                if 0 <= nx < 10 and 0 <= ny < 10:
                    tmp[ny][nx] = not tmp[ny][nx]

    for i in range(1, 10):
        for j in range(10):
            if not tmp[i - 1][j]:
                continue
            for k in range(5):
                nx, ny = j + dx[k], i + dy[k]
                if 0 <= nx < 10 and 0 <= ny < 10:
                    tmp[ny][nx] = not tmp[ny][nx]
            cnt += 1

    checker = True
    for i in range(10):
        if tmp[9][i]:
            checker = False

    if checker:
        answer = min(cnt, answer)

if answer == 10 ** 9:
    answer = -1
print(answer)
