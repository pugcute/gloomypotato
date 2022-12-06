import sys

# int 안바꾸면 오류
N = int(input())
list1 = []
for i in range(N):
    a, b = map(str, sys.stdin.readline().split())
    tmp = [int(a), b]
    list1.append(tmp)

tmp_list = sorted(list1, key=lambda x:x[0])
for zxc in tmp_list:
    print(zxc[0], zxc[1])