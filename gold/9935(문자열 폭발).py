
words = input()
stack = []
explosion = input()

for word in words:
    stack.append(word)
    if len(stack) >= len(explosion):

        tmp = stack[len(stack)-len(explosion):]
        if explosion == ''.join(tmp):
            for i in range(len(explosion)):
                stack.pop()


if stack:
    print(''.join(stack))
else:
    print("FRULA")
