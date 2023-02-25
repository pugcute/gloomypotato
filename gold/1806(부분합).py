N, S = map(int, input().split())
numbers = list(map(int, input().split()))

left = 0
right = 0
answer = 10**9
sums = numbers[0]

while left <= right:
    if sums >= S:
        answer = min(answer, right - left + 1)
        sums -= numbers[left]
        left += 1
    else:
        right += 1
        if right < N:
            sums += numbers[right]
        else:
            break

if answer == 10**9:
    answer = 0
print(answer)