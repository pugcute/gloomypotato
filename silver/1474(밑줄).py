from itertools import combinations

N, K = map(int, input().split())

words = []
total_length = 0
for _ in range(N):
    word = input()
    total_length += len(word)
    words.append(word)

add_length = K - total_length

answer = ''
if add_length == 0:
    for word in words:
        answer += word

else:
    if add_length % (N - 1) == 0:
        for i in range(N):
            answer += words[i]
            if i < N-1:
                answer += '_' * (add_length // (N-1))

    else:
        tmp = add_length // (N-1)
        min_count = 0
        max_count = 0
        for i in range(N-1):
            if i * tmp + (N-1-i) * (tmp + 1) == add_length:
                min_count = i
                max_count = N - 1 - i
        max_count_list = list(combinations([i for i in range(N-1)], max_count))
        answer_list = []
        for max_set in max_count_list:
            tmp_word = ''
            for i in range(N-1):
                if i in max_set:
                    tmp_word += words[i]
                    tmp_word += '_' * (tmp+1)
                else:
                    tmp_word += words[i]
                    tmp_word += '_' * tmp
            tmp_word += words[N-1]
            answer_list.append(tmp_word)
        answer_list.sort()
        answer = answer_list[0]



print(answer)