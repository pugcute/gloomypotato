from itertools import permutations

N = int(input())
numbers = [i for i in range(1, N+1)]
inputs = list(map(int, input().split()))
used = [0 for _ in range(N)]

perms = list(permutations(numbers, N))

if inputs[0] == 2:
    target = inputs[1:]
    for i in range(len(perms)):
        if target == list(perms[i]):
            print(i + 1)
            break
        else:
            continue
else:
    print(*perms[inputs[1]-1])

