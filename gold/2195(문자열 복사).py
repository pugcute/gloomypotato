import sys

start = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()

idx = 0
copy_words = ''
answer = 0
while idx < len(target):
    max_length = 0
    max_words = ''
    if len(target) - len(copy_words) <= len(start):
        check_length = len(start) + 1
    else:
        check_length = len(target) - len(copy_words) + 1
    for i in range(check_length, 0, -1):
        flag = 1
        checking = target[idx:idx+i]
        for j in range(0, len(start)-i+1):
            if start[j:j+i] == checking:
                max_words = start[j:j+i]
                flag = 0
                break
        if flag == 0:
            break
    copy_words += max_words
    max_length = len(max_words)
    idx += max_length
    answer += 1

print(answer)

