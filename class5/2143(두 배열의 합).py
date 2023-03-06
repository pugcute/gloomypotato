
from bisect import bisect_left, bisect_right


T = int(input())
N1 = int(input())
A = list(map(int, input().split()))
N2 = int(input())
B = list(map(int, input().split()))


sums_A = []
sums_B = []
for i in range(N1):
    s = A[i]
    sums_A.append(A[i])
    for j in range(i+1, N1):
        s += A[j]
        sums_A.append(s)

for i in range(N2):
    s = B[i]
    sums_B.append(B[i])
    for j in range(i+1, N2):
        s += B[j]
        sums_B.append(s)

answer = 0
sums_A.sort()
sums_B.sort()


for S in sums_A:
    answer += bisect_right(sums_B, T-S) - bisect_left(sums_B, T-S)
print(answer)
