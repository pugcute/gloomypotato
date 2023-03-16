import sys

N, M = map(int, sys.stdin.readline().split())
arrays = [i for i in range(M)]
dict_stack = {}
stack = []
for _ in range(N):
    tmp = set()
    inputs = list(map(int, sys.stdin.readline().split()))
    if len(inputs) >= 2:
        if inputs[0] == 1:
            stack.append(inputs[1] % M)
            if stack[-1] not in dict_stack.keys():
                dict_stack[stack[-1]] = len(stack) - 1
            else:
                dict_stack[stack[-1]] = len(stack) - 1
    else:
        if inputs[0] == 3:
            if len(dict_stack.keys()) == M:
                tmp = min(dict_stack.values())
                print(len(stack) - tmp)
            else:
                print(-1)
        else:
            if stack:
                tmp = stack.pop()
                flag = 1
                for i in range(len(stack) - 1, -1, -1):
                    if tmp == stack[i]:
                        dict_stack[tmp] = i
                        flag = 0
                        break
                if flag:
                    del dict_stack[tmp]