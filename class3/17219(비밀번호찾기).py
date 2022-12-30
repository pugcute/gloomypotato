import sys

N, M = map(int, input().split())
webpages = {}
for _ in range(N):
    webpage, password = map(str, sys.stdin.readline().split())
    webpages[webpage] = password


for _ in range(M):
    problem = sys.stdin.readline().rstrip()
    print(webpages[problem])