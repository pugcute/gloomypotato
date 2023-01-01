# 50점 풀이
N = int(input())
M = int(input())
strings = input()

IOI = 'I' + 'OI'* N

answer = 0
for start_idx in range(len(strings)-len(IOI)+1):
    if strings[start_idx] == 'O':
        continue
    else:
        if strings[start_idx:len(IOI)+start_idx] == IOI:
            answer += 1

print(answer)