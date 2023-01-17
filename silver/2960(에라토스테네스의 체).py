

def sosu(n):
    if n == 2:
        return True
    elif n == 3:
        return True
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

N, K = map(int, input().split())


numbers = [i for i in range(2, N+1)]

total_cnt = 0
answer = 0
while True:
    num = numbers[0]
    cnt = 1
    if sosu(num):
        for num1 in numbers:
            if num1 % num == 0:
                numbers.remove(num1)
                total_cnt += 1
                if total_cnt == K:
                    answer = num1
    if answer != 0:
        break
print(answer)