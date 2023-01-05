N =int(input())

for _ in range(N):
    num = int(input())
    numbers = [1, 1, 1]
    for i in range(3, num+1):
        numbers.append(numbers[i-3]+numbers[i-2])
    print(numbers[num-1])