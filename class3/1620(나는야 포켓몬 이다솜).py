import sys


N, M = map(int, input().split())
cnt = 1
dict_alpa = {}
dict_num = {}
for _ in range(N):
    poke = sys.stdin.readline().rstrip()
    dict_alpa[poke] = cnt
    dict_num[str(cnt)] = poke
    cnt += 1

for _ in range(M):
    question = sys.stdin.readline().rstrip()
    if dict_alpa.get(question) is not None:
        print(dict_alpa.get(question))
    if dict_num.get(question) is not None:
        print(dict_num.get(question))