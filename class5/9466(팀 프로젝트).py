import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    students = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [False] * (N + 1)
    answer = 0
    for i in range(1, N + 1):
        if visited[i]:
            continue
        to_visits = [i]
        while True:
            visited[to_visits[-1]] = True
            if visited[students[to_visits[-1]]]:
                if students[to_visits[-1]] in to_visits:
                    answer += len(to_visits) - to_visits.index(students[to_visits[-1]])
                break
            to_visits.append(students[to_visits[-1]])

    print(N - answer)