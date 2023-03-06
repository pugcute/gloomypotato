N = int(input())
numbers = list(map(int, input().split()))

start = 0
end = N - 1
answer = 2000000000000
answer_list = []

while start < end:
    tmp = numbers[start] + numbers[end]
    if abs(tmp) < answer:
        answer = abs(tmp)
        answer_list = [numbers[start], numbers[end]]
    if tmp < 0:
        start += 1
    else:
        end -= 1

print(*answer_list)