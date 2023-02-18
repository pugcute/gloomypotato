import sys
from itertools import combinations


N, K = map(int, input().split())
words = []
alpa_list = []

for _ in range(N):
    tmp = sys.stdin.readline().rstrip()
    words.append(tmp)
    alpa_list.extend(list(tmp))


alpa_list = list(set(alpa_list))

# lists = list(combinations(alpa_list, K))
answer = 0
T = len(alpa_list)
for i in range(1<<T):
    subnet = []
    for j in range(T):
        if i & (1<<j):
            subnet.append(alpa_list[j])

    if len(subnet) != K:
        continue
    else:
        tmp_answer = 0
        for word in words:
            for k in range(len(word)):
                if word[k] in subnet:
                    if k == len(word)-1:
                        tmp_answer += 1
                        print(tmp_answer)
                    else:
                        break
        answer = max(answer, tmp_answer)
print(answer)