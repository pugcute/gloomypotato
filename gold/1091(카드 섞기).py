import copy
N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
orgin = copy.deepcopy(P)
tmp = [0, 1, 2] * (N//3)
cnt = 0
answer = [0] * N



while P != tmp:
    for i in range(N):
        answer[S[i]] = P[i]

    P = answer
    answer = [0] * N
    cnt += 1
    if orgin == P:
        cnt = -1
        break

print(cnt)

