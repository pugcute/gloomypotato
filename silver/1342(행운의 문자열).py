from itertools import permutations


words = list(input())

permuation = list(permutations(words, len(words)))

answer = 0
answer_list = []
for per in permuation:
    flag = 0
    if len(per) == len(list(set(per))):
        answer_list.append(per)
        answer += 1
    else:
        for i in range(0, len(per), 2):
            if per[i] == per[i+1]:
                flag = 1
                break
            else:
                continue
        if flag == 0 and per not in answer_list:
            answer_list.append(per)
            answer += 1
        else:
            continue
print(answer)
