

def DFS():
    global number
    global answer
    if number:
        answer.add(int("".join(map(str, number))))
    for i in range(10):
        if not number or number[-1] > i:
            number.append(i)
            DFS()
            number.pop()



N = int(input())
answer = set()
number = []
DFS()
answer = list(answer)
answer.sort()

if len(answer) < N:
    print(-1)
else:
    print(answer[N-1])
