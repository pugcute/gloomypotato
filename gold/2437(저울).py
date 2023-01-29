N = int(input())

numbers = list(map(int, input().split()))

numbers.sort()

answer = 1
for i in range(N):
    if answer < numbers[i]:
        break
    answer += numbers[i]
print(answer)