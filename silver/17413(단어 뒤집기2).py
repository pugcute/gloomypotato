
words = input()
check = []
reverse_word = []
answer = ''

for word in words:
    if word == ' ' and len(check) == 0:
        while len(reverse_word):
            answer += reverse_word.pop()
        answer += ' '
    elif word == '<':
        check.append('<')
        if len(reverse_word):
            while len(reverse_word):
                answer += reverse_word.pop()
        answer += word
    elif word == '>':
        check.pop()
        answer += word

    elif len(check) == 0:
        reverse_word.append(word)
    else:
        answer += word

if len(reverse_word):
    while len(reverse_word):
        answer += reverse_word.pop()


print(answer)
