N = int(input())
numbers = list(map(int, input().split()))
set_numbers = list(set(numbers))


dict_idx = {}
set_numbers.sort()
for idx, val in enumerate(set_numbers):
    dict_idx[val] = idx

for num in numbers:
    print(dict_idx[num], end=' ')