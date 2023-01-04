import sys
from collections import deque

def RD(method):
    global cnt
    if method == 'D':
        if cnt % 2:
            if len(deck) > 0:
                deck.pop()
        else:
            if len(deck) > 0:
                deck.popleft()
    else:
        cnt += 1


    return 1

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    answer = 0
    functions = list(sys.stdin.readline().rstrip())
    list_count = int(sys.stdin.readline().rstrip())
    string_A = sys.stdin.readline().rstrip()[1:-1]


    if len(string_A) > 0:
        list_A = list(map(int, string_A.split(',')))
    else:
        list_A = []

    deck = deque(list_A)
    cnt = 0
    if len(deck) < functions.count('D'):
        print('error')
    else:

        for function in functions:
            answer = RD(function)
        answer = ''

        if cnt % 2:
            deck.reverse()
            answer += '[' + ','.join(map(str, list(deck))) + ']'
            print(answer)
        else:
            answer += '[' + ','.join(map(str, list(deck))) + ']'
            print(answer)
            # 시간 문제 마지막으로 해야 함