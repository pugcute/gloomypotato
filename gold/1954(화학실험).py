N = int(input())
chems = []
for _ in range(N):
    a, b = map(int, input().split())
    chems.append([a, b])

M = int(input())

answer = 0
cnt = 1

while True:
    flag = 1
    tmp = 0
    for chem in chems:
        if (cnt - chem[1]) % chem[0] == 0:
           tmp += (cnt - chem[1]) // chem[0]
        else:
            flag = 0
            break
    if flag == 1:
        if tmp == M:
            answer = cnt
        elif tmp > M:
            break
    cnt += 1

print(answer)