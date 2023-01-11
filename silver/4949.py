
while True:
    words = input()
    if words == '.':
        break
    stack = []
    flag = 0
    for word in words:
        if word in ['(', '[']:
            stack.append(word)
        if word in [')', ']']:
            if len(stack) == 0:
                flag = 1
                break
            else:
                tmp = stack.pop()
                if word == ')' and tmp == '(':
                    continue
                if word == ']' and tmp == '[':
                    continue
                else:
                    flag = 1
                    break
    if len(stack) > 0:
        flag = 1

    if flag == 0:
        print('yes')
    else:
        print('no')