
from collections import deque

N = int(input())
numbers = deque()
for i in range(N, 0, -1):
    numbers.append(i)

while len(numbers) != 1:
    numbers.pop()
    x = numbers.pop()
    numbers.appendleft(x)


print(numbers[0])
