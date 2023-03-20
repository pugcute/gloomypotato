N = int(input())

words = []
for _ in range(N):
    command, word, second = input().split()
    if command == 'type':
        words.append(['add', word, int(second)])
    else:
        for i in range(len(words)-1, -1, -1):
            if words[i][2] + int(word) < int(second):
                continue
            if words[i][0] == 'add':
                words[i][0] = 'delete'
            elif words[i][0] == 'delete':
                words[i][0] = 'add'
            else:
                for j in range(i-1, -1, -1):
                    if words[j][2] + words[i][1] < words[i][2]:
                        continue
                    if words[j][0] == 'add':
                        words[j][0] = 'delete'
                    elif words[j][0] == 'delete':
                        words[j][0] = 'add'

        words.append(['undo', int(word), int(second)])

answer = ''
for word in words:
    if word[0] == 'add':
        answer += word[1]
print(answer)