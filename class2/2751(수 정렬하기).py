import sys

N = int(input())
list1 = []
for i in range(N):
    a = int(sys.stdin.readline())
    list1.append(a)
list1.sort()
for num in list1:
    print(num)