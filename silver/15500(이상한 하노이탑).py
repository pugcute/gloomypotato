from collections import deque

N = int(input())
start = list(map(int, input().split()))
tmp = []
end = []

answer = []
number = N
while number > 0:
    if number in start:
        while start[-1] != number:
            tmp.append(start.pop())
            answer.append([1, 2])
        answer.append([1, 3])
        number -= 1
        end.append(start.pop())

    if number in tmp:
        while tmp[-1] != number:
            start.append(tmp.pop())
            answer.append([2, 1])
        answer.append([2, 3])
        number -= 1
        end.append(tmp.pop())

print(len(answer))
for ans in answer:
    print(' '.join(map(str, ans)))