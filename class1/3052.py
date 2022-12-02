# 나머지

tmp = []
for i in range(10):
    a = int(input())
    tmp.append(a % 42)
print(len(list(set(tmp))))
