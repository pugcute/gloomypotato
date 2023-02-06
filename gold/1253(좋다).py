N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

answer = 0
for i in range(N):
    temp = numbers[:i] + numbers[i+1:]
    start, end = 0, len(temp) - 1

    while start < end:
        total = temp[start] + temp[end]
        if total == numbers[i]:
            answer += 1
            break
        elif total < numbers[i]:
            start += 1
        else:
            end -= 1

print(answer)