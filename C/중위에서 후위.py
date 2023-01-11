
words = input()
stack = []
answer = []
prior = {'(': 0, '+': 1, '-': 1, '*':2, '/' : 2}

for word in words:
    if word not in ['(', ')', '+', '-', '*', '/']:
        answer.append(word)
    else:
        if word == '(':
            stack.append(word)
        elif word == ')':
            tmp = stack.pop()
            while tmp != '(':
                answer.append(tmp)
                tmp = stack.pop()

        else:
            while len(stack) and prior[stack[-1]] >= prior[word]:
                tmp1 = stack.pop()
                answer.append(tmp1)
            stack.append(word)

if len(stack):
    while stack:
        tmp = stack.pop()
        answer.append(tmp)

print(''.join(answer))