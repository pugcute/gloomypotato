import sys

N = int(input())
matrix = [0] * 10001
for _ in range(N):
    tmp = int(sys.stdin.readline())
    matrix[tmp] += 1

for i in range(10001):
    for j in range(matrix[i]):
        print(i)