import sys

N = int(sys.stdin.readline())
crains = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))

boxes.sort(reverse=True)
crains.sort(reverse=True)

time = 0

if max(boxes) > max(crains):
    print(-1)
    sys.exit()

while len(boxes) > 0:
    time += 1
    for i in range(len(crains)):
        for j in range(len(boxes)):
            if crains[i] >= boxes[j]:
                del boxes[j]
                break


print(time)

