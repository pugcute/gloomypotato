import sys

N = int(input())
for _ in range(N):
    K = int(sys.stdin.readline())
    dict_alpa = {}
    answer = 'YES'
    words = []
    for i in range(K):
        current = sys.stdin.readline().rstrip()
        words.append(current)
    words.sort()
    for word in words:
        for i in range(1, len(word)):
            if dict_alpa.get(word[:i]) == 1:
                answer = 'NO'
                break
        if answer == 'YES':
            dict_alpa[word] = 1
        else:
            break

    print(answer)