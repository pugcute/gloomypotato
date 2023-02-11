import sys
from collections import deque


N, L = map(int, sys.stdin.readline().split())
# Di = Ai-L+1 ~ Ai 중
answer = deque()
numbers = list(map(int, sys.stdin.readline().split()))


for idx, number in enumerate(numbers):
    while answer and answer[0][1] <= idx - L:
        answer.popleft()
    while answer and answer[-1][0] >= number:
        answer.pop()
    answer.append([number, idx])
    print(answer[0][0], end=' ')
