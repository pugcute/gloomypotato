


N = int(input())
numbers = [0, 1]
for i in range(2, N+1):
    numbers.append((numbers[i-1] +numbers[i-2]) % 1000000007)
print(numbers[N])