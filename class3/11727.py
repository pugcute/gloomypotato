
N = int(input())

numbers = [1, 3]
for i in range(2, N+1):
    numbers.append(numbers[i-1]+2*numbers[i-2])

print(numbers[N-1] % 10007)