
N = int(input())
numbers= list(map(int, input().split()))
numbers1 = list(map(int, input().split()))
numbers.sort()
numbers1.sort(reverse=True)

answer = 0
for idx in range(N):
    answer +=  numbers[idx] * numbers1[idx]
print(answer)