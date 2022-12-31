import sys


N = int(input())
stack = []
answer = []
num = 1
for _ in range(N):
    number = int(sys.stdin.readline())
    if num <= number:
        for i in range(num, number+1):
            stack.append(i)
            answer.append('+')
        num = number+1
    if number == stack.pop():
        answer.append('-')
    else:
        print('NO')
        answer = []
        break
for ans in answer:
    print(ans)