num = int(input())
for i in range(num):
    cnt, words = input().split()
    final = ''
    for word in words:
        final += word * int(cnt)
    print(final)