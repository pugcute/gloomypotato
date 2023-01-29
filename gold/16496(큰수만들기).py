from functools import cmp_to_key
# 람다는 인자는 무조건 한개, 그래서 정렬힘듬, 여러개 일때 사용

def compare(a, b):
    ab = int(a+b)
    ba = int(b+a)
    if ab < ba:
        return 1
    elif ab == ba:
        return 0
    else:
        return -1

N = int(input())

numbers = list(input().split())

numbers.sort(key=cmp_to_key(compare))

answer = ''.join(numbers)
if answer.count('0') == len(answer):
    print(0)
else:
    print(answer)