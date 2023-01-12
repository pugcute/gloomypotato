import sys
sys.setrecursionlimit(10**8)

def exponentiation(x, n):
    cnt = 0
    if n == 0:
        return 1
    if n == 1:
        return x % C
    else:
        tmp = exponentiation(x, n // 2)
        if n % 2:
           cnt = ((tmp % C) * (tmp % C) * (x % C)) % C
        else:
           cnt = ((tmp % C) * (tmp % C)) % C
    return cnt

A, B, C = map(int, input().split())
answer = exponentiation(A, B)
print(answer)