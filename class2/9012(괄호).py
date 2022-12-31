import sys

def checkVPS(string):
    checker = 0
    while len(string):
        word = string.pop()
        if word == '(':
            checker += 1
        else:
            checker -= 1
        if checker < 0:
            return 'NO'
    if checker == 0:
        return 'YES'
    else:
        return 'NO'


N = int(input())

for _ in range(N):
    string = list(sys.stdin.readline().rstrip())
    print(checkVPS(string[::-1]))
