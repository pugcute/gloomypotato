
words = input()


N = len(words)
idx = 0


dict_alpa = ['c-', 'd-', 'lj', 'nj', 's=', 'z=', 'c=']


answer = 0
while idx < N:
    if words[idx: idx+3] == 'dz=':
        idx += 3
        answer += 1
        continue
    elif words[idx: idx+2] in dict_alpa:
        idx += 2
        answer += 1
        continue
    else:
        answer += 1
        idx += 1

print(answer)