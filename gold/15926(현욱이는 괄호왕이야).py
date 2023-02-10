N = int(input())

words = input()

words_cnt = [0] * N
stack = []


for idx, word in enumerate(words):
    if word == '(':
        stack.append(idx)
    elif word == ')':
        if stack:
            words_cnt[stack.pop()] = 1
            words_cnt[idx] = 1

answer = 0
tmp = 0

for idx in range(N):
    if words_cnt[idx] == 1:
        tmp += 1
        answer = max(answer, tmp)
    else:
        tmp = 0
print(answer)
