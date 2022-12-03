
def isprime(num):
    if num == 1:
        return False
    else:
        for k in range(2, int(num**0.5) + 1):
            if num % k == 0:
                return False
        return True


N = int(input())
numbers = list(map(int, input().split()))

total = 0
for num in numbers:
    if isprime(num):
        total += 1
print(total)

