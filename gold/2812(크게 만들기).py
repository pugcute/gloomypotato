
N, K = map(int, input().split())
numbers = list(input())

cnt = K
stack = []

for num in numbers:
    while cnt > 0 and stack and stack[-1] < num:
        stack.pop()
        cnt -= 1
    stack.append(num)


print(''.join(stack[:N-K]))

