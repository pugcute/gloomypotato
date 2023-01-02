
S = input()
T = input()

answer = 0
while len(S) < len(T):
    if T[-1] == 'A':
        T = T[:-1]
        if S == T:
            answer = 1
    else:
        T = T[:-1]
        T = T[::-1]
        if S == T:
            answer = 1
print(answer)