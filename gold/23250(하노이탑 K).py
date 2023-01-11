import sys

def hanoi(n, start, tmp, end):
    global cnt
    if n == 1:
        cnt += 1
        if cnt == K:
            print(start, end)
            sys.exit()
    else:
        hanoi(n-1, start, end, tmp)
        cnt += 1
        if cnt == K:
            print(start, end)
            sys.exit()
        hanoi(n-1, tmp, start, end)


N, K = map(int, input().split())
cnt = 0
hanoi(N, '1', '2', '3')