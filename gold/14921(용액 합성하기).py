N = int(input())
numbers = list(map(int, input().split()))

start = 0
end = N-1

answer = 10 ** 9
while start < end:
    tmp = numbers[start] + numbers[end]
    if abs(tmp) < abs(answer):
        answer = tmp
    if tmp < 0:
        start += 1
    else:
        end -= 1

print(answer)