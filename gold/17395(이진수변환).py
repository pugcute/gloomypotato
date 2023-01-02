
X, N = map(int, input().split())

bin_X = list(bin(X))

cnt = 1
answer = []
if bin_X.count('1') < N:
    print(-1)
else:
    while cnt <= N:
        if cnt < N:
            for i in range(2, len(bin_X)):
                if bin_X[i] == '1':
                    bin_X[i] = '0'
                    number = ''.join(bin_X)
                    answer.append(int(number, 2))
                    cnt += 1
                    break
        else:
            answer.append(0)
            cnt += 1

for ans in answer:
    print(ans, end=' ')