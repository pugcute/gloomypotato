from collections import deque

words = list(input())

words.sort()
deq = deque(words)
answer = ''
flag = 0
if len(deq) == 2:
    if deq[0] != deq[1]:
        print('I\'m Sorry Hansoo')
    else:
        print(''.join(list(deq)))
else:
    while deq:
        if len(deq) > 1:
            first = deq.pop()
            second = deq.pop()
            if first == second:
                answer = first + answer + second
            else:
                flag += 1
                deq.appendleft(first)
                deq.append(second)

        else:
            second = deq.pop()
            answer = answer[0:len(answer)//2] + second + answer[len(answer)//2:]

        if flag > 1:
            print('I\'m Sorry Hansoo')
            break

if flag < 2:
    print(answer)