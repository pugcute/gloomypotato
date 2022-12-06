M = int(input())
M_list = list(map(int, input().split()))
N = int(input())
N_list = list(map(int, input().split()))

M_dict = {}
for num in M_list:
    if num not in M_dict.keys():
        M_dict[num] = 1
    else:
        M_dict[num] += 1

for num1 in N_list:
    try:
        print(M_dict[num1], end=' ')
    except:
        print(0, end= ' ')