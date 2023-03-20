import math

N = input()
list_N = list(map(int, N))
numbers = [i for i in range(1, 10)]
origin_N = int(N)
lcm = 1
for num in list_N:
    if num in numbers:
        lcm = math.lcm(num, lcm)

if origin_N % lcm == 0:
    print(N)
else:

    cnt = 1
    while True:
        flag = 0
        for i in range(0, 10 ** cnt):
            tmp = int(N + '0' * (cnt - len(str(i))) + str(i))
            if tmp % lcm == 0:
                flag = 1
                break
        if flag:
            print(tmp)
            break
        else:
            cnt += 1
