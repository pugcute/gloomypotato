
import math
N = int(input())
answer = 0
for i in range(0, N+1, 5):
    if i in [5, 25, 125]:
        answer += int(math.sqrt(i))
    else:
        answer += 1
print(answer)