import math

def gcd(tmp, tmp1):
    answer = 0
    if tmp1 == 0:
        return tmp
    if math.gcd(tmp, tmp1) == 1:
        return 1
    else:
        answer = gcd(tmp1, tmp % tmp1)
    return answer

N, M = map(int, input().split())

answer = 0
if N >= M:
    answer = gcd(N, M)
else:
    answer = gcd(N, M)
print('1' * answer)
