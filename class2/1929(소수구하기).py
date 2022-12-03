
a, b = map(int, input().split())


for num in range(a, b+1):
    if 1 < num < 4:
        print(num)
    for k in range(2, int(num**0.5)+1):
        if num % k == 0:
            break
        if k == int(num**0.5):
            print(num)
