N = int(input())

surpluses = {}
i = 11
answer = 2
if N == 1:
    answer = 1
else:
    while i % N != 0:
        i = i % N
        if not surpluses.get(i):
            surpluses[i] = 1
            i = i * 10 + 1
            answer += 1
        else:
            answer = -1
            break

print(answer)

