import sys

N = int(input())

list1 = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    tmp = [a, b]
    list1.append(tmp)
list1.sort()

for zxc in list1:
    print(zxc[0], zxc[1])
