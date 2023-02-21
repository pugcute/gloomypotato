

point = []
for _ in range(3):
    tmp = list(map(int, input().split()))
    point.append(tmp)


def CCW(p1, p2, p3):
    return (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1])


answer = CCW(point[0], point[1], point[2])
if answer > 0:
    print(1)
elif answer == 0:
    print(0)
else:
    print(-1)