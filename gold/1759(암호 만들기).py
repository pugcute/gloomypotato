import sys
sys.setrecursionlimit(10**8)
from itertools import permutations

def DFS(answer):

    if len(answer) == L:
        vowel_cnt = 0
        not_vowel_cnt = 0
        for word in answer:
            if word in vowels:
                vowel_cnt += 1
            else:
                not_vowel_cnt += 1
        if vowel_cnt >= 1 and not_vowel_cnt >= 2:
            print(answer)
        return
    if len(answer) < L:
        for tmp in words:
            if ord(answer[-1]) < ord(tmp):
               DFS(answer+tmp)
    return

L, C = map(int, input().split())

words = list(map(str, input().split()))
vowels = ['a', 'e', 'i', 'o', 'u']
words.sort()

for start in words:
    DFS(start)

