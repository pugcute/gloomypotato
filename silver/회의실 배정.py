import sys

n = int(input())
classTimes = []
for i in range(n):
    classTime = list(map(int, sys.stdin.readline().split()))
    classTimes.append(classTime)
classTimes.sort(key=lambda x:x[1])

finishTime = classTimes[0][1]
answer = 1

while True:

    classTimes.sort(key=lambda x:x[0], reverse=True)

    for classTime in classTimes[::-1]:
        if classTime[0] < finishTime:
            classTimes.pop()
        else:
            break

    if len(classTimes) == 0:
        break
    classTimes.sort(key=lambda x:x[1])

    finishTime = classTimes[0][1]
    answer += 1

print(answer)

