
N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
sets = set()
for i in range(M):
    if i < N:
        sets.add(numbers[i])
    else:
        number = len(list(sets))
        sets.add(number)
        numbers.append(number)
print(numbers[M-1])