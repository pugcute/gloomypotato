N = int(input())
times = list(map(int, input().split()))

prev = 0
answer = 0
cnt = 0
while cnt < N:
    times.sort(reverse=True)
    step = times.pop()
    prev += step
    answer += prev
    cnt += 1

print(answer)