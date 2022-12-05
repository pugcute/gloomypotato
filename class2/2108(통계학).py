import math
import sys
# sys 안쓰면 시간초과
N = int(input())
numbers = []
numbers_dict = {}
for i in range(N):
    a = int(sys.stdin.readline())
    if a not in numbers_dict.keys():
        numbers_dict[a] = 1
    else:
        numbers_dict[a] += 1
    numbers.append(a)

average = round(sum(numbers) / N)
numbers.sort()
middle = numbers[N // 2]
print(average)
print(middle)

check = [key for key, value in numbers_dict.items() if value == max(numbers_dict.values())]
zxc = 0
check.sort()
if len(check) == 1:
    zxc = check[0]
else:
    zxc = check[1]

print(zxc)
zxc1 = max(numbers) - min(numbers)
print(zxc1)


