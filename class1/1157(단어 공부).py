
strings = input()
upper_strings = strings.upper()
words_set = list(set(upper_strings))
tmp = []
for word in words_set:
    cnt = upper_strings.count(word)
    tmp.append(cnt)




if tmp.count(max(tmp)) > 1:
    print("?")
else:
    print(words_set[tmp.index(max(tmp))])
