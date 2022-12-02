
tmp = []
for i in range(9):
    a = int(input())
    tmp.append(a)

print(max(tmp))
print(tmp.index(max(tmp))+1)