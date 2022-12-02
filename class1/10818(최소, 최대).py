N = int(input())
tmp = list(map(int, input().split()))

max_val = -1000000
min_val = 1000000
for w in tmp:
    if max_val < w:
        max_val = w
    if min_val > w:
        min_val = w
print(min_val, max_val)