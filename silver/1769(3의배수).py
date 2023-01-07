import copy
N = list(map(int, input()))
tmp = copy.deepcopy(N)
flag = 0
cnt = 0
while len(tmp) > 0:

    if len(N) == 1:
        if N[0] % 3 == 0:
            flag = 1
        else:
            flag = 0
        break
    else:
        number = sum(tmp)
        if len(tmp) == 1:
            if number % 3 == 0:
                flag = 1
            else:
                flag = 0
            break
        else:
            cnt += 1
            tmp = list(map(int, str(number)))

if flag:
    print(cnt)
    print('YES')
else:
    print(cnt)
    print('NO')