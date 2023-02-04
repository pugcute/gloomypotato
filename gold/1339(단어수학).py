

dict_alpa = {}
N = int(input())
for i in range(ord('A'), ord('Z')+1):
    dict_alpa[chr(i)] = 0

for _ in range(N):
    word = input()
    for i in range(len(word)):
        num = 10 ** (len(word) - i -1)
        dict_alpa[word[i]] += num

tmp = []
for key, val in dict_alpa.items():
    if val > 0:
        tmp.append([key, val])
answer = 0
tmp.sort(key=lambda x:x[1], reverse=True)

for idx in range(len(tmp)):
    answer += tmp[idx][1] * (9-idx)
print(answer)