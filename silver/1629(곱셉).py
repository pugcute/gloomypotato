
def exponentiation(x, n):
    cnt = 0
    if n == 0:
        return 1
    else:
        if n % 2:
            cnt = x * exponentiation(x*x, (n-1)/2)
        else:
            cnt = exponentiation(x*x, n/2)
    return cnt


A, B, C = map(int, input().split())

answer = exponentiation(A, B)
print(answer % C)