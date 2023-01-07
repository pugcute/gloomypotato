
N = int(input())

for _ in range(N):
    numbers = [1, 2, 4]
    num = int(input())
    for i in range(3, num):
        numbers.append(numbers[i-2]+numbers[i-1]+numbers[i-3])

    print(numbers[num-1])