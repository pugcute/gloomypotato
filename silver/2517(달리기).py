import sys
import copy
N = int(input())
list_A = []
for _ in range(N):
    tmp = int(sys.stdin.readline().rstrip())
    list_A.append(tmp)

# dict_A = {}
# set_A = list(set(sorted(list_A)))
# for idx, val in enumerate(set_A):
#     dict_A[val] = idx
#
# contract = []

for idx in range(N):
    if idx == 0:
        print(1)
    else:
        base = list_A[idx]
        cnt = idx + 1
        for j in range(idx):
            if list_A[j] < base:
                cnt -= 1
        print(cnt)
        # base = dict_A[list_A[idx]]
        # cnt = idx + 1
        # for j in range(idx):
        #     if dict_A[list_A[j]] < base:
        #         cnt -= 1
        # print(cnt)



