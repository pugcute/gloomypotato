# 원래는 정렬, 이분탐색이나, 그냥 해시맵으로 품

N = int(input())
A = list(map(int, input().split()))
A_hash = {}
for num in A:
    A_hash[num] = 1

M = int(input())
answers = list(map(int, input().split()))

for num1 in answers:
    try:
        if A_hash[num1] == 1:
            print(1)
    except:
        print(0)
