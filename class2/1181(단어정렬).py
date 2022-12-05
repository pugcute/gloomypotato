import sys
N = int(input())
strings = []
for i in range(N):
    strings.append(input())
strings = list(set(strings))
strings.sort()
strings_dict = {}
for string in strings:
    if len(string) not in strings_dict.keys():
        strings_dict[len(string)] = [string]
    else:
        strings_dict[len(string)].append(string)


for key in sorted(strings_dict.keys()):
    for word in strings_dict[key]:
        print(word)

