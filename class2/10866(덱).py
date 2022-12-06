import sys
from collections import deque
N = int(input())

stack = deque()
for i in range(N):
    list1 = list(map(str, sys.stdin.readline().split()))
    if len(list1) > 1:
        if list1[0] == 'push_front':
            stack.appendleft(int(list1[1]))
        else:
            stack.append(int(list1[1]))
    else:
        if list1[0] == 'back':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
        elif list1[0] == 'size':
            print(len(stack))
        elif list1[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif list1[0] == 'pop_front':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.popleft())
        elif list1[0] == 'pop_back':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())

        elif list1[0] == 'front':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[0])


