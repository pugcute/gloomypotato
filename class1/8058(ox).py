N = int(input())
for i in range(N):
    text = input()
    tmp_list = list(text.split('X'))
    total = 0
    for tmp in tmp_list:
        total += (tmp.count('O') * (tmp.count('O') + 1))/2
    print(int(total))