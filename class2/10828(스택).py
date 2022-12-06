import sys
N = int(input())

stack = []
for i in range(N):
    list1 = list(map(str, sys.stdin.readline().split()))
    if len(list1) > 1:
        stack.append(int(list1[1]))
    else:
        if list1[0] == 'top':
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
        else:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
