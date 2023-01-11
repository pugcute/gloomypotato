


N = int(input())
words = input()
stack = []
dict_alpa = {}
for i in range(N):
    tmp = int(input())
    dict_alpa[chr(65+i)] = tmp

for word in words:
    if word not in ['+', '-', '*', '/']:
        stack.append(dict_alpa[word])
    else:
        first = stack.pop()
        second = stack.pop()
        if word == '+':
            stack.append(first + second)
        elif word == '-':
            stack.append(second - first)
        elif word == '/':
            stack.append(second / first)
        elif word == '*':
            stack.append(first * second)

print(f'{stack[0]:.2f}')